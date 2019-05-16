import socket
import bigsuds
import os
import dns.resolver

device=raw_input('Enter Device :')


file_name1=device+'DNSQueryPre.txt'
file_name2=device+'DNSQueryPost.txt'

if os.path.isfile(file_name1):
        outputFile = open(file_name2, 'w+')
else:
        outputFile = open(file_name1, 'w+')




resolver = dns.resolver.Resolver()
resolver.nameservers = ['10.127.80.12']
resolver.timeout = 2
resolver.lifetime = 2

def checkresolution(fqdn):
	answers= resolver.query(fqdn, 'A')
       	for answer in answers:
        	return answer



b = bigsuds.BIGIP(hostname = device,username = 'admin', password = 'born2run',)
wideips=b.GlobalLB.WideIP.get_list()

for wideip in wideips:
	wideipname=wideip.replace("/Common/","")
	try:
		output=checkresolution(wideipname)
		print >> outputFile,wideipname+" : "+ str(output)
	except Exception,e:
		print >> outputFile,wideipname + str(e)
