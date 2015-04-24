# -*- coding: utf-8 -*-
# python3.4

import ftputil
import os

# os.system('cls' if os.name=='nt' else 'clear')

# vars
server = ''
user = ''
password = ''
root_folder = ''
paths = []
names = []
sizes = []
ftp = ftputil.FTPHost(server, user, password)
msgs = set()

def comparePaths(actual_path, previous_path, actual_size, previous_size):
    global msgs
    while (actual_path == previous_path):
        if (actual_size != previous_size):
            msg = ([actual_path])
            msgs.update(msg)
            break
        break

recursive = ftp.walk(root_folder, topdown=True, onerror=None)
for root_folder, subdir, files in recursive:
    for name in files:
        paths.append(ftp.path.join(root_folder))
        sizes.append(ftp.stat(ftp.path.join(root_folder, name))[6])
        names.append(name)

for x in range(0, len(paths)):
    print(paths[x], names[x], sizes[x])
    comparePaths(paths[x], paths[0] if x == 0 else paths[x-1], sizes[x], sizes[0] if x == 0 else sizes[x-1])

print('directories containing files with different sizes', msgs)































