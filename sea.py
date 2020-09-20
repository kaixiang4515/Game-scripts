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

def buff(t = 1):
    global t_120,t_180,t_200,t_90,t_900
    tn = time.time()
    if tn - t_900 >= 900*0.8 :
        pydirectinput.press('1')
        time.sleep(1)
        t_900 = tn

    if t == 1 :
        if tn - t_180 >= 180*0.8 :
            pydirectinput.press('3')
            time.sleep(3)
            pydirectinput.press('4')
            time.sleep(2)
            pydirectinput.press('0')
            time.sleep(1)
            pydirectinput.press('ctrl')
            time.sleep(1)
            pydirectinput.press('j')
            time.sleep(1)
            t_180 = tn
        if tn - t_120 >= 120:
            pydirectinput.press('6')
            time.sleep(1)
            t_120 = tn

    elif t == 2:
        if tn - t_200 >= 200*0.8 :
            pydirectinput.press('3')
            time.sleep(3)
            t_200 = tn
        if tn - t_120 >= 120 :
            pydirectinput.press('2')
            time.sleep(1)
            t_120 = tn
        if tn - t_90 >= 90 :
            pydirectinput.press('5')
            time.sleep(1)
            t_90 = tn

def move(t = 1, d = 'right'):
    if t == 1 : key = 'alt' #順移
    elif t == 2 : key = 'space' #二段跳
    elif t == 3 : key = d #兩下方向鍵

    pydirectinput.press(d)
    time.sleep(0.1)
    if t == 1:
        pydirectinput.keyDown(d)
        pydirectinput.press(key)
        pydirectinput.keyUp(d)
    elif t == 2 or t == 3:
        pydirectinput.press(key)
        pydirectinput.press(key)

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
    
def attack2(): #精靈遊俠
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

    move(t=2)
    time.sleep(0.1)
    pydirectinput.keyDown('a')
    time.sleep(sec)
    pydirectinput.keyUp('a')
    pydirectinput.press('left')
    pydirectinput.keyDown('a')
    time.sleep(sec)
    pydirectinput.keyUp('a')
    time.sleep(0.1)

    move(t=2)
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

    move(t=2,d='left')
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
    move(t=2,d='left')

def attack1(): #夜光
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

    move()
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

    move()
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

    move(d='left')
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
    move(d='left')

if __name__ == "__main__":
    
    tj = 1
    if tj == 1 : Attack = attack1
    elif tj == 2 : Attack = attack2

    t_900 = 0
    t_200 = t_900 ; t_180 = t_900 ; t_120 = t_900 ; t_90 = t_900
    buff(tj)

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
        buff(tj)
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
        buff(tj)
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
            buff(tj)
            Attack()
            for i in range(5):
                pydirectinput.click(ox,oy)
    '''
    while 1:
        Attack()
    '''
    
