import bigsuds
import os.path

device=raw_input('Enter Device :')

file_name1=device+'iQuerypre.txt'
file_name2=device+'iQuerypost.txt'

if os.path.isfile(file_name1):
	outputFile = open(file_name2, 'w+')
else:
	outputFile = open(file_name1, 'w+')

b = bigsuds.BIGIP(hostname = device,username = 'admin', password = 'born2run',)
iquerystats=b.System.Statistics.get_all_gtm_iquery_statistics_v2()

for stats in iquerystats['statistics']:
	print >> outputFile, stats['connection_state'] +"," + stats['server'] + "," + stats['ip_address'] + "," + stats['data_center']

'''pools=b.LocalLB.Pool.get_list()
wideips=b.GlobalLB.WideIP.get_list()
wideipcount=len(wideips)
print >>outputFile,"Total Wideips"+str(wideipcount)


for wideip in wideips:
  wideipstatus=b.GlobalLB.WideIP.get_object_status([wideip])
  wideippools=b.GlobalLB.WideIP.get_wideip_pool([wideip])
  for status in wideipstatus:
    wname= wideip.replace("/Common/","")
    statd= status['status_description']
    print >> outputFile,"Wide IP",wname+":",statd
    #print statd
  for wideippool in wideippools:
    for pool in wideippool:
      poolname= pool['pool_name']
      poolsstat= b.GlobalLB.Pool.get_object_status([poolname])
      poolmembers= b.GlobalLB.Pool.get_member([poolname])
      for poolstat in poolsstat:
        #print poolstat['status_description']
        rpname= poolname.replace("/Common/","")
        print >> outputFile,"Pool",rpname+":",poolstat['status_description'] 
      for poolmember in poolmembers:
        for mem in poolmember:
          x= mem['member']['address']
          y=mem['member']['port']
          z= str(x)+":"+str(y)
          print >> outputFile,z'''
