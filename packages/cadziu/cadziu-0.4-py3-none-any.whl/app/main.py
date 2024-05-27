import argparse
import os
import sys
import time
from .utils import add_dns_record, is_resolvable, execute_docker_command
from dotenv import load_dotenv

def main():
    load_dotenv()
    
    parser = argparse.ArgumentParser(description='Cadziu Command Line Tool')
    parser.add_argument('command', choices=['add'], help='Command to execute')
    parser.add_argument('subdomain', help='Subdomain to add')
    parser.add_argument('-p', '--port', required=True, help='Backend server port')

    args = parser.parse_args()

    if args.command == 'add':
        subdomain = args.subdomain
        port = args.port
        api_token = os.getenv('CLOUDFLARE_API_TOKEN')
        zone_id = os.getenv('CLOUDFLARE_ZONE_ID')
        
        if not api_token or not zone_id:
            print("Error: CLOUDFLARE_API_TOKEN and CLOUDFLARE_ZONE_ID must be set in the .env file")
            sys.exit(1)

        external_ip = "172.17.0.1"  # Docker network IP

        if add_dns_record(subdomain, external_ip, api_token, zone_id):
            for attempt in range(10):
                if is_resolvable(subdomain):
                    print(f"{subdomain} is now resolvable")
                    break
                print(f"Waiting for {subdomain} to become resolvable... ({attempt + 1}/10)")
                time.sleep(5)
            else:
                print(f"{subdomain} is not resolvable after multiple attempts. Exiting.")
                sys.exit(1)

            command = f'docker exec caddy caddy reverse-proxy --from {subdomain} --to http://localhost:{port}'
            if execute_docker_command(command):
                print(f"Successfully added reverse proxy for {subdomain}")
            else:
                print(f"Failed to add reverse proxy for {subdomain}")
                sys.exit(1)

if __name__ == "__main__":
    main()
