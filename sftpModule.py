# _*_ coding: utf-8 _*_
import paramiko
import os
import sys

class Sftp(object):
    """uploading using sftp"""
    def __init__(self):
        self.sftp = None

    def setSftpParams(self, ip, uname, pwd = None, pkey = None, homeDir = './', port = 22, timeout = 60):
        self.ip = ip
        self.uname = uname
        self.pwd = pwd
        self.pkey = pkey
        self.port = port
        self.timeout = timeout
        self.homeDir = homeDir

    def initEnv(self):
        if self.sftp is None:
            try:
                t = paramiko.Transport(self.ip, self.port)
                if self.pkey != None:
                	t.connect(username = self.uname , pkey=self.pkey)
                elif self.pwd != None:
                    t.connect(username = self.uname, password = self.pwd)
                else:
                    print 'password or key is needed'
                    return
                self.sftp = paramiko.SFTPClient.from_transport(t)
                self.sftp.chdir(self.homeDir)
                print '### connect ftp server: %s!'%self.ip
            except Exception, e:
                print e
    def clearEnv(self):
        if self.sftp != None:
            self.sftp.close()
            print '### disconnect ftp server: %s!'%self.ip
            self.sftp = None
    def uploadFile(self, localPath, remotePath = './'):
        if not os.path.isfile(localPath):
            return
        files=self.sftp.listdir('.')
        index = localPath.rfind('\\')
        if index == -1:
            index = localPath.rfind('/')
        name = localPath[index+1:]
        if name not in files:
            try:
                self.sftp.put(localPath,remotePath)
                print 'upload file: ', localPath
            except Exception, e:
                print e
        else:
            print localPath, 'exist'

    def uploadDir(self, localPath, remotePath = './'):
        if not os.path.isdir(localPath):
            return
        for file in os.listdir(localPath):
            src = os.path.join(localPath, file)
            if os.path.isfile(src):
                self.uploadFile(src, file)
            elif os.path.isdir(src):
                l = self.sftp.listdir('.')
                if(file not in l):
                    try:
                        self.sftp.mkdir(file)
                        print 'upload dir: ',file
                    except Exception, e:
                        print 'failed in uploading dir : ', file
                        print e
                else:
                    print src, 'exist'
                self.sftp.chdir(file)
                self.uploadDir(src, file)
        self.sftp.chdir('..')
    def upload(self, src):
        self.initEnv()
        if os.path.isfile(src):
            index = src.rfind('\\')
            if index == -1:
                index = src.rfind('/')
            filename = src[index+1:]
            self.uploadFile(src,filename)
        elif os.path.isdir(src):
            self.uploadDir(src)
        else:
            print 'error in open ', src
        self.clearEnv()

if __name__ == '__main__':

    sftp = Sftp()
    pkey_path='/root/.ssh/id_rsa'
    #private_key = paramiko.RSAKey.from_private_key_file(pkey_path)
    sftp.setSftpParams('127.0.0.1', 'ftpuser', pwd = '111111', homeDir = 'upload')
    
    #sftp.upload('test.py')
    sftp.upload('par')