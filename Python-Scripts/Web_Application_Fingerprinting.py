#!/usr/bin/python3

# Script : Web_Application_Fingerprinting.py
# Purpose: Prompts the user to type a URL or IP address
########## Prompts the user to type a port number
########## Performs banner grabbing using netcat against the target address at the target port; prints the results to the screen then moves on to the step below
########## Performs banner grabbing using telnet against the target address at the target port; prints the results to the screen then moves on to the step below
########## Performs banner grabbing using Nmap against the target address of all well-known ports; prints the results to the screen
# Why    :

import os

def banner_grabbing_netcat(url_ip,port_number):
    result = os.system(f'nc -w1 {url_ip} {port_number}')
    print(result)

def banner_grabbing_telnet(url_ip,port_number):
    result = os.system(f'telnet {url_ip} {port_number}')
    print(result)

def banner_grabbing_nmap(url_ip):
    result = os.system(f'nmap -p 1-1024 -sV {url_ip}')
    print(result)

def main():

        url_ip      = input("Enter the URL or IP address:\n\t> ")
        port_number = input("\nEnter the port number:\n\t> ")
        
        
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
                    banner_grabbing_nmap(url_ip)
                    break
                case "q":
                    print("\nQuitting...")
                    break
                case _:
                    print("\n ----- You do not entered a correct option. Try again -----\n")


if __name__ == "__main__":
    main()
