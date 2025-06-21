Sentinel Frog — Public Recon Tool (Lite Edition)

Author: Ghost Commander

Purpose: Public release for ethical recon testing

Donate: https://buymeacoffee.com/ghostfrog

import subprocess import requests import json import os

class PublicRecon: def init(self, target): self.target = target self.result = { 'target': target, 'ip': None, 'subdomains': [], 'open_ports': [], 'cms': None }

def resolve_ip(self):
    try:
        print("[+] Resolving IP address...")
        ip = subprocess.check_output(['dig', '+short', self.target]).decode().strip()
        self.result['ip'] = ip
    except Exception as e:
        self.result['ip'] = f"Error: {e}"

def find_subdomains(self):
    try:
        print("[+] Finding subdomains (using subfinder)...")
        output = subprocess.check_output(['subfinder', '-d', self.target, '-silent']).decode()
        self.result['subdomains'] = output.strip().split('\n')
    except Exception as e:
        self.result['subdomains'] = [f"Error: {e}"]

def scan_ports(self):
    try:
        print("[+] Scanning ports (fast)...")
        output = subprocess.check_output(['nmap', '-T4', '-F', self.target]).decode()
        ports = [line for line in output.split('\n') if '/tcp' in line and 'open' in line]
        self.result['open_ports'] = ports
    except Exception as e:
        self.result['open_ports'] = [f"Error: {e}"]

def detect_cms(self):
    try:
        print("[+] Detecting CMS (with whatweb)...")
        output = subprocess.check_output(['whatweb', self.target]).decode().strip()
        self.result['cms'] = output
    except Exception as e:
        self.result['cms'] = f"Error: {e}"

def run_all(self):
    self.resolve_ip()
    self.find_subdomains()
    self.scan_ports()
    self.detect_cms()
    return self.result

if name == "main": print("Sentinel Frog Lite — Public Recon Tool") print("Use responsibly. For ethical testing only.") target = input("Enter target domain: ") recon = PublicRecon(target) results = recon.run_all() print("\n[+] Scan Result:") print(json.dumps(results, indent=4)) print("\nDonate if useful: https://buymeacoffee.com/ghostfrog")

