# -*- coding: utf-8 -*-
# python3.4

from time import strftime
import paramiko


def generate_hash_file(server, user, passwd, directory, server_port):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(server, username=user, password=passwd, port=int(server_port))
    except paramiko.SSHException:
        print('Connection Failed')
        quit()
    print('Connected to ' + server)
    print('Generating checksum file for ' + directory)
    filename = server + str(strftime("%H%M%S")) + '.txt'
    sshcommand = ('find ' + str(directory) + ' -type f -exec sha256sum {} \; > /home/' + str(user) + '/' + filename)
    stdin, stdout, stderr = ssh.exec_command(sshcommand, get_pty=True)
    exit_status = stdout.channel.recv_exit_status()
    print(('Checksum file generated for ' if exit_status == 0 else 'Error generating for ') + directory)
    get_hash_file(server, user, passwd, server_port, filename)
    ssh.exec_command(("rm " + filename), get_pty=True)
    print('Finished. Disconnecting SSH from ' + server)
    ssh.close()


def get_hash_file(server, user, passwd, port, filename):
    t = paramiko.Transport((server, int(port)))
    try:
        t.connect(username=user, password=passwd)
    except paramiko.SSHException:
        print('Connection Failed')
        quit()
    sftp = paramiko.SFTPClient.from_transport(t)
    sftp.get(filename, filename)
    t.close()
