#Script used to resolve IP addresses from a list of domains (domainsList) and output the results to ips.txt.

import dns.resolver

domainsFile = open('domainsList.txt', 'r')
ipFile = open('ips.txt', 'a')

for domain in domainsFile:
    answers = dns.resolver.query(domain[:-1])
    for ip in answers:
        ipFile.write(str(ip) + '\n')

ipFile.close()
domainsFile.close()