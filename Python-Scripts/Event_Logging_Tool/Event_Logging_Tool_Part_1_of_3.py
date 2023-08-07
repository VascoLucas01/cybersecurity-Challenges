#!/usr/bin/python3

# Script : Event_Logging_Tool_Part_1_of_3.py
# Purpose: Add logging capabilities to OpsChallenge02.py; send log data to a file in the local directory
# Why    :


################################################# Python Tool Chosen #################################################
######################################################################################################################
# Script : OpsChallenge02.py
# Purpose: Create an uptime sensor tool that uses ICMP packets to evaluate if hosts on the LAN are up or down
# Why    : Good to practice how to use timestamps and kernel resources in conjuction with flow controls as 'while'

# Import libraries
import subprocess
import datetime
import time
import logging
from logging.handlers import RotatingFileHandler

# Function name: print_timestamp
# Purpose      : prints a timestamp to the terminal
# Arguments    : str, ip
# Return       : none
def print_timestamp(str,ip):
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    if ip is None:
        logging.warning(f'{timestamp} {str}')
        #print(f'{timestamp} {str}')
    else:
        logging.info(f'{timestamp} {str} to {ip}')
        #print(f'{timestamp} {str} to {ip}')
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

def main():
    log_file = 'Event_Logging_Tool_Part_1_of_3.py'
    log_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y/%d/%m %I:%M:%S %p')
    file_handler = RotatingFileHandler(log_file)
    file_handler.setFormatter(log_formatter)
    logging.basicConfig(level=logging.DEBUG, handlers=[file_handler])


    logging.info('Starting script Event_Logging_Tool_Part_1_of_3.py...\n')

    # filename to store the ping's status
    filename  = "{}_logs".format(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))

    # inputs the user to enter the target IP
    target_ip = input("Enter your target IP: ")
    ping_output = None

    # infinite loop
    while True:

        try:
            # store the output in the variable ping_output
            ping_output = subprocess.run(["ping","-c","1",target_ip], stdout=subprocess.PIPE, timeout=3)
        except subprocess.TimeoutExpired as e:
            logging.warning("Timeout Expired")
        else:

            # status' verification
            if "1 received" in ping_output.stdout.decode('utf-8'):
                print_timestamp("Network Active",target_ip)
                #print_timestamp_2_file("Network Active",target_ip,filename)
            else:
                print_timestamp("Network Inactive",target_ip)
                #print_timestamp_2_file("Network Active",target_ip,filename)

            # pings every 2 seconds
            time.sleep(2)


if __name__ == "__main__":
    main()
