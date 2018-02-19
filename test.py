import pyautogui as p
import os
import time
import logging

logging.basicConfig(
    level=logging.INFO,
    format=(u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s')
    )

def closeBtn():
    """ Нажимаем кнопку закрыть """
    logging.info("closeBtn start")
    os.chdir('c:/lod/img/close')
    l = os.listdir('c:/lod/img/close')
    for pic in l:
        try:
            x, y = p.locateCenterOnScreen(pic, grayscale=True)
        except:
            logging.info("close btn not find")
        else:
            logging.info("close btn find")
            p.moveTo(x, y, 1)
            logging.info("mouse move to point", x, y)
            p.click(interval=0.3)
            time.sleep(2)
    logging.info("closeBtn finish")

def shelterIn():
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

def shelterOut():
    logging.info("shelterOut start")
    p.moveTo(445, 79, 1)
    p.click(interval=0.3)
    p.moveTo(594, 162, 1)
    p.click(interval=0.3)
    logging.info("shelterOut finish")

def shelter():
    logging.info("shelter start")
    os.chdir('c:/lod/img/shelter')
    p.moveTo(445, 79, 1)
    p.click(interval=0.3)
    time.sleep(1)
    coord = p.locateCenterOnScreen("sh.png", grayscale=True)
    if coord:
        logging.info("find")
        shelterIn()
    else:
        logging.info("not find")
        shelterOut()
        time.sleep(2)
        p.moveTo(445, 79, 1)
        p.click(interval=0.3)
        time.sleep(1)
        shelterIn()
    time.sleep(2)
    logging.info("shelter finish")

if __name__ == '__main__':
    time.sleep(2)
    for i in range(2):
        shelter()
        print("wait 60 min")
        time.sleep(5)
    print("well done")



