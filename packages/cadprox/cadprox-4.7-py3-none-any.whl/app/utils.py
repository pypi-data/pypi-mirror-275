import requests
import subprocess
import socket
import os
import re
import time
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError, ClientError
import json
import sys
import logging
import traceback
from dotenv import load_dotenv

# Load environment variables from user's current directory
def load_user_env():
    current_working_directory = os.getcwd()
    dotenv_path = os.path.join(current_working_directory, '.env')
    load_dotenv(dotenv_path)

load_user_env()

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Fetch and export environment variables
S3_ACCESS_KEY = os.getenv('S3_ACCESS_KEY')
S3_SECRET_KEY = os.getenv('S3_SECRET_KEY')
S3_REGION = os.getenv('S3_REGION')
S3_BUCKET = os.getenv('S3_BUCKET')
S3_CADDY_FILENAME = os.getenv('S3_CADDY_FILENAME', 'Caddyfile')

# Log the environment variables
logger.info(f"S3_ACCESS_KEY: {S3_ACCESS_KEY}")
logger.info(f"S3_SECRET_KEY: {S3_SECRET_KEY}")
logger.info(f"S3_REGION: {S3_REGION}")
logger.info(f"S3_BUCKET: {S3_BUCKET}")
logger.info(f"S3_CADDY_FILENAME: {S3_CADDY_FILENAME}")

# Validate environment variables
if not all([S3_ACCESS_KEY, S3_SECRET_KEY, S3_REGION, S3_BUCKET]):
    logger.error("One or more required environment variables are missing or not loaded correctly.")
    sys.exit(1)

os.environ['S3_ACCESS_KEY'] = S3_ACCESS_KEY
os.environ['S3_SECRET_KEY'] = S3_SECRET_KEY
os.environ['S3_REGION'] = S3_REGION
os.environ['S3_BUCKET'] = S3_BUCKET

def load_s3_client():
    return boto3.client(
        's3',
        aws_access_key_id=os.getenv('S3_ACCESS_KEY'),
        aws_secret_access_key=os.getenv('S3_SECRET_KEY'),
        region_name=os.getenv('S3_REGION')
    )

def get_external_ip():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        response.raise_for_status()
        return response.json()['ip']
    except requests.RequestException as e:
        logger.error(f"Error retrieving external IP address: {e}")
        return None

def add_dns_record(subdomain, ip_address, api_token, zone_id, max_retries=1, initial_wait_time=5):
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
    for attempt in range(max_retries + 1):
        response = requests.post(url, headers=headers, data=json.dumps(data))
        if response.status_code == 200:
            success_info = response.json()
            logger.info(f"Successfully added DNS record: {json.dumps(success_info, indent=2)}")
            return True
        else:
            error_info = response.json()
            if any(e['code'] == 81057 for e in error_info.get('errors', [])):
                # If the record already exists, proceed without error
                logger.info(f"DNS record for {subdomain} already exists. Continuing...")
                return True
            logger.error(f"Failed to add DNS record: {json.dumps(error_info, indent=2)}")
            if response.status_code == 429 or any(e['code'] == 971 for e in error_info.get('errors', [])):
                if attempt < max_retries:
                    logger.info(f"Retrying in {wait_time} seconds...")
                    time.sleep(wait_time)
                    wait_time *= 2
                else:
                    logger.warning("Max retries exceeded or throttling issue. Please consider throttling your request speed.")
                    user_input = input("Add host to Caddyfile anyway? (yes/no): ").strip().lower()
                    if user_input == 'yes':
                        return True
                    else:
                        return False
            else:
                return False
    return False

def download_caddyfile_from_s3(s3_client, bucket_name, s3_caddy_filename, local_caddyfile_path):
    try:
        logger.info(f"Downloading Caddyfile from bucket: {bucket_name}, key: {s3_caddy_filename}")
        s3_client.download_file(bucket_name, s3_caddy_filename, local_caddyfile_path)
        logger.info(f"Downloaded Caddyfile from S3 bucket {bucket_name}")
    except ClientError as e:
        if e.response['Error']['Code'] == '404':
            logger.info(f"Caddyfile {s3_caddy_filename} not found in S3 bucket {bucket_name}. Creating a new one.")
            with open(local_caddyfile_path, 'w') as f:
                f.write('')
        else:
            logger.error(f"Error downloading Caddyfile from S3: {e}")
            logger.error(traceback.format_exc())
            sys.exit(1)
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
        logger.info(f"Uploading Caddyfile to bucket: {bucket_name}, key: {s3_caddy_filename}")
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

def get_caddyfile_path(docker=False):
    config_dir = os.path.expanduser('~/cadprox_config')
    if docker:
        return os.path.join(config_dir, 'Caddyfile_docker')
    return os.path.join(config_dir, 'Caddyfile')

def update_caddyfile(subdomain, port, caddyfile_path=None, backend_ip='localhost'):
    new_entry = f"{subdomain} {{\n    reverse_proxy {backend_ip}:{port}\n}}\n"
    logger.info(f"Adding new entry to Caddyfile at path: {caddyfile_path}")
    logger.info(f"New entry: {new_entry}")
    try:
        with open(caddyfile_path, 'a') as caddy_file:
            caddy_file.write(new_entry)
        logger.info(f"Updated Caddyfile with new entry for {subdomain}")
    except PermissionError:
        logger.error(f"Permission denied when trying to write to {caddyfile_path}")
        logger.error(traceback.format_exc())
    except Exception as e:
        logger.error(f"Error updating Caddyfile: {e}")
        logger.error(traceback.format_exc())

def remove_caddyfile_entry(subdomain, caddyfile_path=None):
    try:
        with open(caddyfile_path, 'r') as caddy_file:
            content = caddy_file.read()
        new_content = re.sub(rf"{subdomain} \{{.*?\}}\n", '', content, flags=re.DOTALL)
        with open(caddyfile_path, 'w') as caddy_file:
            caddy_file.write(new_content)
        logger.info(f"Removed Caddyfile entry for {subdomain}")
    except PermissionError:
        logger.error(f"Permission denied when trying to modify {caddyfile_path}")
        logger.error(traceback.format_exc())
    except FileNotFoundError:
        logger.error(f"Caddyfile {caddyfile_path} not found.")
    except Exception as e:
        logger.error(f"Error removing Caddyfile entry: {e}")
        logger.error(traceback.format_exc())

def format_caddyfile(caddyfile_path=None, docker=False):
    if docker:
        format_caddyfile_docker(caddyfile_path)
    else:
        format_caddyfile_system(caddyfile_path)

def restart_caddy(caddyfile_path=None, docker=False):
    if docker:
        restart_caddy_docker(caddyfile_path)
    else:
        restart_caddy_system(caddyfile_path)

def is_caddy_running_in_docker():
    try:
        result = subprocess.run(['docker', 'ps', '--filter', 'name=caddy', '--format', '{{.Names}}'], capture_output=True, text=True)
        return 'caddy' in result.stdout.strip().split('\n')
    except Exception as e:
        logger.error(f"Error checking Docker containers: {e}")
        return False

def verify_caddyfile_existence_and_permissions(caddyfile_path):
    if os.path.exists(caddyfile_path):
        logger.info(f"Caddyfile exists at {caddyfile_path}")
        if os.access(caddyfile_path, os.R_OK):
            logger.info(f"Caddyfile at {caddyfile_path} is readable")
        else:
            logger.error(f"Caddyfile at {caddyfile_path} is not readable. Check permissions.")
            return False
    else:
        logger.error(f"Caddyfile at {caddyfile_path} does not exist")
        return False
    return True

def get_caddyfile_paths(docker):
    if docker:
        try:
            result = subprocess.run(['docker', 'inspect', 'caddy'], capture_output=True, text=True, check=True)
            containers = json.loads(result.stdout)
            if containers:
                container = containers[0]
                binds = container['HostConfig']['Binds']
                for bind in binds:
                    if '/etc/caddy/Caddyfile' in bind:
                        local_path, docker_path = bind.split(':')
                        return local_path, docker_path
            return None, None
        except subprocess.CalledProcessError as e:
            logger.error(f"Error inspecting Docker container: {e}")
            return None, None
    else:
        local_path = get_caddyfile_path(docker=False)
        return local_path, None

def format_caddyfile_docker(caddyfile_path=None):
    local_path, docker_path = get_caddyfile_paths(docker=True)
    if local_path and verify_caddyfile_existence_and_permissions(local_path):
        result = subprocess.run(
            ['docker', 'exec', 'caddy', 'caddy', 'fmt', '--overwrite', docker_path],
            capture_output=True, text=True
        )
        if result.returncode == 0:
            logger.info("Caddyfile formatted successfully within Docker")
        else:
            logger.error(f"Failed to format Caddyfile within Docker: {result.stderr}")

def format_caddyfile_system(caddyfile_path=None):
    caddyfile_path = caddyfile_path or get_caddyfile_path(docker=False)
    result = subprocess.run(['caddy', 'fmt', '--overwrite', caddyfile_path], capture_output=True, text=True)
    if result.returncode == 0:
        logger.info("Caddyfile formatted successfully")
    else:
        logger.error(f"Failed to format Caddyfile: {result.stderr}")

def restart_caddy_docker(caddyfile_path=None):
    local_path, docker_path = get_caddyfile_paths(docker=True)
    if local_path and verify_caddyfile_existence_and_permissions(local_path):
        result = subprocess.run(
            ['docker', 'exec', 'caddy', 'caddy', 'reload', '--config', docker_path],
            capture_output=True, text=True
        )
        if result.returncode == 0:
            logger.info("Caddy server reloaded successfully within Docker")
        else:
            logger.error(f"Failed to reload Caddy server in Docker: {result.stderr}")

def restart_caddy_system(caddyfile_path=None):
    caddyfile_path = caddyfile_path or get_caddyfile_path(docker=False)
    result = subprocess.run(['caddy', 'reload', '--config', caddyfile_path], capture_output=True, text=True)
    if result.returncode == 0:
        logger.info("Caddy server reloaded successfully")
    else:
        logger.error(f"Failed to reload Caddy server: {result.stderr}")

def check_port_in_use(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        return sock.connect_ex(('localhost', int(port))) == 0

def check_domain_exists(subdomain, caddyfile_path=None):
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

def load_profiles(s3_client, docker=False):
    key = 'caddy_profiles_docker.json' if docker else 'caddy_profiles.json'
    try:
        response = s3_client.get_object(Bucket=os.getenv('S3_BUCKET'), Key=key)
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

def create_profile(profile_name, docker=False):
    profile = prompt_for_profile()
    profile_key = profile["MAIN_DOMAIN"]
    s3_client = load_s3_client()

    try:
        caddy_profiles = load_profiles(s3_client, docker)
    except Exception as e:
        caddy_profiles = {}

    caddy_profiles[profile_key] = profile

    key = 'caddy_profiles_docker.json' if docker else 'caddy_profiles.json'
    try:
        s3_client.put_object(
            Bucket=os.getenv('S3_BUCKET'),
            Key=key,
            Body=json.dumps(caddy_profiles)
        )
        logger.info(f"Profile '{profile_name}' created successfully.")
    except Exception as e:
        logger.error(f"Error creating profile: {e}")
        logger.error(traceback.format_exc())
