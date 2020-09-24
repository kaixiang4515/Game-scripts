# -*- coding:utf-8 -*-
import pyautogui
import pydirectinput
import time

def f(t):
    for x in range(t):
        sec = 0.01  #間隔秒數
        pydirectinput.press('b')
        #time.sleep(sec)
        for i in range(3):
            pydirectinput.press('down')
            #time.sleep(sec)
        
        for i in range(2):
            pydirectinput.press('b')
            #time.sleep(sec)
        
        pydirectinput.press('down')
        #time.sleep(sec)
        pydirectinput.press('b')
        #time.sleep(sec)
        pydirectinput.press('1')
        #time.sleep(sec)
        pydirectinput.press('0')
        #time.sleep(sec)
        pydirectinput.press('0')
        #time.sleep(sec)
        pydirectinput.press('enter')
        pydirectinput.press('right')
        pydirectinput.press('enter')
        pydirectinput.press('enter')


if __name__ == "__main__":
    t = input('幾次:')

    for i in range(3,-1,-1): #倒數開始
        print(i)
        time.sleep(1)
    
    f(int(t))