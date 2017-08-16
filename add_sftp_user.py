#!/usr/bin/env python3.6
import os

userName = input('Who will be added? ')

with open('./adduser', 'w') as f:
    f.write('#! /bin/bash')
    f.write('\nsudo adduser %s' % (userName))
    f.write('\nsudo usermod -G sftp-users -s /bin/false %s' % (userName))
    f.write('\nsudo mkdir /home/sftp-root/%s/' %(userName))
    f.write('\nsudo mkdir /home/sftp-root/%s/Incoming' % (userName))
    f.write('\nsudo mkdir /home/sftp-root/%s/Outgoing' % (userName))
    f.write('\nsudo chown %s:%s /home/sftp-root/%s/' % (userName, userName, userName))
    f.write('\nsudo chmod 755 /home/sftp-root/%s/' % (userName))
    f.write('\nsudo chmod 755 /home/sftp-root/%s/Incoming' % (userName))
    f.write('\nsudo chmod 755 /home/sftp-root/%s/Outgoing\n' % (userName))

print('File generated: adduser')
print('***'*30)

# add 0o as prefix of permission
os.chmod('./adduser', 0o775)
print('chmod 775 to file: adduser')
print('***'*30)

with open('./adduser') as f:
    print('adduser shows:')
    contents=f.read()
    print(contents)
print('***'*30)

# update /etc/ssh/sshd_config
# run it as 'sudo python3.6 add_sftp.py' for privileges issue

with open('/etc/ssh/sshd_config', 'a') as cg:
    cg.write('\n')
    cg.write('Match user %s\n' %(userName))
    cg.write('\tChrootDirectory /home/sftp-root/%s' %(userName))

print('sshd_config file updated.')
print('***'*30)

with open('/etc/ssh/sshd_config') as cg:
    print('sshd_config shows:')
    contents=cg.read()
    print(contents)

print('''
running commands:
sudo python3 add_sftp_user.py
sudo ./adduser
''')
