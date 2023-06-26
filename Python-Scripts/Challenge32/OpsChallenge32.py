#!/usr/bin/python3

import os

# Script : OpsChallenge32.py
# Purpose: Prompt the user to type in a file name to search for; 
# ######## Prompt the user for a directory to search in; 
# ######## Search each file in the directory by name; 
# ######## For each positive detection, print to the screen the file name and location; 
# ######## At the end of the search process, print to the screen how many files were searched and how many hits were found
# Why    :

# Function to search for a file in a directory
def search_files(directory, filename):
    hits           = 0
    searched_files = 0

    for root, _, files in os.walk(directory):
        for file in files:
            if file == filename:
                hits += 1
                print(f"\nFound: {os.path.join(root, file)}")
            searched_files += 1
    return searched_files, hits


def main():
    filename_to_search  = input("Enter the filename to search for:\n\t> ")
    directory_to_search = input("\nEnter the directory to search for:\n\t> ")

    # Execute different commands based on the operating system
    if os.name == "posix":  # Linux
        searched_files, hits = search_files(directory_to_search, filename_to_search)
    elif os.name == "nt":  # Windows
        directory_to_search  = directory_to_search.replace("/", "\\")
        searched_files, hits = search_files(directory_to_search, filename_to_search)
    else:
        print("Unsupported operating system.")
    searched_files, hits = 0, 0


    print("\n---------------------------------------------")
    print("                STATISTICS")
    print("---------------------------------------------")
    print("     SEARCHED FILES       |       HITS")
    print(f"            {searched_files}             |         {hits}")
if __name__ == "__main__":
    main()
