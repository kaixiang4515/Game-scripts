# -*- coding:utf-8 -*-
import pyautogui
import time

ox , oy = pyautogui.position()
while 1:
    if (ox,oy) != pyautogui.position():
        ox, oy = pyautogui.position()
        print(ox, oy)