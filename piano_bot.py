from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con



# Tile 1 Position: X:  731 Y:  526 RGB: ( 51,  63, 58)
# Tile 2 Position: X:  828 Y:  526 RGB: (  65,   184,   65)
# Tile 3 Position: X:  937 Y:  526 RGB: ( 66,  188, 69)
# Tile 4 Position: X:  1028 Y:  526 RGB: ( 59,  189, 55)

time.sleep(2)

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.1)  # This pauses the script for 0.1 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    
while keyboard.is_pressed('q') == False:
    if pyautogui.pixel(731, 705)[0] in range(40, 55):
        click(731, 705)
    if pyautogui.pixel(828, 705)[0] in range(40, 55):
        click(828, 705)
    if pyautogui.pixel(937, 705)[0] in range(40, 55):
        click(937, 705)
    if pyautogui.pixel(1030, 705)[0] in range(40, 55):
        click(1028, 705)






