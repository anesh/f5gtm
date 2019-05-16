import bigsuds
import os
device=raw_input('Enter Device :')


file_name1=device+'-ServerStatsPre.txt'
file_name2=device+'-ServerStatsPost.txt'

if os.path.isfile(file_name1):
        outputFile = open(file_name2, 'w+')
else:
        outputFile = open(file_name1, 'w+')


b = bigsuds.BIGIP(hostname = device,username = 'admin', password = 'born2run',)
virtualservers=b.GlobalLB.VirtualServerV2.get_list()
stats=b.GlobalLB.VirtualServerV2.get_object_status(virtualservers)

for virtual,stat in zip(virtualservers,stats):
	print virtual['name']+"\t"+ stat['availability_status']
