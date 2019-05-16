#!/bin/bash

for n in `cat enterprise-poc.txt`
do
        echo "Pushing to $n"
        if [ `ssh root@$n 'ls -al /shared/images' | grep -c "BIGIP-*.iso"` -gt 0 ] && [ "$1" != "all" ]
        then
                echo "Base ISO already exists - skipping ..."
        else
                scp /shared/images/BIGIP-11.*.iso root@$n:/shared/images/BIGIP-11.4.1.608.0.iso
                scp /shared/images/BIGIP-11.*.md5 root@$n:/shared/images/BIGIP-11.4.1.608.0.iso.md5
        fi
        scp /shared/images/Hotfix-BIGIP-11.4.1-HF4-647.121-ENG.iso root@$n:/shared/images/Hotfix-BIGIP-11.4.1-HF4-647.121-ENG.iso
        scp /shared/images/Hotfix-BIGIP-11.4.1-HF4-647.121-ENG.iso.md5 root@$n:/shared/images/Hotfix-BIGIP-11.4.1-HF4-647.121-ENG.iso.md5
done
