#!/usr/bin/env python
#-*-coding=utf-8-*-
import sys
from time import sleep

class percentBar(object):
    def __init__(self):
        self.output = sys.stdout
        self.barsize = 60
        self.totalsize = 60
    def printBar(self, count, size, file = 'default', percentage = 0):
        self.output.write('\r' + file + ': ')
        self.barsize = self.totalsize - len(file)-7
        count /= (size / self.barsize)
        self.filename = file
        for i in range(int(count)):
            self.output.write('>')
        for i in range(int(self.barsize)-int(count)):
            self.output.write('=')
        self.output.write(' ' + str(percentage) + '%\r')
        self.output.flush()
    def finish(self):
        print self.filename, 'finish'+' '*(self.totalsize-len(self.filename)-6)

if __name__ == '__main__':
    size = 10
    p = percentBar()
    for count in range(0,size):
        p.printBar(float(count), float(size), 'file', float(count)*100.0 / float(size))
        second = 1
        sleep(second)
    p.finish()