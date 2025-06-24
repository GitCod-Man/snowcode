from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con


import pyscreeze
pyscreeze.USE_IMAGE_NOT_FOUND_EXCEPTION = False  # 关闭异常，改为返回None

while 1:
    if pyautogui.locateOnScreen('dog.png', region=(0,0,1920,1080), grayscale=True, confidence=0.7) != None:
        print("find dog image")
        time.sleep(0.5)
      
    else:
        print("could not find dog image")
        time.sleep(0.5)