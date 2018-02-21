import pyautogui as p
import time
import os

for i in range(5):
    if p.locateCenterOnScreen("closeTvWindow.png", grayscale=True):
        x, y = p.locateCenterOnScreen("closeTvOk", grayscale=True)
        p.moveTo(x, y, 1)
        p.click()
        time.sleep(3600)
    else:
        print("где окно?")