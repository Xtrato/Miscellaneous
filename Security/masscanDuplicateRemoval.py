#This is a script used in conjunction with the NTP monlist checker which can be found:
#https://github.com/Xtrato/Miscellaneous/blob/master/Security/ntpMonlistChecker.py
#to remove duplicates from a masscan log file.
#It parses through the masscan output called ntp.xml and produces a file called port123.txt.
#More information can be found http://jamesdotcom.com/?p=578
from lxml import etree
port = None
address = None
parsedServers = []
#Opens the file used to store single enteries.
outputFile = open('port123.txt', 'a')
#Iterates through the masscan XML file.
for event, element in etree.iterparse('ntp.xml', tag="host"):
    for child in element:
        if child.tag == 'address':
            #Assigns the current iterations address to the address variable.
            address = child.attrib['addr']
        if child.tag == 'ports':
            for a in child:
                #Assigns the current iterations port to the port variable.
                port = a.attrib['portid']
        #is both port and IP address are present.
        if port > 1 and address > 1:
            #If the IP hasnt yet been added to the output file.
            if address not in parsedServers:
                print address
                #Write the IP address to the file.
                outputFile.write(address + '\n')
                #write the IP to the parsedServers list
                parsedServers.append(address)
            port = None
            address = None
    element.clear()
outputFile.close()
print 'End'