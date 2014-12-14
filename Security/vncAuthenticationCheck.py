#This script parses a list of IP/Port's and determines if the destination NTP server has monlist enabled.
#More information can be found http://jamesdotcom.com/?p=578
from scapy.all import *
import thread
#Raw packet data used to request Monlist from NTP server
rawData = "\x17\x00\x03\x2a" + "\x00" * 61
#File containing all IP addresses with NTP port open.
logfile = open('output.txt', 'r')
#Output file used to store all monlist enabled servers
outputFile = open('monlistServers.txt', 'a')
def sniffer():
    #Sniffs incomming network traffic on UDP port 48769, all packets meeting thease requirements run through the analyser function.
    sniffedPacket = sniff(filter="udp port 48769 and dst net 99.99.99.99", store=0, prn=analyser)

def analyser(packet):
    #If the server responds to the GET_MONLIST command.
    if len(packet) > 200:
        if packet.haslayer(IP):
            print packet.getlayer(IP).src
            #Outputs the IP address to a log file.
            outputFile.write(packet.getlayer(IP).src + '\n')

thread.start_new_thread(sniffer, ())

for address in logfile:
    #Creates a UDP packet with NTP port 123 as the destination and the MON_GETLIST payload.
    send(IP(dst=address)/UDP(sport=48769, dport=123)/Raw(load=rawData))
print 'End'