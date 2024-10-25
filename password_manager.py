#!/usr/bin/env python3

from cryptography.fernet import Fernet
import os
import pyfiglet
from termcolor import colored
from tkinter import *


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



root = Tk()
root.title("Password Manager")
root.geometry("400x400")

service_label = Label(root, text="Service Name")
service_label.pack()

service_entry = Entry(root)
service_entry.pack()

password_label = Label(root, text="Password")
password_label.pack()

password_entry = Entry(root)
password_entry.pack()

# Function to store password
def add_password():
    service = service_entry.get()
    password = password_entry.get()
    encrypted_password = encrypt_password(password)
    store_password(service, encrypted_password)
    print(f"Password for {service} stored securely.")


# Retrieve password from file
def retrieve_password() -> None:
    service = service_entry.get()
    print(f"Service: {service}")
    with open("passwords.txt", "r") as file:
        for line in file:
            line = line.strip()  # Remove any extra whitespace or newline characters
            if line:
                parts = line.split(":", 1)
                if len(parts) == 2:  # Ensure both service and password are present
                    stored_service, stored_password = parts
                    if stored_service == service:
                        password = decrypt_password(stored_password.encode())
                        listBox.insert(0, f"{service}: {password}")
                else:
                    print("Skipped malformed line:", line)

    


add_button = Button(root, text="Add Password", command=add_password)
add_button.pack()

list_button = Button(root, text="Show Password", command=retrieve_password)
list_button.pack()

listBox = Listbox(root, width=50, height=20)
listBox.pack(pady=10)

if __name__ == "__main__":
    root.mainloop()
    # main()
