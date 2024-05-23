import argparse
import os
import sys
from cdprox.utils import (
    get_external_ip,
    add_dns_record,
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

        if not api_token or not zone_id:
            print("Error: Cloudflare API token and zone ID must be set as environment variables.")
            sys.exit(1)

        external_ip = get_external_ip()
        if not external_ip:
            print("Failed to retrieve external IP address.")
            sys.exit(1)

        if check_port_in_use(backend_server_port):
            print(f"Port {backend_server_port} is in use.")
            #sys.exit(1)

        add_dns_record(subdomain, external_ip, api_token, zone_id)
        wait_until_resolvable(subdomain)

        # Update the Caddyfile path to use the correct directory
        caddyfile_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Caddyfile')
        if check_domain_exists(subdomain, caddyfile_path):
            print(f"Error: Domain {subdomain} already exists in the Caddy configuration.")
            sys.exit(1)

        update_caddyfile(subdomain, backend_server_port, caddyfile_path)
        restart_caddy(caddyfile_path)
        format_caddyfile(caddyfile_path)
        restart_caddy(caddyfile_path)

if __name__ == "__main__":
    main()
