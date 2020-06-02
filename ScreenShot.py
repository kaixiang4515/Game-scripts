# -*- coding:utf-8 -*-
import pyautogui
import time

for i in range(3,-1,-1):
    print(i)
    time.sleep(1)

img = pyautogui.screenshot('./ScreenShots/test.png', region=(647, 451, 771-647, 565-451))