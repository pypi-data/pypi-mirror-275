import requests
import subprocess
import socket
import os
import re
import time
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError
import json
import sys
import logging
import traceback
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

S3_ACCESS_KEY = os.getenv('S3_ACCESS_KEY')
S3_SECRET_KEY = os.getenv('S3_SECRET_KEY')
S3_REGION = os.getenv('S3_REGION')
S3_BUCKET = os.getenv('S3_BUCKET')
S3_CADDY_FILENAME = os.getenv('S3_CADDY_FILENAME', 'Caddyfile')

def load_s3_client():
    return boto3.client(
        's3',
        aws_access_key_id=S3_ACCESS_KEY,
        aws_secret_access_key=S3_SECRET_KEY,
        region_name=S3_REGION
    )

def get_external_ip():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        response.raise_for_status()
        return response.json()['ip']
    except requests.RequestException as e:
        logger.error(f"Error retrieving external IP address: {e}")
        return None

def add_dns_record(subdomain, ip_address, api_token, zone_id, max_retries=5, initial_wait_time=5):
    url = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records"
    headers = {
        'Authorization': f"Bearer {api_token}",
        'Content-Type': 'application/json'
    }
    data = {
        'type': 'A',
        'name': subdomain,
        'content': ip_address,
        'ttl': 120,
        'proxied': True
    }

    wait_time = initial_wait_time
    for attempt in range(max_retries):
        response = requests.post(url, headers=headers, data=json.dumps(data))
        if response.status_code == 200:
            success_info = response.json()
            logger.info(f"Successfully added DNS record: {json.dumps(success_info, indent=2)}")
            return
        else:
            error_info = response.json()
            logger.error(f"Failed to add DNS record: {json.dumps(error_info, indent=2)}")
            if response.status_code == 429 or any(e['code'] == 971 for e in error_info.get('errors', [])):
                # If rate limited, wait and retry
                logger.info(f"Retrying in {wait_time} seconds...")
                time.sleep(wait_time)
                wait_time *= 2  # Exponential backoff
            else:
                sys.exit(1)  # Exit if the DNS record addition fails due to other reasons
    logger.error("Max retries exceeded. Could not add DNS record.")
    sys.exit(1)

def download_caddyfile_from_s3(s3_client, bucket_name, s3_caddy_filename, local_caddyfile_path):
    try:
        s3_client.download_file(bucket_name, s3_caddy_filename, local_caddyfile_path)
        logger.info(f"Downloaded Caddyfile from S3 bucket {bucket_name}")
    except s3_client.exceptions.NoSuchKey:
        logger.info(f"Caddyfile {s3_caddy_filename} not found in S3 bucket {bucket_name}. Creating a new one.")
        with open(local_caddyfile_path, 'w') as f:
            f.write('')  # Create an empty Caddyfile
    except NoCredentialsError:
        logger.error("AWS credentials not available.")
        sys.exit(1)
    except PartialCredentialsError:
        logger.error("Incomplete AWS credentials provided.")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Error downloading Caddyfile from S3: {e}")
        logger.error(traceback.format_exc())
        sys.exit(1)

def upload_caddyfile_to_s3(s3_client, bucket_name, s3_caddy_filename, local_caddyfile_path):
    try:
        s3_client.upload_file(local_caddyfile_path, bucket_name, s3_caddy_filename)
        logger.info(f"Uploaded Caddyfile to S3 bucket {bucket_name}")
    except NoCredentialsError:
        logger.error("AWS credentials not available.")
        sys.exit(1)
    except PartialCredentialsError:
        logger.error("Incomplete AWS credentials provided.")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Error uploading Caddyfile to S3: {e}")
        logger.error(traceback.format_exc())
        sys.exit(1)

def update_caddyfile(subdomain, port, caddyfile_path):
    new_entry = f"{subdomain} {{\n    reverse_proxy localhost:{port}\n}}\n"
    try:
        with open(caddyfile_path, 'a') as caddy_file:
            caddy_file.write(new_entry)
        logger.info(f"Updated Caddyfile with new entry for {subdomain}")
    except PermissionError:
        logger.error(f"Permission denied when trying to write to {caddyfile_path}")
        logger.error(traceback.format_exc())

def format_caddyfile(caddyfile_path):
    result = subprocess.run(['caddy', 'fmt', '--overwrite', caddyfile_path], capture_output=True, text=True)
    if result.returncode == 0:
        logger.info("Caddyfile formatted successfully")
    else:
        logger.error(f"Failed to format Caddyfile: {result.stderr}")

def restart_caddy():
    result = subprocess.run(['sudo', 'caddy', 'reload'], capture_output=True, text=True)
    if result.returncode == 0:
        logger.info("Caddy server reloaded successfully")
    else:
        logger.error(f"Failed to reload Caddy server: {result.stderr}")

def check_port_in_use(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        return sock.connect_ex(('localhost', int(port))) == 0

def check_domain_exists(subdomain, caddyfile_path):
    try:
        with open(caddyfile_path, 'r') as caddy_file:
            content = caddy_file.read()
            return re.search(rf"{subdomain} \{{.*?\}}", content, flags=re.DOTALL) is not None
    except FileNotFoundError:
        logger.error(f"Caddyfile {caddyfile_path} not found.")
        return False
    except PermissionError:
        logger.error(f"Permission denied when accessing {caddyfile_path}.")
        return False

def is_resolvable(subdomain):
    try:
        result = subprocess.run(['dig', '+short', '@1.1.1.1', subdomain], capture_output=True, text=True)
        return bool(result.stdout.strip())
    except subprocess.SubprocessError:
        return False

def wait_until_resolvable(subdomain, max_attempts=10, wait_time=5):
    attempts = 0
    while attempts < max_attempts:
        if is_resolvable(subdomain):
            logger.info(f"{subdomain} is now resolvable")
            return True
        logger.info(f"Waiting for {subdomain} to become resolvable... ({attempts + 1}/{max_attempts})")
        time.sleep(wait_time)
        attempts += 1
    logger.warning(f"{subdomain} is not resolvable after {max_attempts} attempts, continuing anyway")
    return False

def load_profiles(s3_client):
    try:
        response = s3_client.get_object(Bucket=S3_BUCKET, Key='caddy_profiles.json')
        profiles = json.loads(response['Body'].read().decode('utf-8'))
        return profiles
    except s3_client.exceptions.NoSuchKey:
        return {}
    except NoCredentialsError:
        logger.error("AWS credentials not available.")
        return {}
    except PartialCredentialsError:
        logger.error("Incomplete AWS credentials provided.")
        return {}
    except Exception as e:
        logger.error(f"Error loading profiles: {e}")
        logger.error(traceback.format_exc())
        return {}

def prompt_for_profile():
    profile = {
        "CLOUDFLARE_API_TOKEN": input("CLOUDFLARE_API_TOKEN: "),
        "CLOUDFLARE_ZONE_ID": input("CLOUDFLARE_ZONE_ID: "),
        "S3_CADDY_FILENAME": input("S3_CADDY_FILENAME: "),
        "MAIN_DOMAIN": input("MAIN_DOMAIN: ")
    }
    return profile

def create_profile(profile_name):
    profile = prompt_for_profile()
    profile_key = profile["MAIN_DOMAIN"]
    s3_client = load_s3_client()

    try:
        caddy_profiles = load_profiles(s3_client)
    except Exception as e:
        caddy_profiles = {}

    caddy_profiles[profile_key] = profile

    try:
        s3_client.put_object(
            Bucket=S3_BUCKET,
            Key='caddy_profiles.json',
            Body=json.dumps(caddy_profiles)
        )
        logger.info(f"Profile '{profile_name}' created successfully.")
    except Exception as e:
        logger.error(f"Error creating profile: {e}")
        logger.error(traceback.format_exc())
