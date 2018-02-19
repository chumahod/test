import pyautogui as p
import time
#p.screenshot('img.png', region=(0, 0, 800, 520))
time.sleep(2)
for i in range(3):

    print(p.position())
    time.sleep(3)