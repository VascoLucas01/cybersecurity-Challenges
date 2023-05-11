#!/usr/bin/python3

# Script : OpsChallenge12.py
# Purpose: 
# Why    : 

from scapy.all import *
import ipaddress


def TCP_Port_Range_Scanner(host, lower_port, upper_port):
    port_range = range(lower_port,upper_port+1)
    
    print(f"Scanning host {host}...\n")

    for dst_port in port_range:
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
        
    print(f"\n{upper_port+1-lower_port} ports were scanned")



def ICMP_Ping_Sweep(network_address):
    network = ipaddress.ip_network(network_address)
    hosts = [str(host) for host in network.hosts()]
    
    number_hosts_block  = 0
    number_hosts_up     = 0
    number_no_responses = 0
    
    
    for host in hosts:
        icmp_packet = IP(dst=host)/ICMP()
        response = sr1(icmp_packet, timeout=1) 

        if response == None:
            number_no_responses += 1
            print(f"{host}: is down or unresponsive")
        elif response and response.haslayer(ICMP) and response[ICMP].type == 3 and response[ICMP].code in [1,2,3,9,10,13]:
            number_hosts_block += 1
            print(f"{host}: is actively blocking ICMP traffic")
        else:
            number_hosts_up += 1
            print(f"{host} is responding")
            
    print(f"Statistics:\nNumber of hosts down or unresponsive: {number_no_responses}\nNumber of hosts actively blocking ICMP traffic: {number_hosts_block}\nNumber of hosts responding: {number_hosts_up}")
        
        

while(True):
    
    print("Choose one of the following options:")
    print("\nMode 1 - TCP Port Range Scanner\nMode 2 - ICMP Ping Sweep\nMode 3 - Type \"q\" to quit")

    user_input = input("\n>")
    
    match(user_input):
        case "1":
            host       = input("HOST: ")
            lower_port = int(input("Lower port: "))
            upper_port = int(input("Upper port: "))
            
            print("\n--------------------------------------------------")
            TCP_Port_Range_Scanner(host, lower_port, upper_port)
            print("--------------------------------------------------\n")
        case "2":
            network_address = input("Network Address: ")
            
            print("\n--------------------------------------------------")
            ICMP_Ping_Sweep(network_address)
            print("--------------------------------------------------\n")
            
        case "q":
            break
        case _:
            print("\n ----- You do not entered any correct option. Try again -----\n")
