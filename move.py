# -*- coding:utf-8 -*-
#import pydirectinput
import pydirectinput
import time

for i in range(2,-1,-1):
    print(i)
    time.sleep(1)

pydirectinput.keyDown('right')
#time.sleep(1)
#pydirectinput.keyUp('right')

#pydirectinput.press('ctrl')
time.sleep(1.5)
pydirectinput.keyUp('right')
'''
pydirectinput.press('ctrl')
#time.sleep(0.4)
pydirectinput.keyUp('right')


#time.sleep(1)
pydirectinput.keyDown('left')
pydirectinput.press('ctrl')
time.sleep(0.4)
pydirectinput.press('ctrl')
pydirectinput.keyUp('left')
'''
