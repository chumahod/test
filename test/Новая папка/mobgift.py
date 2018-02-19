import pyautogui as p
from time import sleep
for i in range(38):
    print(i, end='\t')
    print("mouse position: ", p.position())
    try:
        x, y = p.locateCenterOnScreen("open.png", grayscale=True)
        print("hand find")
        p.moveTo(x, y, 1)
        print("mouse move to point", x, y)
        p.click(interval=0.1)
        sleep(0.5)
        p.click(interval=0.1)
        sleep(2)
    except:
        print("not find")