# -*- coding:utf-8 -*-
import pyautogui
import pydirectinput
import random
import time

for i in range(3,-1,-1):
    print(i)
    time.sleep(1)

#im1 = pyautogui.screenshot('./clock.png', region=(812, 100, 1115-812, 377-100))

nx , ny = 975 , 811 #npc
dx , dy = 694 , 367 #地點
x1 , y1 = 821 , 391 #貨物
x2 , y2 = 1021 , 391
cx , cy = 1235 , 772 #出發
#gx , gy = cx , cy
dx2 , dy2 = 976 , 697
x3 , y3 = 821 , 432
ox , oy = 960 , 755 #結束
def talk_with_npc():
    global nx,ny
    sec = 0.05
    pydirectinput.click(nx,ny)
    time.sleep(sec)
    pydirectinput.press('down')
    time.sleep(0.05)
    for i in range(5):
        pydirectinput.press('b')
        time.sleep(0.05)
    pydirectinput.press('right')
    time.sleep(0.05)
    for i in range(2):
        pydirectinput.press('enter')
        time.sleep(0.05)
    
def attack(): #精靈遊俠
    sec = 0.4
    pydirectinput.press('left')
    pydirectinput.keyDown('a')
    time.sleep(sec)
    pydirectinput.keyUp('a')
    pydirectinput.press('right')
    pydirectinput.keyDown('a')
    time.sleep(sec)
    pydirectinput.keyUp('a')
    time.sleep(0.1)

    pydirectinput.press('space')
    pydirectinput.press('space')
    time.sleep(0.1)
    pydirectinput.keyDown('a')
    time.sleep(sec)
    pydirectinput.keyUp('a')
    pydirectinput.press('left')
    pydirectinput.keyDown('a')
    time.sleep(sec)
    pydirectinput.keyUp('a')
    time.sleep(0.1)
    pydirectinput.press('right')
    time.sleep(0.1)

    pydirectinput.press('space')
    pydirectinput.press('space')
    time.sleep(0.1)
    pydirectinput.keyDown('a')
    time.sleep(sec)
    pydirectinput.keyUp('a')
    time.sleep(0.1)
    pydirectinput.press('left')
    pydirectinput.keyDown('a')
    time.sleep(sec)
    pydirectinput.keyUp('a')
    time.sleep(0.1)

    pydirectinput.press('space')
    pydirectinput.press('space')
    time.sleep(0.1)
    pydirectinput.keyDown('a')
    time.sleep(sec)
    pydirectinput.keyUp('a')
    time.sleep(0.1)
    pydirectinput.press('right')
    pydirectinput.keyDown('a')
    time.sleep(sec)
    pydirectinput.keyUp('a')
    time.sleep(0.1)
    pydirectinput.press('left')
    time.sleep(0.1)
    pydirectinput.press('space')
    pydirectinput.press('space')

def attack2(): #夜光
    sec = 0.4
    rdi = random.randrange(0,100,1)%2
    if rdi == 1:
        skill = 'd'
    else:
        skill = 'w'
    pydirectinput.press('left')
    pydirectinput.keyDown(skill)
    time.sleep(sec)
    pydirectinput.keyUp(skill)
    time.sleep(sec)
    pydirectinput.press('right')
    pydirectinput.keyDown(skill)
    time.sleep(sec)
    pydirectinput.keyUp(skill)
    time.sleep(sec)

    pydirectinput.keyDown('right')
    pydirectinput.press('ctrl')
    pydirectinput.keyUp('right')
    time.sleep(0.1)
    pydirectinput.keyDown(skill)
    time.sleep(sec)
    pydirectinput.keyUp(skill)
    time.sleep(sec)
    pydirectinput.press('left')
    pydirectinput.keyDown(skill)
    time.sleep(sec)
    pydirectinput.keyUp(skill)
    time.sleep(sec)
    pydirectinput.press('right')
    time.sleep(0.1)

    pydirectinput.keyDown('right')
    pydirectinput.press('ctrl')
    pydirectinput.keyUp('right')
    time.sleep(0.1)
    pydirectinput.keyDown(skill)
    time.sleep(sec)
    pydirectinput.keyUp(skill)
    time.sleep(sec)
    pydirectinput.press('left')
    pydirectinput.keyDown(skill)
    time.sleep(sec)
    pydirectinput.keyUp(skill)
    time.sleep(sec)

    pydirectinput.keyDown('left')
    pydirectinput.press('ctrl')
    pydirectinput.keyUp('left')
    time.sleep(0.1)
    pydirectinput.keyDown(skill)
    time.sleep(sec)
    pydirectinput.keyUp(skill)
    time.sleep(sec)
    pydirectinput.press('right')
    pydirectinput.keyDown(skill)
    time.sleep(sec)
    pydirectinput.keyUp(skill)
    time.sleep(sec)
    pydirectinput.press('left')
    time.sleep(0.1)
    pydirectinput.keyDown('left')
    pydirectinput.press('ctrl')
    pydirectinput.keyUp('left')


if __name__ == "__main__":
    
    Attack = attack
    talk_with_npc()
    pydirectinput.click(dx,dy)
    pydirectinput.press('enter')
    pydirectinput.click(x1,y1)
    pydirectinput.click(x1,y1)
    pydirectinput.click(x2,y2)
    pydirectinput.click(x2,y2)
    for i in range(2):
        pydirectinput.click(cx,cy)
        pydirectinput.press('enter')
    while 1 :
        time.sleep(2)
        pos = pyautogui.locateOnScreen('./ScreenShots/clock.png')
        #print(pos)
        if pos != None:
            break
        Attack()
        for i in range(5):
            pydirectinput.click(ox,oy)
    
    talk_with_npc()
    pydirectinput.click(dx2,dy2)
    pydirectinput.press('enter')
    pydirectinput.click(x1,y1)
    pydirectinput.click(x1,y1)
    pydirectinput.click(x2,y2)
    pydirectinput.click(x3,y3)
    for i in range(2):
        pydirectinput.click(cx,cy)
        pydirectinput.press('enter')
    while 1 :
        time.sleep(2)
        pos = pyautogui.locateOnScreen('./ScreenShots/clock.png')
        #print(pos)
        if pos != None:
            break
        Attack()
        for i in range(5):
            pydirectinput.click(ox,oy)
    
    for t in range(6):
        talk_with_npc()
        pydirectinput.click(dx2,dy2)
        pydirectinput.press('enter')
        for i in range(4):
            pydirectinput.click(x1,y1)
        
        for i in range(2):
            pydirectinput.click(cx,cy)
            pydirectinput.press('enter')
        
        while 1 :
            time.sleep(2)
            pos = pyautogui.locateOnScreen('./ScreenShots/clock.png')
            #print(pos)
            if pos != None:
                break
            Attack()
            for i in range(5):
                pydirectinput.click(ox,oy)
    '''
    while 1:
        Attack()
    '''
    
