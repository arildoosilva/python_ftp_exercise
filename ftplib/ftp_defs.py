# -*- coding: utf-8 -*-

import ftplib
import os

# class that receives server, user, password and root_dir to be listed, prints a list of files
class Con_Ftp:
    server = ''
    user = ''
    password = ''
    root_dir = ''
    files = []
    ftp = ''
    
    def __init__(self, server, user, password, root_dir):
        Con_Ftp.server = server
        Con_Ftp.user = user
        Con_Ftp.password = password
        Con_Ftp.root_dir = root_dir
    
    def busca_ftp(self):
        dirs=Con_Ftp.ftp.nlst() # list of nodes
        for item in (path for path in dirs if path not in ('.', '..')): # for each item in the directory
            try:
                Con_Ftp.ftp.cwd(item)
                try:
                    Con_Ftp.files.append('Directories '+Con_Ftp.ftp.pwd())
                    Con_Ftp.ftp.dir(Con_Ftp.files.append) # adds all files that are inside root_dir to the list
                    Con_Ftp.busca_ftp(Con_Ftp.ftp)
                finally:
                    Con_Ftp.ftp.cwd('..') # cd ..
            except(ftplib.error_perm): # Exception raised when an error code signifying a permanent error 
                pass

    def list_files(self):
        Con_Ftp.ftp=ftplib.FTP(Con_Ftp.server)
        Con_Ftp.ftp.login(Con_Ftp.user, Con_Ftp.password)
        Con_Ftp.ftp.cwd(Con_Ftp.root_dir)
        Con_Ftp.busca_ftp(Con_Ftp.ftp)
        Con_Ftp.ftp.quit()
        files = Con_Ftp.files
        for line in files:
            print(line)
