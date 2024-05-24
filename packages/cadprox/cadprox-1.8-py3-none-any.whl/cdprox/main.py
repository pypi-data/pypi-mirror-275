import argparse
import os
import sys
import boto3
from .utils import (
    get_external_ip,
    add_dns_record,
    download_caddyfile_from_s3,
    upload_caddyfile_to_s3,
    update_caddyfile,
    format_caddyfile,
    restart_caddy,
    check_port_in_use,
    check_domain_exists,
    wait_until_resolvable
)

def main():

    parser = argparse.ArgumentParser(description='CDProxy Command Line Tool')
    parser.add_argument('command', choices=['add'], help='Command to execute')
    parser.add_argument('subdomain', help='Subdomain to add')
    parser.add_argument('-p', '--port', required=True, help='Backend server port')

    args = parser.parse_args()

    if args.command == 'add':
        subdomain = args.subdomain
        backend_server_port = args.port

        api_token = os.getenv('CLOUDFLARE_API_TOKEN')
        zone_id = os.getenv('CLOUDFLARE_ZONE_ID')
        s3_access_key = os.getenv('S3_ACCESS_KEY')
        s3_secret_key = os.getenv('S3_SECRET_KEY')
        s3_region = os.getenv('S3_REGION')
        s3_bucket = os.getenv('S3_BUCKET')
        s3_caddy_filename = os.getenv('S3_CADDY_FILENAME', 'Caddyfile')

        if not api_token or not zone_id:
            logger.error("Error: Cloudflare API token and zone ID must be set as environment variables.")
            sys.exit(1)

        if not s3_access_key or not s3_secret_key or not s3_region or not s3_bucket:
            logger.error("Error: S3 access key, secret key, region, and bucket name must be set as environment variables.")
            sys.exit(1)

        external_ip = get_external_ip()
        if not external_ip:
            logger.error("Failed to retrieve external IP address.")
            sys.exit(1)

        if check_port_in_use(backend_server_port):
            logger.error(f"Error: Port {backend_server_port} is already in use.")
            sys.exit(1)

        add_dns_record(subdomain, external_ip, api_token, zone_id)
        wait_until_resolvable(subdomain)

        s3_client = boto3.client(
            's3',
            aws_access_key_id=s3_access_key,
            aws_secret_access_key=s3_secret_key,
            region_name=s3_region
        )

        local_caddyfile_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'Caddyfile')

        download_caddyfile_from_s3(s3_client, s3_bucket, s3_caddy_filename, local_caddyfile_path)

        if check_domain_exists(subdomain, local_caddyfile_path):
            logger.error(f"Error: Domain {subdomain} already exists in the Caddy configuration.")
            sys.exit(1)

        update_caddyfile(subdomain, backend_server_port, local_caddyfile_path)
        format_caddyfile(local_caddyfile_path)
        upload_caddyfile_to_s3(s3_client, s3_bucket, s3_caddy_filename, local_caddyfile_path)
        restart_caddy()

if __name__ == "__main__":
    main()
