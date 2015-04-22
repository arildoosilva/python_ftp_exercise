# -*- coding: utf-8 -*-
#python3.4

from datetime import datetime
import ftp_defs

servidor = ''
usuario = ''
senha = ''
pasta_raiz = ''

x = ftp_defs.Con_Ftp(servidor, usuario, senha, pasta_raiz)
arquivos = x.lista_arquivos()

for arquivo in arquivos:
    print(arquivo)