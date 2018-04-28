import pyautogui as p
import os
import time
import logging

logging.basicConfig(
    level=logging.INFO,
    format=(u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s')
)

logging.info("shelterIn start")
p.moveTo(456, 350, 1)
p.click(interval=0.3)
p.moveTo(443, 396, 1)
p.click(interval=0.3)
p.moveTo(609, 407, 1)
p.click(interval=0.3)
time.sleep(3)
if p.locateCenterOnScreen("c:/lod/img/close/close1.png"):
    closeBtn()
    time.sleep(2)
    if p.locateCenterOnScreen("c:/lod/img/close/close2.png"):
        x, y = p.locateCenterOnScreen("c:/lod/img/close/close1.png")
        p.moveTo(x, y, 1)
        p.click()
        time.sleep(1)
logging.info("shelterIn finish")