# Imports
import socket
from cryptography.fernet import Fernet

# Load Key (Has to be manually sent From Server to Client)
with open('secret.key', 'rb') as key_file:
    key = key_file.read()

cipher = Fernet(key)

# Functions
# Encrypt
def encrypt_file(file_path):
    with open(file_path, 'rb') as f:
        file_data = f.read()
    encrypted_data = cipher.encrypt(file_data)
    return encrypted_data

# Send
def send_file(file_path):
    encrypted_data = encrypt_file(file_path)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 65432))
    client_socket.sendall(encrypted_data)
    client_socket.close()
    print(f"File '{file_path}' sent successfully.")

# Main Thread
if __name__ == "__main__":
    file_to_send = r'C:\Users\shibi\OneDrive\Documents\projects\Encrypted_FTP\data.txt'  # File
    send_file(file_to_send)