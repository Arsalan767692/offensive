# Install necessary libraries
!pip install scapy

# Import required libraries
import socket
from scapy.all import ARP, Ether, srp

# Function to simulate scanning the wireless network
def scan_network(network_cidr="192.168.1.0/24"):
    print(f"Scanning the wireless network: {network_cidr}...")
    arp = ARP(pdst=network_cidr)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp

    # Send packet and receive responses
    result = srp(packet, timeout=3, verbose=0)[0]

    # Parse results
    devices = []
    for sent, received in result:
        devices.append({'IP': received.psrc, 'MAC': received.hwsrc})

    print("\nDevices detected on the network:")
    for device in devices:
        print(f"IP: {device['IP']}, MAC: {device['MAC']}")

# Function to check open ports on a target device
def check_open_ports(target_ip):
    print(f"\nChecking open ports for target: {target_ip}...")
    common_ports = [21, 22, 23, 80, 443, 8080]  # Common ports to check
    open_ports = []

    for port in common_ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Set a timeout of 1 second
        result = sock.connect_ex((target_ip, port))  # 0 means port is open
        if result == 0:
            open_ports.append(port)
        sock.close()

    if open_ports:
        print(f"Open ports detected on {target_ip}: {open_ports}")
    else:
        print(f"No open ports detected on {target_ip}.")

# Example usage
network_cidr = "192.168.1.0/24"  # Replace with your network range
target_ip = "192.168.1.1"  # Replace with the IP of a detected device

# Scan the wireless network
scan_network(network_cidr)

# Check open ports on the target device
check_open_ports(target_ip)
