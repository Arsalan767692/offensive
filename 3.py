# Install necessary packages
!pip install python-nmap scapy

# Import necessary modules
import nmap
from scapy.all import ARP, Ether, srp

# Function for scanning a network for active devices using ARP
def arp_scan(network):
    print(f"Scanning network: {network}")
    # Create ARP packet
    arp = ARP(pdst=network)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp

    # Send the packet and capture the response (increase timeout and enable verbose output)
    result = srp(packet, timeout=5, verbose=1)[0]  # Timeout increased to 5 seconds, verbose=1 for debug info

    # Parse the result
    devices = []
    for sent, received in result:
        devices.append({'IP': received.psrc, 'MAC': received.hwsrc})

    print("Active devices on the network:")
    if devices:
        for device in devices:
            print(f"IP: {device['IP']}, MAC: {device['MAC']}")
    else:
        print("No devices found.")

    return devices

# Function for port scanning using nmap
def port_scan(target):
    print(f"Scanning ports for target: {target}")
    # Initialize nmap scanner
    nm = nmap.PortScanner()
    # Scan the top 1000 ports
    scan_result = nm.scan(hosts=target, arguments='-Pn -sS -T4 -p 1-1024')

    # Display scan results
    for host in nm.all_hosts():
        print(f"\nHost: {host} ({nm[host].hostname()})")
        print(f"State: {nm[host].state()}")
        for protocol in nm[host].all_protocols():
            print(f"\nProtocol: {protocol}")
            ports = nm[host][protocol].keys()
            for port in ports:
                port_info = nm[host][protocol][port]
                print(f"Port: {port}, State: {port_info['state']}, Service: {port_info.get('name', 'unknown')}")

# Example usage:
# Replace with your network CIDR or target IP
network_cidr = "192.168.1.0/24"  # Replace with your network range
target_ip = "192.168.1.1"  # Replace with your desired target IP

# Run ARP scan to identify devices
devices = arp_scan(network_cidr)

# Run port scan on the first device found (if any)
if devices:
    port_scan(devices[0]['IP'])
