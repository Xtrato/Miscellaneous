from scapy.all import *
 
#Must run the following command before executing this script. Allows for the TCP handshake to take place.
#iptables -A OUTPUT -p tcp --tcp-flags RST RST -j DROP
 
#IP and Port of the VNC server
IpAddress = '192.168.1.13'
port = 5900
 
#Function which is executed on each packet.
def vncCheck(packet):
    #Checks that the packet is a server protocol version response. (Should contain 'RFB' if it is.
    if packet.haslayer('Raw'):
        if 'RFB' in packet.load:
            #Creates and sends a clientVersion response. The security type response from the VNC server is saved in the
            #Variable supportedtypesPacket
            clientVersion = IP(dst=IpAddress)/TCP(dport=port, flags='AP', seq=1, ack=packet.seq + 1)/'RFB 003.003\n'
            supportedtypesPacket = sr1(clientVersion)
            #Extract the HEX value from the security type response.
            authenticationType = str(ord(supportedtypesPacket.load[2])) + str(ord(supportedtypesPacket.load[3]))
            authenticationType = int(authenticationType)
            #Match the value with the correct authentication type.
            print IpAddress + ' Uses an Authentication type of : ' + str(authenticationType)
            if authenticationType == 00:
                print IpAddress + ' uses an Invalid Authentication type of ' + str(authenticationType)
            elif authenticationType == 01:
                print IpAddress + ' uses No Authentication'
            elif authenticationType == 02:
                print IpAddress + ' uses VNC Authentication'
            elif authenticationType == 05:
                print IpAddress + ' uses RA2 Authentication'
            elif authenticationType == 06:
                print IpAddress + ' uses RA2ne Authentication'
            elif authenticationType == 16:
                print IpAddress + ' uses Tight Authentication'
            elif authenticationType == 17:
                print IpAddress + ' uses Ultra Authentication'
            elif authenticationType == 18:
                print IpAddress + ' uses TLS Authentication'
            elif authenticationType == 19:
                print IpAddress + ' uses VeNCrypt Authentication'
            elif authenticationType == 20:
                print IpAddress + ' uses GTK-VNC SASL Authentication'
            elif authenticationType == 21:
                print IpAddress + ' uses MD5 Hash Authentication'
            elif authenticationType == 22:
                print IpAddress + ' uses Colin Dean XVP Authentication'
            else:
                print IpAddress + ' uses an Unknown Authentication type of: ' + str(authenticationType)
 
#Creates and sends a TCP SYN packet to the VNC server. (Step 1 of the TCP handshake)
syn = IP(dst=IpAddress)/TCP(dport=port, flags='S')
synack = sr1(syn, timeout=2)
 
#Creates and sends an ACK packet is response to the servers SYNACK. (Step 3 of the TCP handshake)
ack = IP(dst=IpAddress)/TCP(dport=port, flags='A', seq=1, ack=synack.seq + 1)
send(ack)
 
#Sniffs incoming network data after the initial TCP handshake. Sends the packets to the vncCheck function.
filter = 'host ' + IpAddress
vnc = sniff(filter=filter, count=1,timeout=2, prn=vncCheck)