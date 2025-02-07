# Imports
from cryptography.fernet import Fernet

# Load key (Generated by Server)
with open('secret.key', 'rb') as key_file:
    key = key_file.read()

cipher = Fernet(key)

# Main Function - Decrypt
def decrypt_file(encrypted_file_path, decrypted_file_path):
    with open(encrypted_file_path, 'rb') as f:
        encrypted_data = f.read()
    
    decrypted_data = cipher.decrypt(encrypted_data)
    
    with open(decrypted_file_path, 'wb') as f:
        f.write(decrypted_data)

    print(f"File '{encrypted_file_path}' decrypted and saved as '{decrypted_file_path}'.")

# Main Thread
if __name__ == "__main__":
    encrypted_file = 'received_file.enc'  # Specify the encrypted file to decrypt
    decrypted_file = 'decrypted_file.txt'  # Specify the output file name
    decrypt_file(encrypted_file, decrypted_file)