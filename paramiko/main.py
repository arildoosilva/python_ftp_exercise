# -*- coding: utf-8 -*-
# python3.4

import getpass
import sys
import getopt
import ftp
import os
import time
from threading import Thread

# vars
server1 = None
port1 = None
user1 = None
passwd1 = None
dir1 = None
server2 = None
port2 = None
user2 = None
passwd2 = None
dir2 = None


def main(argv):
    help = ('Uses python 3.4\n\n'
            'Usage: python main.py <server1> <port1> <username1> <directory1> '
            '<server2> <port2> <username2> <directory2> <password1> <password2>\n\n'
            'Necessary modules: getpass, sys, getopt, os, threading, paramiko, time\n\n'
            'SFTP and SSH are required')

    #prints the help text when -h or --help is used
    try:
        opts, args = getopt.getopt(argv, 'h', ['help'])
    except getopt.GetoptError:
        print(help)
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print(help)
            sys.exit()

    global server1
    global port1
    global user1
    global passwd1
    global dir1
    global server2
    global port2
    global user2
    global passwd2
    global dir2

    if len(sys.argv) < 9:
        print('Missing parameters\n')
        print(help)
        sys.exit(2)
    else:
        server1 = sys.argv[1]
        port1 = sys.argv[2]
        user1 = sys.argv[3]
        dir1 = sys.argv[4]
        server2 = sys.argv[5]
        port2 = sys.argv[6]
        user2 = sys.argv[7]
        dir2 = sys.argv[8]
        if len(sys.argv) < 10:
            print('Enter the password for server-1', server1)
            passwd1 = getpass.getpass('Password: ', None)
        else:
            passwd1 = sys.argv[9]
        if len(sys.argv) < 11:
            print('Enter the password for server-2', server2)
            passwd2 = getpass.getpass('Password: ', None)
        else:
            passwd2 = sys.argv[10]

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')

    main(sys.argv[0:])

    t1 = Thread(target=ftp.generate_hash_file, args=(server1, user1, passwd1, dir1, port1))
    t1.start()

    time.sleep(2)

    t2 = Thread(target=ftp.generate_hash_file, args=(server2, user2, passwd2, dir2, port2))
    t2.start()

    t1.join()
    t2.join()

    ftp.get_hash_file(server1, user1, passwd1, port1)
    ftp.get_hash_file(server2, user2, passwd2, port2)
