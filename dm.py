# -*- coding: utf-8 -*-

import time,sys

from danmu import DanMuClient

def pp(msg):
    print(msg.encode(sys.stdin.encoding, 'ignore').
        decode(sys.stdin.encoding))

dmc = DanMuClient('http://www.douyu.com/610588')
if not dmc.isValid(): print('Url not valid')

@dmc.danmu
def danmu_fn(msg):
    print(msg['Content'])
    with open('1.txt','ab') as f:
        dm_text = msg['Content']
        f.write(dm_text.encode('utf-8'))
        f.close()



'''
@dmc.gift
def gift_fn(msg):
    pp('[%s] sent a gift!' % msg['NickName'])
'''

dmc.start(blockThread = True)