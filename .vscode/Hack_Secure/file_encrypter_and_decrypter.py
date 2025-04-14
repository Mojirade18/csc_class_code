from cryptography.fernet import Fernet

# Function to generate a new secret key
def generate_key():
    return Fernet.generate_key()

# Function to encrypt a text file
def encrypt_file(file_path, key, output_path):
    try:
        with open(file_path, 'rb') as file:
            file_data = file.read()

        fernet = Fernet(key)
        encrypted_data = fernet.encrypt(file_data)

        with open(output_path, 'wb') as encrypted_file:
            encrypted_file.write(encrypted_data)

        print(f"\n File encrypted and saved as: {output_path}")
    except Exception as e:
        print(f"\n Error during encryption: {e}")

# Function to decrypt a text file
def decrypt_file(file_path, key, output_path):
    try:
        with open(file_path, 'rb') as file:
            encrypted_data = file.read()

        fernet = Fernet(key)
        decrypted_data = fernet.decrypt(encrypted_data)

        with open(output_path, 'wb') as decrypted_file:
            decrypted_file.write(decrypted_data)

        print(f"\n✅ File decrypted and saved as: {output_path}")
    except Exception as e:
        print(f"\n❌ Error during decryption: {e}")

# Main function
def main():
    print("🔐 Welcome to the File Encryption/Decryption Program!")

    while True:
        # Option to generate or enter a key
        key_choice = input("\nDo you have a secret key? (y/n): ").lower()
        while key_choice not in ['y', 'n']:
            key_choice = input("Please enter 'y' or 'n': ").lower()

        if key_choice == 'n':
            key = generate_key()
            print(f"\n🔑 New secret key generated (save this!):\n{key.decode()}")
        else:
            key = input("Enter your secret key: ").encode()

        # Choose action
        action = input("\nWhat would you like to do?\n(e) Encrypt a file\n(d) Decrypt a file\nChoice: ").lower()
        while action not in ['e', 'd']:
            action = input("Please enter 'e' or 'd': ").lower()

        if action == 'e':
            file_path = input("Enter the path of the text file to encrypt: ")
            output_path = input("Enter the path to save the encrypted file (e.g. encrypted.txt): ")
            encrypt_file(file_path, key, output_path)

        elif action == 'd':
            file_path = input("Enter the path of the encrypted file to decrypt: ")
            output_path = input("Enter the path to save the decrypted file (e.g. decrypted.txt): ")
            decrypt_file(file_path, key, output_path)

        # Ask if the user wants to continue
        again = input("\nDo you want to perform another operation? (y/n): ").lower()
        while again not in ['y', 'n']:
            again = input("Please enter 'y' for yes or 'n' for no: ").lower()

        if again == 'n':
            print("\n👋 Goodbye! Stay secure!")
            break

# Run the program
if __name__ == "__main__":
    main()
