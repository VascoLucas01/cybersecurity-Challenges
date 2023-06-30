#!/usr/bin/python3

import os
import hashlib
import time

# Function to recursively scan files and folders in the directory
def scan_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)

            # Generate MD5 hash of the file
            md5_hash = generate_md5_hash(file_path)

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
            scan_directory(subdir_path)

# Function to generate MD5 hash of a file
def generate_md5_hash(file_path):
    md5_hash = hashlib.md5()
    with open(file_path, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            md5_hash.update(chunk)
    return md5_hash.hexdigest()

def main():
    directory_to_scan = input("Enter the directory path to scan:\n\t> ")
    print("---------------------------------------------")
    print("           SCAN RESULTS")
    print("---------------------------------------------")
    scan_directory(directory_to_scan)

if __name__ == "__main__":
    main()
