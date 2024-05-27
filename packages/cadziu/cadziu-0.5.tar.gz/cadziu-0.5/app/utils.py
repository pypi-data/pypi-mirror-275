import requests
import subprocess
import json
import os
import logging
import time

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def add_dns_record(subdomain, ip_address, api_token, zone_id, max_retries=3, initial_wait_time=5):
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
            return True
        else:
            error_info = response.json()
            logger.error(f"Failed to add DNS record: {json.dumps(error_info, indent=2)}")
            if response.status_code == 429 or any(e['code'] == 971 for e in error_info.get('errors', [])):
                logger.info(f"Retrying in {wait_time} seconds...")
                time.sleep(wait_time)
                wait_time *= 2
            else:
                return False
    return False

def is_resolvable(subdomain):
    try:
        result = subprocess.run(['dig', '+short', '@1.1.1.1', subdomain], capture_output=True, text=True)
        return bool(result.stdout.strip())
    except subprocess.SubprocessError:
        return False

def execute_docker_command(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            logger.info(f"Command executed successfully: {command}")
            return True
        else:
            logger.error(f"Failed to execute command: {result.stderr}")
            return False
    except Exception as e:
        logger.error(f"Error executing command: {e}")
        return False
