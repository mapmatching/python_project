# coding: utf-8
import time
import random
import datetime

import itchat

itchat.auto_login(hotReload=True)


sended = False
while True:
    now = datetime.datetime.now()
    if not sended and now.hour == 17 and now.minute > 20:
        weight = 0.05
        while not sended:
            r = random.random()
            print (r, weight)
            if r < weight:
                itchat.send('test', 'filehelper')
                sended = True
            else:
                weight += 0.05
            time.sleep(60)
        time.sleep(3600)

    # if now.hour > 12:
    #     sended = False 
