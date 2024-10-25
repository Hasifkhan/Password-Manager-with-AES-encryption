#!/usr/bin/env python3

from cryptography.fernet import Fernet
import os
import pyfiglet
from termcolor import colored


# Function to display name in style
def display_styled_name():
    ascii_banner = pyfiglet.figlet_format("Password Manager with AES Encryption")  # Replace "YOUR NAME" with your actual name
    colored_banner = colored(ascii_banner, 'green')  # You can change the color
    print(colored_banner)

# Main execution
if __name__ == "__main__":
    # Display your name in a styled format
    display_styled_name()


# Generate key for encryption
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

# Load the previously generated key
def load_key():
    return open("secret.key", "rb").read()

# Encrypt the password
def encrypt_password(password):
    key = load_key()
    fernet = Fernet(key)
    encrypted_password = fernet.encrypt(password.encode())
    return encrypted_password

# Decrypt the password
def decrypt_password(encrypted_password):
    key = load_key()
    fernet = Fernet(key)
    decrypted_password = fernet.decrypt(encrypted_password).decode()
    return decrypted_password

# Store password in a file
def store_password(service, encrypted_password):
    with open("passwords.txt", "a") as file:
        file.write(f"{service}:{encrypted_password.decode()}\n")

# Retrieve password from file
def retrieve_password(service):
    with open("passwords.txt", "r") as file:
        for line in file:
            stored_service, stored_password = line.split(":")
            if stored_service == service:
                return decrypt_password(stored_password.strip().encode())
    return None

# Main function
def main():
    if not os.path.exists("secret.key"):
        generate_key()
    
    print("Password Manager")
    while True:
        choice = input("1. Store password\n2. Retrieve password\n3. Quit\nChoose an option: ")

        if choice == "1":
            service = input("Enter the service name: ")
            password = input("Enter the password: ")
            encrypted_password = encrypt_password(password)
            store_password(service, encrypted_password)
            print(f"Password for {service} stored securely.")
        
        elif choice == "2":
            service = input("Enter the service name: ")
            password = retrieve_password(service)
            if password:
                print(f"Password for {service}: {password}")
            else:
                print("Service not found.")
        
        elif choice == "3":
            break

        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
