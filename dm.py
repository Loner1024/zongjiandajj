#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time, sys

from danmu import DanMuClient

def pp(msg):
    print(msg.encode(sys.stdin.encoding, 'ignore').
        decode(sys.stdin.encoding))

dmc = DanMuClient('http://www.douyu.com/610588')
if not dmc.isValid(): print('Url not valid')

@dmc.danmu
def danmu_fn(msg):
    #pp('[%s] %s' % (msg['NickName'], msg['Content']))
    print(msg['Content'])
    with open('1.txt','ab') as f:
        dm_text = str(msg['Content'].encode('utf-8'))
        f.write(str(dm_text))
        f.close()



'''
@dmc.gift
def gift_fn(msg):
    pp('[%s] sent a gift!' % msg['NickName'])
'''

dmc.start(blockThread = True)