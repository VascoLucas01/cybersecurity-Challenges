#!/usr/bin/python3

import os
import hashlib
import time
from dotenv import load_dotenv
#from virustotalsearch import VT_Request


# Script : OpsChallenge33.py
# Purpose: Successfully connect to the VirusTotal API
# ######## Automatically compare your target file’s md5 hash with the hash values of entries on VirusTotal API;
# ######## Print to the screen the number of positives detected and total files scanned; 
# Why    :

# Function to recursively scan files and folders in the directory
def scan_directory(api_key,directory,processed_files):


    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)

            # Skip the file if it has already been processed
            if file_path in processed_files:
                continue

            # Add the file path to the set of processed files
            processed_files.add(file_path)

            # Generate MD5 hash of the file
            md5_hash = generate_md5_hash(file_path)

            print("           VIRUS TOTAL")
            print("---------------------------------------------")
            query = "python3 virustotalsearch.py -k " + str(api_key) + " -m " + str(md5_hash)
            os.system(query)
            print("---------------------------------------------")

            #VT_Request(api_key,md5_hash,file_path)

            # Get current timestamp
            timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

            # Print file information
            print(f"Timestamp: {timestamp}")
            print(f"File Name: {file}")
            print(f"File Size: {file_size} bytes")
            print(f"File Path: {file_path}")
            print(f"MD5 Hash: {md5_hash}")
            print("---------------------------------------------")

        for subdir in dirs:
            subdir_path = os.path.join(root, subdir)
            scan_directory(api_key,subdir_path,processed_files)





# Function to generate MD5 hash of a file
def generate_md5_hash(file_path):
    md5_hash = hashlib.md5()
    with open(file_path, "rb") as file:
        for chunk in iter(lambda: file.read(1024), b""):
            md5_hash.update(chunk)
    return md5_hash.hexdigest()

def main():

    load_dotenv()

    api_key = os.getenv('APIKEY')
    directory_to_scan = input("Enter the directory path to scan:\n\t> ")
    print("---------------------------------------------")
    print("           SCAN RESULTS")
    print("---------------------------------------------")
    processed_files = set()
    scan_directory(api_key,directory_to_scan,processed_files)


if __name__ == "__main__":
    main()
