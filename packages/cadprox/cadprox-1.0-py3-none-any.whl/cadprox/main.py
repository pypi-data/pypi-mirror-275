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
    wait_until_resolvable,
    load_profiles,
    create_profile
)

def main():
    print(f"Python executable: {sys.executable}")
    print(f"Python path: {sys.path}")
    print(f"Boto3 version: {boto3.__version__}")

    parser = argparse.ArgumentParser(description='CADProxy Command Line Tool')
    parser.add_argument('command', choices=['add', 'create'], help='Command to execute')
    parser.add_argument('subdomain', help='Subdomain to add', nargs='?')
    parser.add_argument('-p', '--port', required=False, help='Backend server port')

    args = parser.parse_args()

    if args.command == 'create':
        profile_name = args.subdomain
        if profile_name:
            create_profile(profile_name)
        else:
            print("Error: Profile name must be provided.")
        return

    if args.command == 'add':
        if not args.subdomain or not args.port:
            print("Error: Subdomain and port must be provided.")
            return

        subdomain = args.subdomain
        backend_server_port = args.port

        s3_client = boto3.client(
            's3',
            aws_access_key_id=os.getenv('S3_ACCESS_KEY'),
            aws_secret_access_key=os.getenv('S3_SECRET_KEY'),
            region_name=os.getenv('S3_REGION')
        )

        profiles = load_profiles(s3_client)
        main_domain = ".".join(subdomain.split(".")[-2:])

        profile = profiles.get(main_domain)

        if not profile:
            print(f"Error: No profile found for main domain '{main_domain}'.")
            return

        api_token = profile['CLOUDFLARE_API_TOKEN']
        zone_id = profile['CLOUDFLARE_ZONE_ID']
        s3_access_key = profile['S3_ACCESS_KEY']
        s3_secret_key = profile['S3_SECRET_KEY']
        s3_region = profile['S3_REGION']
        s3_bucket = profile['S3_BUCKET']
        s3_caddy_filename = profile['S3_CADDY_FILENAME']

        external_ip = get_external_ip()
        if not external_ip:
            print("Failed to retrieve external IP address.")
            sys.exit(1)

        if check_port_in_use(backend_server_port):
            print(f"Error: Port {backend_server_port} is already in use.")
            sys.exit(1)

        add_dns_record(subdomain, external_ip, api_token, zone_id)
        wait_until_resolvable(subdomain)

        local_caddyfile_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'Caddyfile')

        download_caddyfile_from_s3(s3_client, s3_bucket, s3_caddy_filename, local_caddyfile_path)

        if check_domain_exists(subdomain, local_caddyfile_path):
            print(f"Error: Domain {subdomain} already exists in the Caddy configuration.")
            sys.exit(1)

        update_caddyfile(subdomain, backend_server_port, local_caddyfile_path)
        format_caddyfile(local_caddyfile_path)
        upload_caddyfile_to_s3(s3_client, s3_bucket, s3_caddy_filename, local_caddyfile_path)
        restart_caddy()

if __name__ == "__main__":
    main()
