import pyautogui as p
import time
import os

while True:
    if p.locateCenterOnScreen("closeTvWindow.png", grayscale=True):
        x, y = p.locateCenterOnScreen("closeTvOk", grayscale=True)
        p.moveTo(x, y, 1)
        p.click()
        time.sleep(3600)