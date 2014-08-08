#Python code designed to enumerate device details using UPNP. Uses the Scapy framework.
#README at https://github.com/Xtrato/Miscellaneous/blob/master/Readme%27s/UPNPEnumerator.md
from scapy.all import *
import xml.etree.ElementTree as ET
import urllib2
import collections
upnpDevices = []
def processPacket(response):
    noXMLFile = False
    #Checks if the packet being analysed is a HTTP response packet from the UPNP device.
    if response.load[:15] == "HTTP/1.1 200 OK":
        #creates a new dictionary to store details on the current device being parsed.
        currentDevice = collections.OrderedDict()
        #Gets the location of the XML file returned in the response and stores it to a variable.
        #Two variables used as sometimes the location is prefaced with LOCATION other times Location.
        location = response.load[response.load.find("Location:") + 9:][:response.load[response.load.find("Location") + 10:].find("\r\n") + 2]
        location2 = response.load[response.load.find("LOCATION:") + 9:][:response.load[response.load.find("LOCATION") + 10:].find("\r\n") + 2]
        #Checks if the packet sniffed from scapy is a responce packet with UPNP details.
    if "200 OK" in location:
        try:
            #Opens the XML file to the variable xmlFileOnWeb. Xml file stored at location variable gathered from the UPNP response.
            xmlFileOnWeb = urllib2.urlopen(location2)
        except (urllib2.HTTPError, ValueError):
            noXMLFile = True
        else:
            try:
                #Opens the XML file to the variable xmlFileOnWeb. Xml file stored at location variable gathered from the UPNP response.
                xmlFileOnWeb = urllib2.urlopen(location)
        except (urllib2.HTTPError, ValueError):
            noXMLFile = True
    #Checks if the XML file returned in the response is present.(Runs statement if it is).
    if noXMLFile == False:
        xmlRoot = ET.fromstring(xmlFileOnWeb.read())
        #Iterates through each element in the XML file.
        for element in xmlRoot.iter():
            if str(element.text) != "None":
                #Adds the element (Key) and the value to the ordered dict.
                currentDevice[element.tag[33:]] = str(element.text)
        #If entry dosn't already exist in upnpDevices list this appends the populated currentDevice dict to upnpdevices.
        existingDevice = 0
        for device in upnpDevices:
            if device == currentDevice:
                existingDevice = 1
        if existingDevice == 0:
            upnpDevices.append(currentDevice)
        #print upnpDevices[-1]
#Payload used to generate responses from UPNP devices detailing the XML schema location etc..
payload = "M-SEARCH * HTTP/1.1\r\n" "Host:239.255.255.250:1900\r\n" "ST:ssdp:all\r\n" "Man:\"ssdp:discover\"\r\n" "MX:4\r\n\r\n"
#creates the packet to be sent to the multicast address 239.255.255.250 on port 1900 with the payload defined above.
packet = IP(dst="239.255.255.250")/UDP(dport=1900, sport=RandShort())/payload
send(packet)
#captures all udp port 1900 packets and sends them individually to the processPacket function.
sniff(filter="udp port 1900", prn=processPacket, count = 10)
print upnpDevices
print "done"