#!/usr/bin/python3

#Script : OpsChallenge02.py
#Purpose: Create an uptime sensor tool that uses ICMP packets to evaluate if hosts on the LAN are up or down
#Why    : Good to practice how to use timestamps and kernel resources in conjuction with flow controls as 'while'

# Import libraries
import subprocess
import datetime
import time

# Function name: print_timestamp
# Purpose      : prints a timestamp to the terminal
# Arguments    : str, ip
# Return       : none
def print_timestamp(str,ip):
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    if ip is None:
        print(f'{timestamp} {str}')
    else:
        print(f'{timestamp} {str} to {ip}')
    print("")


############################# Stretch Goal #############################   
# Function name: print_timestamp_2_file
# Purpose      : prints a timestamp to a file
# Arguments    : str, ip, file
# Return       : none
def print_timestamp_2_file(str,ip,file):
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    with open(file, "a") as f:
        if ip is None:
            f.write(f'{timestamp} {str}')
        else:
            f.write(f'{timestamp} {str} to {ip}')
        f.write("\n")
#########################################################################

# main
print_timestamp("\nStarting script LAB2_OpsChallenge02.py...",None)

# filename to store the ping's status
filename  = "{}_logs".format(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))

# inputs the user to enter the target IP
target_ip = input("Enter your target IP: ")

# infinite loop
while True:
    # store the output in the variable ping_output
    ping_output = subprocess.run(["ping","-n","1",target_ip], stdout=subprocess.PIPE);

    # status' verification
    if "Received = 1" in ping_output.stdout.decode('utf-8'):
        print_timestamp("Network Active",target_ip)
        #print_timestamp_2_file("Network Active",target_ip,filename)
    else:
        print_timestamp("Network Inactive",target_ip)
        #print_timestamp_2_file("Network Active",target_ip,filename)    
    
    # pings every 2 seconds
    time.sleep(2)
    
