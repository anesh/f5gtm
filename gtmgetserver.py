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
servers=b.GlobalLB.Server.get_list()
for server in servers:
	servstatus =b.GlobalLB.Server.get_object_status([server])
        for stats in servstatus:
		print >> outputFile,server+", "+stats['availability_status']
