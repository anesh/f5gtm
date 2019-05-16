
import os
import paramiko




f1 = open('enterprise-poc.txt', 'r')

devices = f1.readlines()

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

for device in devices:
    column = device.split()
    try:
        ssh.connect(column[1], username="root", password="born2run", timeout=4)
	print "running backup for "+ column[0]	
        stdin, stdout, stderr = ssh.exec_command("tmsh save /sys ucs /var/tmp/$HOSTNAME.ucs")
	print stderr.read()
	print "running Qkview for "+ column[0]
	stdin, stdout, stderr = ssh.exec_command("qkview")
        print stderr.read()
	print "Copying UCS.."
	stdin, stdout, stderr = ssh.exec_command("scp /var/tmp/$HOSTNAME.ucs ihdp@10.126.33.71:/apps/f5backups")
	print stderr.read()
	print "Copying qkview.."
	stdin, stdout, stderr = ssh.exec_command("scp /var/tmp/$HOSTNAME.qkview ihdp@10.126.33.71:/apps/f5backups")
        print stderr.read()

    except Exception, e:
        print e
	
f1.close()




