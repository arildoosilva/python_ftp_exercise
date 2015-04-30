# -*- coding: utf-8 -*-
# python3.4

import paramiko


def generate_hash_file(server, user, passwd, dir, server_port):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(server, username=user, password=passwd, port=server_port)
    except paramiko.SSHException:
        print('Connection Failed')
        quit()
    print('Connected to', server)
    print('Generating checksum file for', dir)
    command = ('find '+str(dir)+' -type f -exec sha256sum {} \; > /home/'+str(user)+'/$(hostname).txt')
    stdin, stdout, stderr = ssh.exec_command(command, get_pty=True)
    exit_status = stdout.channel.recv_exit_status()
    print(('Checksum file generated for' if exit_status == 0 else 'Error generating for'), dir)
    print('Finished. Disconnecting SSH from', server)
    ssh.close()


def get_hash_file(server, user, passwd, port):
    t = paramiko.Transport((server, port))
    try:
        t.connect(username=user, password=passwd)
    except paramiko.SSHException:
        print('Connection Failed')
        quit()
    sftp = paramiko.SFTPClient.from_transport(t)
    sftp.get(server+'.txt', server+'.txt')
    t.close()
