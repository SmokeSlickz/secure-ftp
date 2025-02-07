# Imports
import socket
from cryptography.fernet import Fernet

# Encryption Key Generator (Symetric Fernet Encryption)
key = Fernet.generate_key()
cipher = Fernet(key)

# Save Key
with open('secret.key', 'wb') as key_file:
    key_file.write(key)

# Main Function (Server Instance)
def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 65432))
    server_socket.listen(1)
    print("Server is listening...")

    conn, addr = server_socket.accept()
    print(f"Connection from {addr} established.")

    with open('received_file.enc', 'wb') as f:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            f.write(data)

    print("File received and saved as 'received_file.enc'.")
    conn.close()

# Main Thread
if __name__ == "__main__":
    start_server()