# Install necessary libraries
!pip install pycryptodome bcrypt

from Crypto.Cipher import AES
import bcrypt
import os

# ------------------ Encryption & Decryption (AES) ------------------
def encrypt_data(data, key):
    """Encrypts data using AES encryption."""
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(data.encode('utf-8'))
    return nonce, ciphertext

def decrypt_data(nonce, ciphertext, key):
    """Decrypts data using AES decryption."""
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext).decode('utf-8')
    return plaintext

# Example encryption usage
key = b"thisisaverysecret"[:16]  # Ensure the key is exactly 16 bytes
data = "Confidential Information"
nonce, ciphertext = encrypt_data(data, key)
decrypted_data = decrypt_data(nonce, ciphertext, key)

print(f"Original Data: {data}")
print(f"Encrypted Data (Hex): {ciphertext.hex()}")
print(f"Decrypted Data: {decrypted_data}")

# ------------------ Password Hashing (bcrypt) ------------------
def hash_password(password):
    """Hashes a password using bcrypt."""
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password

def verify_password(password, hashed_password):
    """Verifies a password against its hashed version."""
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)

# Example password hashing usage
password = "securepassword123"
hashed_password = hash_password(password)

print(f"\nOriginal Password: {password}")
print(f"Hashed Password: {hashed_password}")

# Verifying password
if verify_password(password, hashed_password):
    print("Password verification successful!")
else:
    print("Password verification failed!")

# ------------------ Access Control Simulation (Role-Based) ------------------
# Example roles and policies
roles = {
    "admin": ["read", "write", "delete"],
    "user": ["read"],
    "guest": []
}

def check_access(role, action):
    """Checks if a role has permission for a specific action."""
    if action in roles.get(role, []):
        print(f"Access granted for {role} to perform '{action}'.")
    else:
        print(f"Access denied for {role} to perform '{action}'.")

# Example access control checks
print("\nAccess Control Simulation:")
check_access("admin", "write")  # Expected: Access granted
check_access("user", "delete")  # Expected: Access denied
check_access("guest", "read")   # Expected: Access denied
