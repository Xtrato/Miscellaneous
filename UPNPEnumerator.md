UPNPEnumeration
===============
Python code designed to enumerate device details using UPNP. Uses the Scapy framework.

The details on each UPNP device are returned and placed in a dictonary for easy access.

## ProcessPacket() ##
The processPacket function is executed on each packet captured by the Scapy sniffer. This function simply grabs the location of the XML file. Then reads its contents to dictionaries called currentDict which are then stored in a list called upnpDevices.