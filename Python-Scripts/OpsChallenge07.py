#!/usr/bin/python3

# Script : OpsChallenge07.py
# Purpose: Prompts the user to select if he/she want to encrpt/decrypt a file/string/folder
# Why    : It is important to understand how to encrypt/decrypt data at rest

from cryptography.fernet import Fernet
import os
import tarfile
import datetime
from tqdm import tqdm

### funtions
# Function name: write_key
# Purpose      : Generates a key that will be used to encrypt and decrypt and save it to a file. Symmetric cryptography.
# Arguments    : none
# Return       : none
def write_key():
    key = Fernet.generate_key()
    with open("key","wb") as key_file:
        key_file.write(key)

# Function name: load_key
# Purpose      : Loads the key saved in a file
# Arguments    : none
# Return       : The key read from the file
def load_key():
    return open("key","rb").read()

# Function name: encrypt_file
# Purpose      : Encrypts a file
# Arguments    : file_path, fernet
# Return       : none
def encrypt_file(file_path, fernet):
    if os.path.exists(file_path):
        with open(file_path, 'rb') as file:
            plaintext = file.read()

        ciphertext = fernet.encrypt(plaintext)

        with open(file_path, 'wb') as encrypted_file:
            encrypted_file.write(ciphertext)
            if want_to_compress(encrypted_file):
                timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H:%M:%S.%f')
                compress(f"compressed_{timestamp}.tar.gz",[file_path])
                os.system(f"rm {file_path}")
    else:
        print(f"The file {file_path} does not exists")

# Function name: decrypt_file
# Purpose      : Decrypts a file
# Arguments    : file_path, fernet
# Return       : none
def decrypt_file(file_path, fernet):
    if os.path.exists(file_path):
        with open(file_path, 'rb') as file:
            ciphertext = file.read()

        plaintext = fernet.decrypt(ciphertext)

        with open(file_path, 'wb') as plaintext_file:
            plaintext_file.write(plaintext)
    else:
        print(f"The file {file_path} does not exists")

# Function name: encrypt_string
# Purpose      : Encrypts a string and print to the standard output the ciphertext
# Arguments    : string, fernet
# Return       : none
def encrypt_string(string,fernet):
    encoded_string   = string.encode()
    encrypted_string = fernet.encrypt(encoded_string).decode()
    print(f"\nCiphertext: {encrypted_string}\n")

# Function name: decrypt_string
# Purpose      : Decrypts a string and print to the standard output the plaintext
# Arguments    : string, fernet
# Return       : none
def decrypt_string(string,fernet):
    decrypted_string = fernet.decrypt(string.encode()).decode()
    print(f"\nPlaintext: {decrypted_string}\n")
    
# Function name: encrypt_decrypt_folder
# Purpose      : Encrypts and decrypts a folder
# Arguments    : folder_path, fernet, value
# Return       : none   
def encrypt_decrypt_folder(folder_path,fernet,value):
    if value == ENCRYPT:
        for (root, dirs, files) in os.walk(folder_path, topdown=True):
            for filename in files:
                file_path = os.path.join(root,filename)

                encrypt_file(file_path,fernet)

    if value == DECRYPT:
        for (root, dirs, files) in os.walk(folder_path, topdown=True):
            for filename in files:
                file_path = os.path.join(root,filename)

                decrypt_file(file_path,fernet)
                
########## Functions from https://www.thepythoncode.com/article/compress-decompress-files-tarfile-python ############
def compress(tar_file, members):
    """
    Adds files ('members') to a tar_file and compress it
    """

    # open file for gzip compressed writing
    tar = tarfile.open(tar_file, mode="w:gz")

    # with progress bar
    # set the progress bar
    progress = tqdm(members)
    for member in progress:
        # add file/folder/link to the tar file (compress)
        tar.add(member)
        # set the progress description of the progress bar
        progress.set_description(f"Compressing {member}")

    # close the file
    tar.close()

# this funtion is not used in this script
def decompress(tar_file, path, members=None):
    """
    Extracts 'tar_file' and puts the 'members' to 'path'
    If members is None, all members on 'tar_file' will be extracted
    """

    tar = tarfile.open(tar_file, mode="r:gz")
    if members is None:
        members = tar.getmembers()

    # with progress bar
    # set the progress bar
    progress = tqdm(members)
    for member in progress:
        tar.extract(member, path=path)
        # set the progress description of the progress bar
        progress.set_description(f"Extracting {member.name}")

    # or use this
    # tar.extractall(members=members, path=path)
    # close the file
    tar.close()
#####################################################################################################################


# main
try:
    key = load_key()
except FileNotFoundError:
    write_key()
    key = load_key()
except:
    print("\n ----- An unexpected error occured during a load key -----\n")

# initialize the Fernet class
fernet = Fernet(key)

while(True):

    print("Mode 1 - Encrypt a file")
    print("Mode 2 - Decrypt a file")
    print("Mode 3 - Encrypt a message")
    print("Mode 4 - Decrypt a message")
    print("Mode 5 - Encrypt a folder")
    print("Mode 6 - Decrypt a folder")
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
        
        case "5":
            folder_plaintext = input("\nEnter the folder to encrypt: ")
            encrypt_decrypt_folder(folder_plaintext,fernet,ENCRYPT)

        case "6":
            folder_ciphertext = input("\nEnter the folder to decrypt: ")
            encrypt_decrypt_folder(folder_ciphertext,fernet,DECRYPT)
        
        case "q":
            break

        case _:
            print("\n ----- You do not entered a correct option. Try again -----\n")
            
            
### REFERENCES
# https://www.geeksforgeeks.org/encrypt-and-decrypt-files-using-python/
# https://www.thepythoncode.com/article/encrypt-decrypt-files-symmetric-python
