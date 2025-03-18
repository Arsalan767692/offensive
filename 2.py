# Import the necessary module
import nmap

# Initialize the nmap scanner
nm = nmap.PortScanner()

# Function to perform a basic scan
def vulnerability_scan(target):
    print(f"Scanning target: {target}")
    # Perform a scan on the common ports (1-1024)
    scan_result = nm.scan(hosts=target, arguments='-sV -p 1-1024')

    # Display the scan result
    for host in nm.all_hosts():
        print(f"Host: {host} ({nm[host].hostname()})")
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

# Example target (replace with your desired target)
target_ip = 'scanme.nmap.org'  # Replace with your target IP or domain

1# Run the vulnerability scan
vulnerability_scan(target_ip)
