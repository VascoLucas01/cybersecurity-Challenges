#!/usr/bin/python3

# Script : OpsChallenge16.py
# Purpose: Perform a dictionary iterator or Password Recognized
# Why    : "To properly defend against the techniques used by modern threat actors, we need to have an idea of the tools they will be using against us in an effort to circumvent our defenses"

import time

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
    



while(True):
    user_input = input("\n\n---> Select one of the modes (1,2, or q):\n\nMode 1: Offensive; Dictionary Iterator\nMode 2: Defensive; Password Recognized\nMode q: Quit\n\n>")
    
    match(user_input):
        case "1":
            wordlist = input("\nEnter the path to the wordlist:\n\n>")
            mode1(wordlist)
        case "2":
            string = input("\nEnter a string:\n\n>")
            wordlist = input("\nEnter the path to the wordlist:\n\n>")
            mode2(string,wordlist)
        case "q":
            print("\nQuitting...")
            break
        case _:
            print("\n ----- You do not entered a correct option. Try again -----\n")
