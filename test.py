# -*- coding:utf-8 -*-
import pyautogui
import pydirectinput
import time

screenWidth, screenHeight = pydirectinput.size() # Get the size of the primary monitor.
currentMouseX, currentMouseY = pydirectinput.position() # Get the XY position of the mouse.
#print(screenWidth,screenHeight,currentMouseX,currentMouseY)
'''
ox , oy = pydirectinput.position()
while 1:
    if (ox,oy) != pydirectinput.position():
        ox, oy = pydirectinput.position()
        print(ox, oy)
'''

for i in range(2,-1,-1): #倒數3秒
    print(i)
    time.sleep(1)

cnt = 0
'''
for pos in pydirectinput.locateAllOnScreen('./clock.png'):
    print(pos)
    cnt += 1

if cnt == 0: print('There was nothing matched.')
'''
'''
for i in range(5):
    #pydirectinput.click(x = d[0], y = d[1])
    pydirectinput.mouseDown(x=d[0], y=d[1], button='left')
    time.sleep(0.1)
    pydirectinput.mouseUp(x=d[0], y=d[1], button='left')
    time.sleep(0.3)
'''
'''
for pos in pyautogui.locateAllOnScreen('./ScreenShots/test.png', grayscale=True):
    print(pos)
'''

pos = pyautogui.locateOnScreen('./ScreenShots/clock.png')
print(pos)

