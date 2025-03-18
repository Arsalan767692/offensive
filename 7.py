import os
import socket
import subprocess
import platform
import shutil

# Function to gather system information
def gather_system_info():
    print("Gathering system information...\n")
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    os_info = platform.platform()

    # Try to retrieve the current user, with a fallback
    try:
        user = os.getlogin()  # This works in typical environments
    except OSError:
        user = os.environ.get('USER') or os.environ.get('USERNAME')  # Fallback for non-terminal environments

    print(f"Hostname: {hostname}")
    print(f"IP Address: {ip_address}")
    print(f"Operating System: {os_info}")
    print(f"User: {user}")

# Function to list running processes
def list_processes():
    print("\nListing running processes...\n")
    try:
        output = subprocess.getoutput("ps aux")
        print(output)
    except Exception as e:
        print(f"Error listing processes: {e}")

# Function to create persistence by adding a startup script (simulation)
def simulate_persistence():
    print("\nSimulating persistence by copying a file to a 'startup' folder (for demonstration only)...\n")
    payload_file = "reverse_shell.py"
    startup_folder = "/tmp/startup"  # Simulated startup directory for demonstration

    # Create the simulated startup directory
    if not os.path.exists(startup_folder):
        os.makedirs(startup_folder)

    # Simulate copying the payload to the startup directory
    shutil.copy(payload_file, os.path.join(startup_folder, payload_file))
    print(f"Copied {payload_file} to {startup_folder}")

# Function to simulate privilege escalation (dummy command)
def simulate_privilege_escalation():
    print("\nSimulating privilege escalation...\n")
    try:
        # Simulate privilege escalation using a dummy sudo command
        output = subprocess.getoutput("sudo -n ls /root")
        print(output)
    except Exception as e:
        print(f"Error simulating privilege escalation: {e}")

# Example usage of post-exploitation functions
gather_system_info()
list_processes()
simulate_persistence()
simulate_privilege_escalation()
