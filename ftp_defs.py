# -*- coding: utf-8 -*-

import ftplib

# classe que recebe o servidor, usuario, senha e pasta a ser listada, retorna uma list com os arquivos
class Con_Ftp:
    servidor = ''
    usuario = ''
    senha = ''
    pasta = ''
    arquivos = []
    ftp = ''
    
    def __init__(self, servidor, usuario, senha, pasta):
        Con_Ftp.servidor = servidor
        Con_Ftp.usuario = usuario
        Con_Ftp.senha = senha
        Con_Ftp.pasta = pasta
    
    def busca_ftp(self):
        dirs=Con_Ftp.ftp.nlst() #lista de nos
        for item in (path for path in dirs if path not in ('.', '..')): #pra cada item nao oculto nos diretorios abaixo
            try:
                Con_Ftp.ftp.cwd(item) #usa o comando cd
                #print('Verificando pasta', Con_Ftp.ftp.pwd())
                try:
                    var=Con_Ftp.ftp.dir(Con_Ftp.arquivos.append) #adiciona todos os arquivos da pasta no array
                    Con_Ftp.busca_ftp(Con_Ftp.ftp) #chama a def de novo para entrar nos subdiretorios
                finally:
                    Con_Ftp.ftp.cwd('..') #volta uma pasta
            except(ftplib.error_perm): #Exception raised when an error code signifying a permanent error 
                pass

    def lista_arquivos(self):
        Con_Ftp.ftp=ftplib.FTP(Con_Ftp.servidor)
        Con_Ftp.ftp.login(Con_Ftp.usuario, Con_Ftp.senha)
        Con_Ftp.ftp.cwd(Con_Ftp.pasta) #pasta raiz a ser listada
        Con_Ftp.busca_ftp(Con_Ftp.ftp)
        Con_Ftp.ftp.quit()
        return Con_Ftp.arquivos