
import os
import pexpect
import time

device=raw_input('Enter Device :')

child = pexpect.spawn ('ssh root@'+ device)
child.expect ('Password:')
child.sendline ('default')
child.expect ('#')
time.sleep(1)
child.sendline ('bigip_add 192.168.190.130')
print child.before
