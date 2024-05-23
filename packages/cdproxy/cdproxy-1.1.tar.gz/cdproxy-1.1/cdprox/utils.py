import subprocess
import socket
import os
import re
import time
import requests
import json
def get_external_ip():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        response.raise_for_status()
        return response.json()['ip']
    except requests.RequestException as e:
        print(f"Error retrieving external IP address: {e}")
        return None

def add_dns_record(subdomain, ip_address, api_token, zone_id):
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
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        print(f"Successfully added DNS record: {subdomain} -> {ip_address}")
    else:
        print(f"Failed to add DNS record: {response.json()}")

def update_caddyfile(subdomain, port, caddyfile_path):
    new_entry = f"{subdomain} {{\n    reverse_proxy localhost:{port}\n}}\n"
    try:
        with open(caddyfile_path, 'a') as caddy_file:
            caddy_file.write(new_entry)
        print(f"Updated Caddyfile with new entry for {subdomain}")
    except PermissionError:
        print(f"Permission denied when trying to write to {caddyfile_path}")

def format_caddyfile(caddyfile_path):
    result = subprocess.run(['caddy', 'fmt', '--overwrite', caddyfile_path], capture_output=True, text=True)
    if result.returncode == 0:
        print("Caddyfile formatted successfully")
    else:
        print(f"Failed to format Caddyfile: {result.stderr}")

def restart_caddy(caddyfile_path):
    result = subprocess.run(['caddy', 'reload', '--config', caddyfile_path], capture_output=True, text=True)
    if result.returncode == 0:
        print("Caddy server reloaded successfully")
    else:
        print(f"Failed to reload Caddy server: {result.stderr}")

def check_port_in_use(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        return sock.connect_ex(('localhost', int(port))) == 0

def check_domain_exists(subdomain, caddyfile_path):
    try:
        with open(caddyfile_path, 'r') as caddy_file:
            content = caddy_file.read()
            return re.search(rf"{subdomain} \{{.*?\}}", content, flags=re.DOTALL) is not None
    except FileNotFoundError:
        print(f"Caddyfile {caddyfile_path} not found.")
        return False
    except PermissionError:
        print(f"Permission denied when accessing {caddyfile_path}.")
        return False

def is_resolvable(subdomain):
    try:
        result = subprocess.run(['dig', '+short', '@1.1.1.1', subdomain], capture_output=True, text=True)
        return bool(result.stdout.strip())
    except subprocess.SubprocessError:
        return False

def wait_until_resolvable(subdomain, max_attempts=50, wait_time=5):
    attempts = 0
    while attempts < max_attempts:
        if is_resolvable(subdomain):
            print(f"{subdomain} is now resolvable")
            return True
        print(f"Waiting for {subdomain} to become resolvable... ({attempts + 1}/{max_attempts})")
        time.sleep(wait_time)
        attempts += 1
    print(f"{subdomain} is not resolvable after {max_attempts} attempts, continuing anyway")
    return False
