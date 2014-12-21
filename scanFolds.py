# -*- coding: utf-8 -*- 

import os
import os.path
rootdir = "/srv/ftp/upload"

filelist = []

for parent,dirnames,filenames in os.walk(rootdir):
    for dirname in  dirnames:
        print parent + '/' + dirname

    for filename in filenames:
        print parent + '/' + filename
        filelist.append(parent+'/'+filename)
