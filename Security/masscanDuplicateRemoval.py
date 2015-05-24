#This is a script used in conjunction with the NTP monlist checker which can be found:
#https://github.com/Xtrato/Miscellaneous/blob/master/Security/ntpMonlistChecker.py
#to remove duplicates from a masscan log file.
#It parses through the masscan output called ntp.xml and produces a file called port123.txt.
#More information can be found http://jamesdotcom.com/?p=578
from lxml import etree
import argparse
import sys
parser = argparse.ArgumentParser(description='This tool parses the Masscan output and removed any duplicate IP enteries which commonley appear during UDP scans.') # This and preceding 3 lines used to control the arguments entered in the CLI.
parser.add_argument('-i', action="store",dest='inputFile', help='The Masscan XML file.')
parser.add_argument('-o', action="store",dest='outputFile', help='The output file.')
args = parser.parse_args()
args = vars(args)

if args['inputFile'] == None or args['outputFile'] == None:
    print 'Please specify an input and output file with the argument -i inputFile -o outputFile.'
    sys.exit()

port = None
address = None
parsedServers = []
#Opens the file used to store single enteries.
outputFile = open(args['outputFile'], 'a')
#Iterates through the masscan XML file.
for event, element in etree.iterparse(args['inputFile'], tag="host"):
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
            if address + ':' + port not in parsedServers:
                print address + ':' + port
                #Write the IP address to the file.
                outputFile.write(address + ':' + port + '\n')
                #write the IP to the parsedServers list
                parsedServers.append(address + ':' + port)
            port = None
            address = None
    element.clear()
outputFile.close()
print 'End'