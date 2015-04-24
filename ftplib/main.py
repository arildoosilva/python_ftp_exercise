# -*- coding: utf-8 -*-
# python3.4

import ftp_defs

# vars
server = ''
user = ''
password = ''
root_dir = ''

x = ftp_defs.Con_Ftp(server, user, password, root_dir)
x.list_files()
