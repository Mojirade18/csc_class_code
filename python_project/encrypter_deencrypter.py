GREETING_MESSAGE = """Encrypt/Decrypt your message using XOR cipher. This is message coder by Moji"""

def xor_encrypt_decrypt(text, key):
    """Encrypt or decrypt text using XOR cipher with the given key."""
    result = ""
    for i in range(len(text)):
        result += chr(ord(text[i]) ^ ord(key[i % len(key)]))
    return result

def get_key_or_default(prompt="Enter a secret key: "):
    """Get key from user or return default if none provided."""
    key = input(prompt)
    if not key:
        key = "default_key"
        print("Using default key since none was provided.")
    return key

def encrypt_message():
    """Handle the encryption process."""
    word = input("Type in the word you want to encrypt: ")
    key = get_key_or_default()
    
    encrypted_value = xor_encrypt_decrypt(word, key)
    
    hex_result = ''.join(f'{ord(c):02x}' for c in encrypted_value)
    print(f"The encrypted message is: {hex_result}")
    print(f"Remember your key: {key}")

def decrypt_message():
    """Handle the decryption process."""
    encrypted_message = input("Enter the encrypted message (in hex): ")
    key = get_key_or_default()
    
    try:
        
        encrypted_chars = ''.join(chr(int(encrypted_message[i:i+2], 16)) 
                                for i in range(0, len(encrypted_message), 2))
        decrypted_message = xor_encrypt_decrypt(encrypted_chars, key)
        print(f"Decrypted message: {decrypted_message}")
    except ValueError:
        print("Invalid encrypted message format. Please enter valid hexadecimal values.")


print(GREETING_MESSAGE)
print("What do you want to do?")
print("1. encrypt your message.")
print("2. De-encrypt your message.")

while True:
    try:
        choice = int(input("What is your choice 1/2: "))
        if choice in [1, 2]:
            break
        else:
            print("Please enter either 1 or 2.")
    except ValueError:
        print("Invalid input. Please enter a number (1 or 2).")

if choice == 1:
    encrypt_message()
elif choice == 2:
    decrypt_message()
else:
    print("Invalid choice. Please select 1 or 2.")