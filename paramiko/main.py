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
user1 = None
passwd1 = None
dir1 = None
server2 = None
user2 = None
passwd2 = None
dir2 = None


def main(argv):
    help = ('Uses python 3.4\n\n'
            'Usage: python main.py <server1> <username1> <directory1> '
            '<server2> <username2> <directory2> <password1> <password2>\n\n'
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
    global user1
    global passwd1
    global dir1
    global server2
    global user2
    global passwd2
    global dir2

    if len(sys.argv) > 0:
        server1 = sys.argv[1]
    if len(sys.argv) >= 1:
        user1 = sys.argv[2]
    if len(sys.argv) >= 2:
        dir1 = sys.argv[3]
    if len(sys.argv) >= 3:
        server2 = sys.argv[4]
    if len(sys.argv) >= 4:
        user2 = sys.argv[5]
    if len(sys.argv) >= 5:
        dir2 = sys.argv[6]
    if len(sys.argv) >= 6:
        passwd1 = sys.argv[7]
    if len(sys.argv) >= 7:
        passwd2 = sys.argv[8]

    if server1 is None:
        server1 = input('Server 1: ')
    if user1 is None:
        user1 = input('Username for server '+server1+': ')
    if dir1 is None:
        dir1 = input('Directory: ')
    if passwd1 is None:
        print('Enter the password for server-1', server1)
        passwd1 = getpass.getpass('Password: ', None)

    if server2 is None:
        server2 = input('\nServer 2: ')
    if user2 is None:
        user2 = input('Username for server '+server2+': ')
    if dir2 is None:
        dir2 = input('Directory: ')
    if passwd2 is None:
        print('Enter the password for server-2', server2)
        passwd2 = getpass.getpass('Password: ', None)

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')

    main(sys.argv[1:])

    t1 = Thread(target=ftp.generate_hash_file, args=(server1, user1, passwd1, dir1))
    t1.start()

    time.sleep(2)

    t2 = Thread(target=ftp.generate_hash_file, args=(server2, user2, passwd2, dir2))
    t2.start()

    t1.join()
    t2.join()

    ftp.get_hash_file(server1, user1, passwd1, 22)
    ftp.get_hash_file(server2, user2, passwd2, 22)
