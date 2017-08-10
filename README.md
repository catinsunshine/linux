# linux

Debian backup and notes:

./update: update and autoremove Debian

font.conf: Improve font showing in Chromium

Source.list: Debian Sid source list file

add_sftp_user.py:
  The script will create a new SFTP user account on AWS Ubuntu: 
  1. You should create sftp-users group and mkdir sftp-root directory in /home. It'll be helpful to manage users and store unique folder under sftp-root. Then you can  consider create a root account to control.
  2. The script will generate a bash file to create a new sFTP user in the same directory with permission 775
  3. It'll append new user account in /etc/ssh/sshd_config file to active it.
