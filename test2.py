import pyautogui as p
import os
import time
import logging

logging.basicConfig(
    level=logging.INFO,
    format=(u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s')
)

def noxMove():
    ''' перемещаем nox в угол экрана'''
    logging.info("noxMove start")
    os.chdir('c:/lod/img/nox')
    try:
        x, y = p.locateCenterOnScreen("nox_window.png", grayscale=True)
    except:
        logging.info("nox_window find")
    else:
        logging.info("nox_window find")
        p.moveTo(x, y, 1)
        logging.info("mouse move to point")
        p.mouseDown()
        p.moveTo(15, 5, 1)
        p.mouseUp()
    logging.info("noxMove finish")

def shieldEnable():
    logging.info("shieldEnable start")
    os.chdir('img/shield')
    x, y = 773, 198
    p.moveTo(x, y, 0.3)
    p.click(interval=0.2)
    time.sleep(1)
    if (p.locateCenterOnScreen("turfBoostsWindow.png")):
        x, y = p.locateCenterOnScreen("turfBoostsWindow.png", grayscale=True)
        p.moveTo(x, y, 0.3)
        print(x, y)
        if (p.locateCenterOnScreen("turfBoostsShieldIcon.png")):
            x, y = p.locateCenterOnScreen("turfBoostsShieldIcon.png", grayscale=True)
            p.moveTo(x, y, 0.3)
            p.moveTo(624, y, 0.2)
            p.click(interval=0.2)
            time.sleep(1)
            if (p.locateCenterOnScreen("turfBoostsShieldIcon2.png")):
                x, y = p.locateCenterOnScreen("turfBoostsShieldIcon2.png", grayscale=True)
                p.moveTo(x, y, 0.3)
                p.moveTo(624, y, 0.2)
                p.click(interval=0.2)
            else:
                p.press('esc')
                return print('shield enable2')
        else:
            p.press('esc')
            return print('shield enable')

    else:
        p.press('esc')
        return print('turfBoostsWindow not find')

if __name__ == "__main__":
    #noxMove()
    shieldEnable()