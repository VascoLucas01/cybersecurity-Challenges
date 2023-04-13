#!/usr/bin/python3

#Script : LAB3_OpsChallenge03.py
#Purpose: 
#Why    : 

# import libraries
import os
import subprocess
import datetime
import time
import smtplib
import ssl
from email.message import EmailMessage

# Function name: send an email
# Purpose      : notify the administrator everytime the host status change
# Arguments    : email_sender, email_password, host, status
# Return       : none
def sendEmail(email_sender,email_password,host,status):
    # in order to hide my username and password from public repositories, it was created two environment variables
    # email_sender   = 'cyberpractitioner00@gmail.com'
    # email_password = os.environ.get('PASSWORD')
    timestamp        = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    email_receiver   = 'cyberpractitioner00@gmail.com'

    subject = f'[REPORT] Target IP: {host}'
    
    if "UP" == status:
        body = f'[Date and Time: {timestamp}]\n\nStatus of {host} change from DOWN to UP'
    else:
        body = f'[Date and Time: {timestamp}]\n\nStatus of {host} change from UP to DOWN'

    em            = EmailMessage()
    em['From']    = email_sender
    em['To']      = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())



# main
timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
print("\nStarting script LAB3_OpsChallenge03.py...\n")

# inputs the user to enter the email sender, email password and target IP
email_sender    = input("\nEnter an email to use as necessary: ")
email_password  = input("\nEnter the password: ")
target_ip       = input("Enter your target IP: ")


last_state = "None"

# infinite loop
while True:
    # store the output in the variable ping_output
    ping_output = subprocess.run(["ping","-n","1",target_ip], stdout=subprocess.PIPE);

    # status' verification
    if "Received = 1" in ping_output.stdout.decode('utf-8'):
        if last_state == None:
            last_state = "UP"
        if last_state == "DOWN":
            sendEmail(email_sender,email_password,target_ip,"UP")
            last_state = "UP"

    else:
        if last_state == None:
            last_state = "DOWN"        
        if last_state == "UP":
            sendEmail(email_sender,email_password,target_ip,"DOWN")
            last_state = "DOWN"
    
    # pings every 2 seconds
    time.sleep(2)