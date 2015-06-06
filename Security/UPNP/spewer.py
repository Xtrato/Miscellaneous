#This script iterates through a input file formatted with ip:port\r\n and sends a SSDP M-Search to each address.
#Used for UPNP enumeration
from scapy.all import *

inputIPs = open('input.txt')

for address in inputIPs:
    colon = address.index(':')
    ip = address[:colon]
    port = int(address[colon + 1:-1])
    print ip
    print port
    payload = "M-SEARCH * HTTP/1.1\r\n" "Host:%s:%s\r\n" "ST:ssdp:all\r\n" "Man:\"ssdp:discover\"\r\n" "MX:4\r\n\r\n" % (ip, port)
    print payload
    packet = IP(dst=ip)/UDP(dport=port, sport=port)/payload
    send(packet)
    payload = "M-SEARCH * HTTP/1.1\r\n" "Host:%s:%s\r\n" "ST:upnp:rootdevice\r\n" "Man:\"ssdp:discover\"\r\n" "MX:3\r\n\r\n" % (ip, port)
    print payload
    packet = IP(dst=ip)/UDP(dport=port, sport=port)/payload
    send(packet)

print 'THE END'