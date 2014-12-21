# -*- coding: utf-8 -*- 
import sys
import os
import ftplib

class Ftp(object):
    """uploading using ftp"""
    def __init__(self):
        self.ftp = None

    def setFtpParams(self, ip, uname, pwd, homeDir = './', port = 21, timeout = 60):
        self.ip = ip
        self.uname = uname
        self.pwd = pwd
        self.port = port
        self.timeout = timeout
        self.homeDir = homeDir

    def initEnv(self):
        if self.ftp is None:
            self.ftp = ftplib.FTP()
            print '### connect sftp server: %s ...'%self.ip
            try:
                self.ftp.connect(self.ip, self.port, self.timeout)  
                self.ftp.login(self.uname, self.pwd)
                self.ftp.cwd(self.homeDir)
            except Exception, e:
                print e
    def clearEnv(self):  
        if self.ftp:
            self.ftp.close()
            print '### disconnect sftp server: %s!'%self.ip   
            self.ftp = None

    def uploadDir(self, localdir='./', remotedir='./'):
        if not os.path.isdir(localdir):
            return
        for file in os.listdir(localdir):
            src = os.path.join(localdir, file)
            if os.path.isfile(src):
                self.uploadFile(src, file)
            elif os.path.isdir(src):
                l = self.ftp.nlst()
                if(file not in l):
                    try:
                        self.ftp.mkd(file)
                        print 'upload dir : ', file
                    except Exception, e:
                        print e
                else:
                    print localdir+'/'+file, 'exist'
                self.ftp.cwd(file)
                self.uploadDir(src, file)
        self.ftp.cwd('..')

    def uploadFile(self, localpath, remotepath='./'):
        if not os.path.isfile(localpath):
            return
        l = self.ftp.nlst()
        index = localpath.rfind('\\')
        if index == -1:
            index = localpath.rfind('/')
        name = localpath[index+1:]
        if name not in l:
            print 'upload file: ', localpath
            self.ftp.storbinary('STOR ' + remotepath, open(localpath, 'rb'))
        else:
            print localpath, 'exist'
      
    def upload(self, src):
        self.initEnv()

        if os.path.isfile(src):
            index = src.rfind('\\')
            if index == -1:
                index = src.rfind('/')
            filename = src[index+1:]
            self.uploadFile(src, filename)
        elif os.path.isdir(src):
            self.uploadDir(src)

if __name__ == '__main__':
    ftp = Ftp()
    ftp.setFtpParams('127.0.0.1', uname = 'ftpuser', pwd = '111111', homeDir = 'upload')
    ftp.upload('par')
    #ftp.upload('test.txt')