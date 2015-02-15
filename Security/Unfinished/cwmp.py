#A work in progress, An attempt to interact with CWMP server.
from scapy.all import *

ip = IP(src='192.168.1.17', dst='62.24.243.161')

syn = ip/TCP(sport=1500, dport=7547, flags="S", seq=564)
synack = sr1(syn)

print 'SynAck Sent'


httpRequest = 'POST /cwmpWeb/CPEMgt HTTP/1.1\n\n'
httpRequest += 'Host: 10.10.10.11'
httpRequest +=
request = ip/TCP(sport=1500, dport=7547, flags="A", seq=synack[TCP].ack, ack=synack[TCP].seq + 1)/httpRequest
reply = sr1(request)

print reply.show()
print 'End'
