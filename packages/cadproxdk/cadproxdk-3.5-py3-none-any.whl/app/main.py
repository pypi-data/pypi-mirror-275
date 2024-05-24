import argparse
import os
import sys
import logging
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
    create_profile,
    load_s3_client
)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def main():
    print(f"Python executable: {sys.executable}")
    print(f"Python path: {sys.path}")

    parser = argparse.ArgumentParser(description='CADProxy Command Line Tool')
    parser.add_argument('command', choices=['add', 'create'], help='Command to execute')
    parser.add_argument('domain', help='Domain to add or create profile for')
    parser.add_argument('-p', '--port', required=False, help='Backend server port (required for add command)')

    args = parser.parse_args()

    if args.command == 'create':
        create_profile(args.domain)
    elif args.command == 'add':
        if not args.port:
            logger.error("Port number is required for the add command.")
            sys.exit(1)

        subdomain = args.domain
        backend_server_port = args.port

        api_token = os.getenv('CLOUDFLARE_API_TOKEN')
        zone_id = os.getenv('CLOUDFLARE_ZONE_ID')

        if not api_token or not zone_id:
            logger.error("Cloudflare API token and zone ID must be set as environment variables.")
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

        s3_client = load_s3_client()
        s3_caddy_filename = os.getenv('S3_CADDY_FILENAME', 'Caddyfile')
        local_caddyfile_path = os.path.expanduser(f'~/caddy_config/{s3_caddy_filename}')

        download_caddyfile_from_s3(s3_client, S3_BUCKET, s3_caddy_filename, local_caddyfile_path)

        if check_domain_exists(subdomain):
            logger.error(f"Error: Domain {subdomain} already exists in the Caddy configuration.")
            sys.exit(1)

        update_caddyfile(subdomain, backend_server_port)
        format_caddyfile()
        upload_caddyfile_to_s3(s3_client, S3_BUCKET, s3_caddy_filename, local_caddyfile_path)
        restart_caddy()

if __name__ == "__main__":
    main()
