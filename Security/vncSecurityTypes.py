#This is a current work in progress and is used to fetch the security type used on a VNC server.
# execute the following first to allow for the TCP handshake: iptables -A OUTPUT -p tcp --tcp-flags RST RST -j DROP


from scapy.all import *


IpAddress = '192.168.1.16'
port = 5900


def vncCheck(packet):
    if packet.haslayer('Raw'):
        if 'RFB' in packet.load:
            clientVersion = IP(dst=IpAddress)/TCP(dport=port, flags='AP', seq=1, ack=packet.seq + 1)/'RFB 003.003\n'
            supportedtypesPacket = sr1(clientVersion)
            print supportedtypesPacket.show()
            authenticationType = ord(supportedtypesPacket.load[3])
            print 'Authentication type of : ' + str(authenticationType)
            if authenticationType == 0:
                print 'This server uses an Invalid Authentication type'
            elif authenticationType == 1:
                print 'This server uses No Authentication'
            elif authenticationType == 2:
                print 'This server uses VNC Authentication'
            elif authenticationType == 5:
                print 'This server uses RA2 Authentication'
            elif authenticationType == 6:
                print 'This server uses RA2ne Authentication'
            elif authenticationType == 16:
                print 'This server uses Tight Authentication'
            elif authenticationType == 17:
                print 'This server uses Ultra Authentication'
            elif authenticationType == 18:
                print 'This server uses TLS Authentication'
            elif authenticationType == 19:
                print 'This server uses VeNCrypt Authentication'
            elif authenticationType == 20:
                print 'This server uses GTK-VNC SASL Authentication'
            elif authenticationType == 21:
                print 'This server uses MD5 Hash Authentication'
            elif authenticationType == 22:
                print 'This server uses Colin Dean XVP Authentication'
            else:
                print 'This server uses an Unknown Authentication type'

syn = IP(dst=IpAddress)/TCP(dport=port, flags='S')
synack = sr1(syn)
ack = IP(dst=IpAddress)/TCP(dport=port, flags='A', seq=1, ack=synack.seq + 1)
send(ack)

filter = 'port ' + str(port) + ' and host ' + IpAddress
vnc = sniff(filter=filter, count=1, prn=vncCheck)

print 'End'
