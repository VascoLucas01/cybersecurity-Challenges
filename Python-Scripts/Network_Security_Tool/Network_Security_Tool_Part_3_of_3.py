#!/usr/bin/python3

# Script : Network_Security_Tool_Part_3_of_3.py
# Purpose: Add the following features to Network_Security_Tool_Part_2_of_3.py:
########## Ping an IP address determined by the user.
########## If the host exists, scan its ports and determine if any are open.
# Why    : 

from scapy.all import *
import ipaddress
import sys

def TCP_Port_Range_Scanner(host,common_ports):

    print(f"\nScanning host {host}...\n")

    for dst_port in common_ports:
        # TCP packet with flag SYN 
        src_port       = RandShort() 
        tcp_syn_packet = IP(dst=host)/TCP(sport=src_port,dport=dst_port,flags="S")
        response       = sr1(tcp_syn_packet,timeout=1, verbose=0)
        
        if response and response.haslayer(TCP) and response[TCP].flags == 0x12: 
            # TCP packet with flag RST 
            tcp_rst_packet = IP(dst=host)/TCP(sport=src_port, dport=dst_port, flags="R")
            send(tcp_rst_packet, verbose=0)
            
            print(f"Port {dst_port} is open")
        elif response and response.haslayer(TCP) and response[TCP].flags == 0x14: 
            print(f"Port {dst_port} is closed")
        else:
            print(f"Port {dst_port} is filtered or silently dropped")
        

def ICMP_Ping_Sweep(host):

    icmp_packet = IP(dst=host)/ICMP()
    response = sr1(icmp_packet, timeout=1) 

    if response == None or (response and response.haslayer(ICMP) and response[ICMP].type == 3 and response[ICMP].code in [1,2,3,9,10,13]):
        return False
    else:
        return True
        
            
        
        
common_ports = [20, 21, 22, 53, 80, 123, 179, 443, 500, 587, 3389]
args = sys.argv

if(len(args) != 2):
    print("\nUsage:\n./Network_Security_Tool_Part_3_of_3.py IP_ADDRESS (e.g. ./Network_Security_Tool_Part_3_of_3.py 8.8.8.8)")    
else:
    try:
        ip_address = str(ipaddress.ip_address(args[1]))
    except ValueError:
        print("\n ----- You do not entered a valid IP ADDRESS -----\n")
        print("Ending script...\n")
        exit(0)    
    except:
        print("\n ----- Something went wrong -----\n")
        print("Ending script...\n")
        exit(0) 

print("\n--------------------------------------------------")
if(ICMP_Ping_Sweep(ip_address)):
    print("\n--------------------------------------------------")
    TCP_Port_Range_Scanner(ip_address,common_ports)
    print("\n--------------------------------------------------")
