#!/usr/bin/python3

# Script : OpsChallenge16.py
# Purpose: 
# Why    : 

import time

def mode1(file):
    print("\n")
    
    with open(file, 'r') as file:
        wordlist = file.read().splitlines()

    for w in wordlist:
        time.sleep(1)  
        print(w)
    

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
