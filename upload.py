# -*- coding: utf-8 -*- 

import sys
import os
import sftpModule, ftpModule
import percentBar



if __name__ == '__main__':
    rootdir = 'par'
    filelist = []

    for parent,dirnames,filenames in os.walk(rootdir):
        for filename in filenames:
            filelist.append(parent+'/'+filename)
    totalFiles = len(filelist)
    print 'total', totalFiles

    try:
        print 'using sftp...'
        uploader = sftpModule.Sftp()
        uploader.setSftpParams('127.0.0.1', 'ftpuser', pwd = '111111', homeDir = 'upload')
        uploader.upload('par')
    except Exception, e:
        print e
        print 'using ftp...'
        try:
            uploader = ftpModule.Ftp()
            uploader.setFtpParams('127.0.0.1', 'ftpuser', pwd = '111111', homeDir = 'upload')
            uploader.upload('par')
        except Exception, e:
            print e
            print 'both sftp and ftp failed'