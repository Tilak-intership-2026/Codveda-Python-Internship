# project name file encryptor for file encryption
#devloper: tilak kumar
#project source :task 2 from level 3 advanced
#provider:code veda

from cryptography.fernet import Fernet
import os
def generate_key():
    """Generates a key and saves it into a file."""
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print(" Key generated and saved as 'secret.key'")


def load_key():
    """Loads the key from the current directory named 'secret.key'."""
    return open("secret.key", "rb").read()


def encrypt_file(filename):
    """Encrypts any file using the generated key."""
    key = load_key()
    f = Fernet(key)

    # Split filename to handle extensions correctly
    name, ext = os.path.splitext(filename)
    encrypted_filename = f"{name}_encrypted{ext}"

    with open(filename, "rb") as file:
        file_data = file.read()

    encrypted_data = f.encrypt(file_data)

    with open(encrypted_filename, "wb") as file:
        file.write(encrypted_data)

    print(f" File '{filename}' has been encrypted to '{encrypted_filename}'")


def decrypt_file(filename):
    """Decrypts a file using the generated key."""
    key = load_key()
    f = Fernet(key)

    # Check if it's an encrypted file based on naming convention
    if "_encrypted" not in filename:
        print(" Warning: This file doesn't look like an encrypted file.")
        confirm = input("Do you still want to try? (y/n): ").lower()
        if confirm != 'y':
            return

    with open(filename, "rb") as file:
        encrypted_data = file.read()

    try:
        decrypted_data = f.decrypt(encrypted_data)

        # Restore original name by removing '_encrypted'
        original_name = filename.replace("_encrypted", "")

        with open(original_name, "wb") as file:
            file.write(decrypted_data)

        print(f" File '{filename}' has been decrypted to '{original_name}'")
    except Exception as e:
        print(f" Decryption failed: {e}")
        print("Tip: Ensure you are using the correct 'secret.key' file.")


def main():
    print("--- Codveda Level 3: File Encryption/Decryption ---")

    if not os.path.exists("secret.key"):
        generate_key()

    print("\n1. Encrypt a file")
    print("2. Decrypt a file")

    choice = input("Select an option (1/2): ")
    filename = input("Enter the filename (e.g., photo.jpg or doc.pdf): ").strip()

    if not filename:
        print(" No filename provided.")
        return

    if choice == '1':
        if os.path.exists(filename):
            encrypt_file(filename)
        else:
            print(f" Error: File '{filename}' not found in the current directory.")
    elif choice == '2':
        if os.path.exists(filename):
            decrypt_file(filename)
        else:
            print(f" Error: File '{filename}' not found in the current directory.")
    else:
        print("Invalid choice. Please select 1 or 2.")


if __name__ == "__main__":
    main()