# Encryption Methods
# caesar - Shifts Letter With Same Number
def caesar_encrypt(plaintext, shift):
    encrypted = ""
    for char in plaintext:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted += char
    return encrypted

def caesar_decrypt(ciphertext, shift):
    return caesar_encrypt(ciphertext, -shift)


# vigenere - - Shifts Letter With Numeric Value of Keyword Charachters for each letter
def vigenere_encrypt(plaintext, keyword):
    encrypted = ""
    keyword_repeated = (keyword * (len(plaintext) // len(keyword) + 1))[:len(plaintext)]
    
    for p_char, k_char in zip(plaintext, keyword_repeated):
        if p_char.isalpha():
            shift_base = ord('A') if p_char.isupper() else ord('a')
            shift = ord(k_char.lower()) - ord('a')
            encrypted += chr((ord(p_char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted += p_char
    return encrypted

def vigenere_decrypt(ciphertext, keyword):
    decrypted = ""
    keyword_repeated = (keyword * (len(ciphertext) // len(keyword) + 1))[:len(ciphertext)]
    
    for c_char, k_char in zip(ciphertext, keyword_repeated):
        if c_char.isalpha():
            shift_base = ord('A') if c_char.isupper() else ord('a')
            shift = ord(k_char.lower()) - ord('a')
            decrypted += chr((ord(c_char) - shift_base - shift) % 26 + shift_base)
        else:
            decrypted += c_char
    return decrypted

# Main Function
def main():
    print("Simple Encryption/Decryption Tool")
    print("1. Caesar Cipher")
    print("2. Vigenère Cipher")
    choice = input("Choose an option (1 or 2): ")

    if choice == '1':
        action = input("Do you want to (e)ncrypt or (d)ecrypt? ")
        message = input("Enter your message: ")
        shift = int(input("Enter shift value (1-25): "))

        if action.lower() == 'e':
            result = caesar_encrypt(message, shift)
            print("Encrypted message:", result)
        elif action.lower() == 'd':
            result = caesar_decrypt(message, shift)
            print("Decrypted message:", result)
        else:
            print("Invalid action.")

    elif choice == '2':
        action = input("Do you want to (e)ncrypt or (d)ecrypt? ")
        message = input("Enter your message: ")
        keyword = input("Enter the keyword: ")

        if action.lower() == 'e':
            result = vigenere_encrypt(message, keyword)
            print("Encrypted message:", result)
        elif action.lower() == 'd':
            result = vigenere_decrypt(message, keyword)
            print("Decrypted message:", result)
        else:
            print("Invalid action.")
    else:
        print("Invalid choice.")

# Main Thread
run = True
if __name__ == "__main__":
    while run:
        main()
        cont = input("Enter 'exit' To terminate the program:")
        if cont == "exit":
            run = False
    print("Have A Good Day!")