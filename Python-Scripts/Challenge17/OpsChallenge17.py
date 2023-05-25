#!/usr/bin/python3

# Script : OpsChallenge16.py
# Purpose: 
# Why    : 

import time
import paramiko

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

    
def main(): 

    while(True):
        
        user_input = input("\n\n---> Select one of the modes (1,2,3 or q):\n\nMode 1: Offensive; Dictionary Iterator\nMode 2: Defensive; Password Recognized\nMode 3: Authenticate to an SSH server by its IP address\nMode q: Quit\n\n>")
        
        match(user_input):
            case "1":
                wordlist = input("\nEnter the path to the wordlist:\n\n>")
                mode1(wordlist)
            case "2":
                string = input("\nEnter a string:\n\n>")
                wordlist = input("\nEnter the path to the wordlist:\n\n>")
                mode2(string,wordlist)
            case "3":
                mode3(HOSTNAME, USERNAME, PASSWORD, PORT)
            case "q":
                print("\nQuitting...")
                break
            case _:
                print("\n ----- You do not entered a correct option. Try again -----\n")
            
if __name__ == "__main__":
    main()
