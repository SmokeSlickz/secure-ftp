This is a secure encrypted FTP system, that encrypts the data and sends it to the client.

This program contains:
1. Sample Files
   i.   secret.key - Shared Key Generated By Server
   ii.  received_file.enc - Encrypted File recieved
   iii. decrypted_file.txt - Which is the decrypted file recieved.
   iv.  data.txt - Sample Data
2. client.py - Client Python Executable
3. server.py - Server Python Executable
4. decrypt.py - Data Decryption Tool


How to use:
1. Run the server.py. (Key Generated to be sent to client.)
2. Edit client.py path of file to be sent.
3. Run client.py.
4. Root direcory recieves the encrypted file.
5. use the decrypt.py tool to decrypt the encrypted message.
