#!/usr/bin/python3

# Script : OpsChallenge36.py
# Purpose:
# Why    :

import subprocess

def banner_grabbing_netcat(url_ip,port_number):
    result = subprocess.run(['nc', '-w2', url_ip, port_number], capture_output=True, text=True)
    print(result.stdout)

def banner_grabbing_telnet(url_ip,port_number):
    os.system(f'telnet {url_ip} {port_number}')

def banner_grabbing_nmap(url_ip,port_number):
    print("nmap")

def main():

        url_ip      = input("Enter the URL or IP address:\n\t> ")
        port_number = input("\nEnter the port number:\n\t> ")

        banner_grabbing_netcat(url_ip,port_number)
        while(not url_ip == "scanme.nmap.org"):
            url_ip = input("Enter the URL or IP address:\n\t> ")

        while(True):

            user_input = input("\n\n---> Select one of the following (1,2,3 or q):\n\n1. Netcat;\n2. Telnet\n3. Nmap\nq. Quit\n\n> ")

            match(user_input):
                case "1":
                    banner_grabbing_netcat(url_ip,port_number)
                    break
                case "2":
                    banner_grabbing_telnet(url_ip,port_number)
                    break
                case "3":
                    banner_grabbing_nmap(url_ip,port_number)
                    break
                case "q":
                    print("\nQuitting...")
                    break
                case _:
                    print("\n ----- You do not entered a correct option. Try again -----\n")


if __name__ == "__main__":
    main()
