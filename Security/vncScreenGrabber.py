import subprocess
from lxml import etree
import time

port = None
address = None

for event, element in etree.iterparse('scan.xml', tag="host"):
    for child in element:
        if child.tag == 'address':
            address = child.attrib['addr']
        if child.tag == 'ports':
            for a in child:
                port = a.attrib['portid']
        if port > 1 and address > 1:
            server = address + ':' + port[2:]
            print 'Currentley attempting ' + server
            try:
                snapshotter = subprocess.Popen(['timeout', '5s', 'vncsnapshot', server, server + '.jpg'],stdout=None)
                time.sleep(0.1)
            except:
                time.sleep(5)
            port = None
            address = None
    element.clear()
print 'End'