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
    remove_caddyfile_entry,
    format_caddyfile,
    restart_caddy,
    check_port_in_use,
    check_domain_exists,
    wait_until_resolvable,
    load_profiles,
    create_profile,
    get_caddyfile_path  # Ensure this is imported
)

def main():
    """
    The main function of the CADProxy Command Line Tool.
    Parses command line arguments and executes the corresponding commands.
    """
    parser = argparse.ArgumentParser(description='CADProxy Command Line Tool')
    parser.add_argument('command', choices=['add', 'create', 'remove', 'docker_add', 'docker_create', 'docker_remove'], help='Command to execute')
    parser.add_argument('subdomain', help='Subdomain to add or remove', nargs='?')
    parser.add_argument('-p', '--port', required=False, help='Backend server port')

    args = parser.parse_args()

    try:
        if args.command == 'create' or args.command == 'docker_create':
            profile_name = args.subdomain
            docker = args.command == 'docker_create'
            if profile_name:
                create_profile(profile_name, docker)
            else:
                raise ValueError("Error: Profile name must be provided.")

        if args.command in ['add', 'docker_add']:
            if not args.subdomain or not args.port:
                raise ValueError("Error: Subdomain and port must be provided.")

            subdomain = args.subdomain
            backend_server_port = args.port
            docker = args.command == 'docker_add'

            s3_client = boto3.client(
                's3',
                aws_access_key_id=os.getenv('S3_ACCESS_KEY'),
                aws_secret_access_key=os.getenv('S3_SECRET_KEY'),
                region_name=os.getenv('S3_REGION')
            )

            profiles = load_profiles(s3_client, docker)
            main_domain = ".".join(subdomain.split(".")[-2:])

            profile = profiles.get(main_domain)

            if not profile:
                raise ValueError(f"Error: No profile found for main domain '{main_domain}'.")

            api_token = profile['CLOUDFLARE_API_TOKEN']
            zone_id = profile['CLOUDFLARE_ZONE_ID']
            s3_caddy_filename = profile.get('S3_CADDY_FILENAME', 'Caddyfile_docker' if docker else 'Caddyfile')
            if not s3_caddy_filename:
                s3_caddy_filename = 'Caddyfile_docker' if docker else 'Caddyfile'

            external_ip = get_external_ip()
            if not external_ip:
                raise ValueError("Failed to retrieve external IP address.")

            backend_ip = '172.17.0.1' if docker else 'localhost'

            if check_port_in_use(backend_server_port):
                print(f"Warning: Port {backend_server_port} is already in use.")
                # Continue without exiting

            if add_dns_record(subdomain, external_ip, api_token, zone_id):
                wait_until_resolvable(subdomain)

                local_caddyfile_path = get_caddyfile_path(docker)

                download_caddyfile_from_s3(s3_client, os.getenv('S3_BUCKET'), s3_caddy_filename, local_caddyfile_path)

                if check_domain_exists(subdomain, local_caddyfile_path):
                    raise ValueError(f"Error: Domain {subdomain} already exists in the Caddy configuration.")

                update_caddyfile(subdomain, backend_server_port, local_caddyfile_path, backend_ip)
                format_caddyfile(local_caddyfile_path, docker)
                upload_caddyfile_to_s3(s3_client, os.getenv('S3_BUCKET'), s3_caddy_filename, local_caddyfile_path)
                restart_caddy(local_caddyfile_path, docker)

        if args.command in ['remove', 'docker_remove']:
            subdomain = args.subdomain
            docker = args.command == 'docker_remove'
            if not subdomain:
                raise ValueError("Error: Subdomain must be provided.")

            s3_client = boto3.client(
                's3',
                aws_access_key_id=os.getenv('S3_ACCESS_KEY'),
                aws_secret_access_key=os.getenv('S3_SECRET_KEY'),
                region_name=os.getenv('S3_REGION')
            )

            s3_caddy_filename = 'Caddyfile_docker' if docker else 'Caddyfile'
            local_caddyfile_path = get_caddyfile_path(docker)

            download_caddyfile_from_s3(s3_client, os.getenv('S3_BUCKET'), s3_caddy_filename, local_caddyfile_path)
            remove_caddyfile_entry(subdomain, local_caddyfile_path)
            format_caddyfile(local_caddyfile_path, docker)
            upload_caddyfile_to_s3(s3_client, os.getenv('S3_BUCKET'), s3_caddy_filename, local_caddyfile_path)
            restart_caddy(local_caddyfile_path, docker)

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
