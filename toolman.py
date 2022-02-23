# -*- coding:utf-8 -*-
import pydirectinput
import time

for i in range(2,-1,-1): #倒數3秒
    print(i)
    time.sleep(1)

pydirectinput.press('3')
time.sleep(1)
pydirectinput.press('f4')
time.sleep(1)