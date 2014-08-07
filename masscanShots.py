import xml.etree.ElementTree as ET
import subprocess
import argparse
#Argparse used to gather the location of the nmap XML file from the argument.
parser = argparse.ArgumentParser(description='This program is used to provide screenshots of webpages found during nmap scans.')
parser.add_argument('-x','--xmlfile', help='location of the XML file produced by nmap.', required=True)
args = vars(parser.parse_args())
#Hides the wkhtmltoimage-i386 standard output
devNull = open('/dev/null', 'w')
addresses = []
#Opens the masscan or nmap XML file
results = ET.parse(args['xmlfile'])
root = results.getroot()
#Iterates through the IP addresses in the XML file
for address in root.iter('address'):
#Appends each address to the addresses list
addresses.append(address.attrib['addr'])
print addresses
#Iterates through each of the IP addresses
for ip in addresses:
#Prints the current IP address being screenshotted.
print 'Currently taking a screenshot of: ' + str(ip)
#Takes a screenshow and saves it in the same directory with the IP address as the file name.
screenshot = subprocess.Popen(["wkhtmltoimage-i386", ip, ip+'.png'], stdout=devNull, stderr=devNull)
screenshot.communicate()
print "Finished"__author__ = 'root'