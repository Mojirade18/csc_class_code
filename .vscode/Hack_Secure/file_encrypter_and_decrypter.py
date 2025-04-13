from cryptography.fernet import Fernet

# Function to generate a new secret key
def generate_key():
    return Fernet.generate_key()

# Function to encrypt a text file
def encrypt_file(file_path, key, output_path):
    # Read the file content
    with open(file_path, 'rb') as file:
        file_data = file.read()

    # Encrypt the file data
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(file_data)

    # Save the encrypted data to a new file
    with open(output_path, 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)

    print(f"File encrypted and saved as {output_path}")

# Function to decrypt a text file
def decrypt_file(file_path, key, output_path):
    # Read the encrypted file content
    with open(file_path, 'rb') as file:
        encrypted_data = file.read()

    # Decrypt the data
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data)

    # Save the decrypted data to a new file
    with open(output_path, 'wb') as decrypted_file:
        decrypted_file.write(decrypted_data)

    print(f"File decrypted and saved as {output_path}")

# Main function to provide the menu and handle user input
def main():
    print("Welcome to the file encryption/decryption program!")

    # Option to generate a new key
    key_choice = input("Do you have a secret key? (y/n): ")
    if key_choice.lower() == 'n':
        key = generate_key()
        print(f"New secret key generated: {key.decode()}")
    else:
        key = input("Enter your secret key: ").encode()

    # Provide options for encryption and decryption
    action = input("Do you want to (e)ncrypt or (d)ecrypt a file? ")

    if action.lower() == 'e':
        file_path = input("Enter the path of the text file to encrypt: ")
        output_path = input("Enter the path to save the encrypted file: ")
        encrypt_file(file_path, key, output_path)
    elif action.lower() == 'd':
        file_path = input("Enter the path of the encrypted file to decrypt: ")
        output_path = input("Enter the path to save the decrypted file: ")
        decrypt_file(file_path, key, output_path)
    else:
        print("Invalid option. Please choose 'e' to encrypt or 'd' to decrypt.")

# Run the main program
if __name__ == "__main__":
    main()
