import os
from cryptography.fernet import Fernet

class AlphaWare:
    def __init__(self, key_file='key.key'):
        self.key_file = key_file
        if not os.path.exists(self.key_file):
            self.key = self.generate_key()
            self.save_key()
        else:
            self.key = self.load_key()
        self.cipher = Fernet(self.key)

    def generate_key(self):
        return Fernet.generate_key()

    def save_key(self):
        with open(self.key_file, 'wb') as key_file:
            key_file.write(self.key)

    def load_key(self):
        with open(self.key_file, 'rb') as key_file:
            return key_file.read()

    def encrypt_file(self, file_path):
        if not os.path.exists(file_path):
            raise FileNotFoundError("The file to encrypt does not exist.")
        with open(file_path, 'rb') as file:
            file_data = file.read()
        encrypted_data = self.cipher.encrypt(file_data)
        with open(file_path, 'wb') as file:
            file.write(encrypted_data)
        print(f"File '{file_path}' encrypted successfully.")

    def decrypt_file(self, file_path):
        if not os.path.exists(file_path):
            raise FileNotFoundError("The file to decrypt does not exist.")
        with open(file_path, 'rb') as file:
            encrypted_data = file.read()
        decrypted_data = self.cipher.decrypt(encrypted_data)
        with open(file_path, 'wb') as file:
            file.write(decrypted_data)
        print(f"File '{file_path}' decrypted successfully.")

def main():
    alphaware = AlphaWare()
    print("AlphaWare - Secure Your Sensitive Information")
    choice = input("Would you like to (E)ncrypt or (D)ecrypt a file? ").strip().upper()
    file_path = input("Enter the full path of the file: ").strip()

    if choice == 'E':
        alphaware.encrypt_file(file_path)
    elif choice == 'D':
        alphaware.decrypt_file(file_path)
    else:
        print("Invalid option selected. Please choose 'E' for encrypt or 'D' for decrypt.")

if __name__ == "__main__":
    main()