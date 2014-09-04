#This is a current work in progress and is used to fetch the security type used on a VNC server.

from scapy.all import *

IpAddress = '192.168.1.12'
port = '5900'


def vncCheck(packet):
    if packet.haslayer('Raw'):
        if 'RFB' in packet.load:
            clientVersion = IP(dst='192.168.1.12')/TCP(dport=5900, flags='AP', seq=1, ack=packet.seq + 1)/'RFB 003.003\n'
            supportedtypesPacket = sr1(clientVersion)
            authenticationType = ''
            normal = ''
            for char in supportedtypesPacket.load:
                authenticationType += str(ord(char))
            print authenticationType

syn = IP(dst='192.168.1.12')/TCP(dport=5900, flags='S')
synack = sr1(syn)
ack = IP(dst='192.168.1.12')/TCP(dport=5900, flags='A', seq=1, ack=synack.seq + 1)
send(ack)

filter = 'port ' + port + ' and host ' + IpAddress
vnc = sniff(filter=filter, count=1, prn=vncCheck)

print 'End'
