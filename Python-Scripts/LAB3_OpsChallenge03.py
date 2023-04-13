#!/usr/bin/python3

#Script : LAB3_OpsChallenge03.py
#Purpose: 
#Why    : 

# import libraries
import os

# variables

# in order to hide my username and password from public repositories, it was created two environment variables
username = ""
password = os.environ.get('PASSWORD')




# main
print(password)