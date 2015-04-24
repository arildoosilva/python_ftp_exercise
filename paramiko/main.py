# -*- coding: utf-8 -*-
# python3.4

import os
import paramiko
import time
from threading import Thread

os.system('cls' if os.name == 'nt' else 'clear')

# vars
# first connection
server1 = ''
user1 = ''
passwd1 = ''
dir1 = ''
port1 = 22
# second connection
server2 = ''
user2 = ''
passwd2 = ''
dir2 = ''
port2 = 22

def generate_hash_file(server, user, passwd, dir):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(server, username = user, password = passwd)
    except paramiko.SSHException:
        print('Connection Failed')
        quit()
    print('Connected to', server)
    command = ('find '+str(dir)+' -type f -exec sha256sum {} \; > /home/'+str(user)+'/$(hostname)-$(date +%s).txt')
    stdin,stdout,stderr = ssh.exec_command(command, get_pty = True)
    exit_status = stdout.channel.recv_exit_status()
    print('Checksum file generated for', dir, '-', ('OK' if exit_status == 0 else ('Error generating for', dir)))
    #for line in stdout.readlines():
    #print(line.strip())
print('Finished. Disconnecting SSH from', server)
    ssh.close()

def get_hash_file(server, user, passwd, port):
    t = paramiko.Transport((server, port))
    try:
        t.connect(username = user, password = passwd)
    except paramiko.SSHException:
        print('Connection Failed')
        quit()
    sftp = paramiko.SFTPClient.from_transport(t)
    sftp.get(server+'.txt', server+'.txt')
    t.close()

#generate_hash_file(server1, user1, passwd1, dir1)
#generate_hash_file(server2, user2, passwd2, dir2)
#get_hash_file(server1, user1, passwd1, port1)
#get_hash_file(server2, user2, passwd2, port2)

t1 = Thread(target=generate_hash_file, args=(server1, user1, passwd1, dir1))
t1.start()
time.sleep(2)
t2 = Thread(target=generate_hash_file, args=(server2, user2, passwd2, dir2))
t2.start()
t1.join()
t2.join()

get_hash_file(server1, user1, passwd1, port1)
get_hash_file(server2, user2, passwd2, port2)