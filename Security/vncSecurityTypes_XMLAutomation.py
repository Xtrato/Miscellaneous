from scapy.all import *
import subprocess
from lxml import etree


port = None
IpAddress = None


def log(message):
    logFile = open('servers.txt', 'a')
    logFile.write(message + '\n')
    logFile.close()

def vncCheck(packet):
    if packet.haslayer('Raw'):
        if 'RFB' in packet.load:
            clientVersion = IP(dst=IpAddress)/TCP(dport=port, flags='AP', seq=1, ack=packet.seq + 1)/'RFB 003.003\n'
            supportedtypesPacket = sr1(clientVersion)
            print supportedtypesPacket.show()
            authenticationType = str(ord(supportedtypesPacket.load[2])) + str(ord(supportedtypesPacket.load[3]))
            authenticationType = int(authenticationType)
            print IpAddress + ' Uses an Authentication type of : ' + str(authenticationType)
            if authenticationType == 00:
                print IpAddress + ' uses an Invalid Authentication type of ' + str(authenticationType)
                log(str(IpAddress) + ' uses an Invalid Authentication type')
            elif authenticationType == 01:
                print IpAddress + ' uses No Authentication'
                log(IpAddress + ' uses No Authentication')
            elif authenticationType == 02:
                print IpAddress + ' uses VNC Authentication'
                log(IpAddress + ' uses VNC Authentication')
            elif authenticationType == 05:
                print IpAddress + ' uses RA2 Authentication'
                log(IpAddress + ' uses RA2 Authentication')
            elif authenticationType == 06:
                print IpAddress + ' uses RA2ne Authentication'
                log(IpAddress + ' uses RA2ne Authentication')
            elif authenticationType == 16:
                print IpAddress + ' uses Tight Authentication'
                log(IpAddress + ' uses Tight Authentication')
            elif authenticationType == 17:
                print IpAddress + ' uses Ultra Authentication'
                log(IpAddress + ' uses Ultra Authentication')
            elif authenticationType == 18:
                print IpAddress + ' uses TLS Authentication'
                log(IpAddress + ' uses TLS Authentication')
            elif authenticationType == 19:
                print IpAddress + ' uses VeNCrypt Authentication'
                log(IpAddress + ' uses VeNCrypt Authentication')
            elif authenticationType == 20:
                print IpAddress + ' uses GTK-VNC SASL Authentication'
                log(IpAddress + ' uses GTK-VNC SASL Authentication')
            elif authenticationType == 21:
                print IpAddress + ' uses MD5 Hash Authentication'
                log(IpAddress + ' uses MD5 Hash Authentication')
            elif authenticationType == 22:
                print IpAddress + ' uses Colin Dean XVP Authentication'
                log(IpAddress + ' uses Colin Dean XVP Authentication')
            else:
                print IpAddress + ' uses an Unknown Authentication type of: ' + str(authenticationType)
                log(IpAddress + ' uses an Unknown Authentication type')


for event, element in etree.iterparse('scan.xml', tag="host"):
    for child in element:
        #print child.attrib
        if child.tag == 'address':
            IpAddress = child.attrib['addr']
        if child.tag == 'ports':
            for a in child:
                port = int(a.attrib['portid'])
        if port > 1 and IpAddress > 1:
            server = IpAddress + ':' + str(port)
            print 'Currentley attempting ' + server


            syn = IP(dst=IpAddress)/TCP(dport=port, flags='S')
            synack = sr1(syn, timeout=2)
            if synack != None:
                ack = IP(dst=IpAddress)/TCP(dport=port, flags='A', seq=1, ack=synack.seq + 1)
                send(ack)
                filter = 'port ' + str(port) + ' and host ' + IpAddress
                vnc = sniff(filter=filter, count=1,timeout=2, prn=vncCheck)

            port = None
            IpAddress = None
    element.clear()
print 'End'