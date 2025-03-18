# Install necessary packages
!pip install python-nmap

# Import necessary libraries
import nmap
import socket

# Function to enumerate open ports and services using nmap
def enumerate_ports_and_services(target):
    print(f"Enumerating open ports and services for target: {target}")
    nm = nmap.PortScanner()
    scan_result = nm.scan(hosts=target, arguments='-sV -p 1-1024')

    # Display scan results
    for host in nm.all_hosts():
        print(f"\nHost: {host} ({nm[host].hostname()})")
        print(f"State: {nm[host].state()}")
        for protocol in nm[host].all_protocols():
            print(f"\nProtocol: {protocol}")
            ports = nm[host][protocol].keys()
            for port in ports:
                port_info = nm[host][protocol][port]
                print(f"Port: {port}")
                print(f"State: {port_info['state']}")
                print(f"Service: {port_info.get('name', 'unknown')}")
                print(f"Version: {port_info.get('version', 'unknown')}")

# Function to enumerate DNS records using socket
def enumerate_dns_records(target):
    print(f"\nEnumerating DNS records for target: {target}")
    try:
        ip_address = socket.gethostbyname(target)
        print(f"IP Address: {ip_address}")
        print("\nDNS Records:")
        for alias in socket.gethostbyaddr(ip_address):
            print(f"Alias: {alias}")
    except Exception as e:
        print(f"Error retrieving DNS records: {e}")

# Example usage:
target_ip = "scanme.nmap.org"  # Replace with your desired target

# Enumerate open ports and services
enumerate_ports_and_services(target_ip)

# Enumerate DNS records
enumerate_dns_records(target_ip)
