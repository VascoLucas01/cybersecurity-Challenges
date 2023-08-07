#!/usr/bin/python3

# Script : Automated_Brute_Force_Wordlist_Attack_Tool_Part_1_of_3.py
# Purpose: Create of a script that prompts the user to select one of the following modes:
########## Mode 1: Offensive; Dictionary Iterator
########## Mode 2: Defensive; Password Recognized
# Why    : "To properly defend against the techniques used by modern threat actors, we need to have an idea of the tools they will be using against us in an effort to circumvent our defenses"

import time

### funtions
# Function name: print_words_from_file
# Purpose      : Opens a file with one word at each line and displays those words at 1 second intervals
# Arguments    : file
# Return       : none
def print_words_from_file(file):
    print("\n")
    
    with open(file, 'r') as file:
        wordlist = file.read().splitlines()

    for w in wordlist:
        time.sleep(1)  
        print(w)
  

# Function name: search_str
# Purpose      : Verifies if the string passed as an argument is in the wordlist passed as another argument
# Arguments    : string, wordlist
# Return       : none
def search_str(string,wordlist):
    if(string in wordlist):
        print(f"\nThe string \"{string}\" was found!")
    else:
        print(f"\nThe string \"{string}\" was not found!")
    



while(True):
    user_input = input("\n\n---> Select one of the modes (1,2, or q):\n\nMode 1: Offensive; Dictionary Iterator\nMode 2: Defensive; Password Recognized\nMode q: Quit\n\n>")
    
    match(user_input):
        case "1":
            wordlist = input("\nEnter the path to the wordlist:\n\n>")
            print_words_from_file(wordlist)
        case "2":
            string = input("\nEnter a string:\n\n>")
            wordlist = input("\nEnter the path to the wordlist:\n\n>")
            search_str(string,wordlist)
        case "q":
            print("\nQuitting...")
            break
        case _:
            print("\n ----- You do not entered a correct option. Try again -----\n")
