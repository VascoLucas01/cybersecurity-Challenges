#!/usr/bin/python3

# Script : 
# Purpose: 
# Why    : 

from scapy.all import *


HOST        = "8.8.8.8"
UPPER_LIMIT = 54
LOWER_LIMIT = 50
PORT_RANGE  = range(LOWER_LIMIT,UPPER_LIMIT+1)

print(f"Scanning host {HOST}...\n")

for dst_port in PORT_RANGE:
    # TCP packet with flag SYN 
    src_port = RandShort() 
    tcp_syn_packet = IP(dst=HOST)/TCP(sport=src_port,dport=dst_port,flags="S")
    response = sr1(tcp_syn_packet,timeout=1, verbose=0)
    
    if response and response.haslayer(TCP) and response[TCP].flags == 0x12: 
        # TCP packet with flag RST 
        send(IP(dst=HOST)/TCP(sport=src_port, dport=dst_port, flags="R"), verbose=0)
        print(f"Port {dst_port} is open")
    elif response and response.haslayer(TCP) and response[TCP].flags == 0x14: 
        print(f"Port {dst_port} is closed")
    else:
        print(f"Port {dst_port} is filtered or silently dropped")
        
    
    #if response:
    #    print(response.show())
    
print(f"\n{UPPER_LIMIT+1-LOWER_LIMIT} ports were scanned")


    
