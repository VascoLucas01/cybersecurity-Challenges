#!/usr/bin/python3

# Script : OpsChallenge06.py
# Purpose: 
# Why    : 

from cryptography.fernet import Fernet
import os

# funtions
def write_key():

    key = Fernet.generate_key()
    with open("key","wb") as key_file:
        key_file.write(key)

def load_key():
    return open("key","rb").read()

def encrypt_file(file_path, fernet):
    if os.path.exists(file_path):
        with open(file_path, 'rb') as file:
            plaintext = file.read()

        ciphertext = fernet.encrypt(plaintext)

        with open(file_path, 'wb') as encrypted_file:
            encrypted_file.write(ciphertext)

        # os.system(f"rm {file_path}")
    else:
        print(f"The file {file_path} does not exists")

def decrypt_file(file_path, fernet):
    if os.path.exists(file_path):
        with open(file_path, 'rb') as file:
            ciphertext = file.read()

        plaintext = fernet.decrypt(ciphertext)

        with open(file_path, 'wb') as plaintext_file:
            plaintext_file.write(plaintext)
    else:
        print(f"The file {file_path} does not exists")

def encrypt_string(string,fernet):
    encoded_string   = string.encode()
    encrypted_string = fernet.encrypt(encoded_string).decode()
    print(f"\nCiphertext: {encrypted_string}\n")

def decrypt_string(string,fernet):
    decrypted_string = fernet.decrypt(string.encode()).decode()
    print(f"\nPlaintext: {decrypted_string}\n")

    # main
try:
    key = load_key()
except FileNotFoundError:
    write_key()
    key = load_key()
except:
    print("\n ----- An unexpected error occured during a load key -----\n")

fernet = Fernet(key)

while(True):

    print("Mode 1 - Encrypt a file")
    print("Mode 2 - Decrypt a file")
    print("Mode 3 - Encrypt a message")
    print("Mode 4 - Decrypt a message")
    print("Enter 'q' to quit\n")
    user_input = input("Enter one of the modes listed above: (1,2,3, or 4)\n\n>")

    match(user_input):

        case "1":
            file_path  = input("\nFile Path: ")
            print("")
            encrypt_file(file_path,fernet)

        case "2":
            file_path  = input("\nFile Path: ")
            print("")
            try:
                decrypt_file(file_path,fernet)
            except:
                print(f"\n ----- Check the file {file_path}. It is probably already decrypted. -----\n")

        case "3":
            plaintext  = input("\nEnter a plaintext string: ")
            print("")
            encrypt_string(plaintext,fernet)

        case "4":
            ciphertext = input("\nEnter a ciphertext string: ")
            print("")
            decrypt_string(ciphertext,fernet)

        case "q":
            break

        case _:
            print("\n ----- You do not entered a correct option. Try again -----\n")
            
            
### REFERENCES
# https://www.geeksforgeeks.org/encrypt-and-decrypt-files-using-python/
# https://www.thepythoncode.com/article/encrypt-decrypt-files-symmetric-python
