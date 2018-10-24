#Script used to resolve IP addresses from a list of domains (domainsList) and output the results to ips.txt.

import dns.resolver

domainsFile = open('domainsList.txt', 'r')
ipFile = open('ips.txt', 'a')

for domain in domainsFile:
    try:
        answers = dns.resolver.query(domain[:-1])
        for ip in answers:
            print(domain + ' ' + str(ip))
            ipFile.write(str(ip) + '\n')
    except dns.resolver.NoAnswer:
        print ('NO A RECORD FOR' + domain)
        pass

ipFile.close()
domainsFile.close()