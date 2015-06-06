#This script iterates through a input file formatted with ip:port\r\n and sends a SSDP M-Search to each address.
#Packets sniffed in return are analysed and added to a SQLite database.
from scapy.all import *
from Queue import Queue
from threading import Thread
import sqlite3
import os
import urllib2
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

os.system('rm /root/PycharmProjects/upnpEnumeration/upnp.db')
conn = sqlite3.connect('upnp.db', check_same_thread=False)
inputIPs = open('input.txt')
c = conn.cursor()
c.execute('''CREATE TABLE devices (ip text, st text, usn text, server text, location text, date text, xml text)''')

def sniffBuffer(packet):
    thread.start_new_thread(analyser, ((packet,)))


def analyser(packet):
    c = conn.cursor()
    try:
        ip = packet[0][IP].src
        st = ''
        usn = ''
        server = ''
        location = ''
        date = ''
        xml = ''
        split = packet.load.split('\r\n')
        for attribute in split:
            if 'ST' in attribute:
                if not 'HOST:' in attribute:
                    st = attribute
                continue
            if 'USN' in attribute:
                usn = attribute
                continue
            if 'SERVER' in attribute:
                server = attribute
                continue
            if 'LOCATION' in attribute:
                try:
                    location = attribute
                    portDelimeterColon = attribute[15:].index(':') + 15
                    xmlURL = 'http://' + str(packet[0][IP].src + attribute[portDelimeterColon:])
                    file = urllib2.urlopen(xmlURL)
                    xml = file.read()
                except urllib2.URLError:
                    print 'BAD URL' + xmlURL
                    pass
            if 'DATE' in attribute:
                date = attribute
                continue
        #c.execute("INSERT INTO devices VALUES (ip, st, usn, server, location, date)")
        try:
            c.execute("INSERT INTO devices VALUES (?, ?, ?, ?, ?, ?, ?);", (ip, st, usn, server, location, date, xml))
            conn.commit()
        except Exception,e:
            print 'CANT ADD TO DB' + str(e)
            pass
    except Exception,e:
        print 'INDEX ERROR' + str(e)
        pass



def sniffer():
    sniff(filter="udp port 1900", store=0, prn=sniffBuffer)

thread.start_new_thread(sniffer, ())


print 'PAST THREAD'
for ip in inputIPs:
    time.sleep(0.4)
    colon = ip.index(':')
    print ip[:colon]
    payload1 = "M-SEARCH * HTTP/1.1\r\n" "Host:239.255.255.250:1900\r\n" "ST:ssdp:all\r\n" "Man:\"ssdp:discover\"\r\n" "MX:4\r\n\r\n"
    #payload2 = "M-SEARCH * HTTP/1.1\r\n" "Host:239.255.255.250:1900\r\n" "ST:upnp:rootdevice\r\n" "Man:\"ssdp:discover\"\r\n" "MX:3\r\n\r\n"
    packet = IP(dst=ip[:colon])/UDP(dport=1900, sport=1900)/payload1
    send(packet)

print 'THE END'
raw_input()
conn.close()
