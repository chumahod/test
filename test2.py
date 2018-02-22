import pyautogui as p
import os
import time
import logging

logging.basicConfig(
    level=logging.INFO,
    format=(u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s')
)

def noxStart():
    """ запускаем nox с рабочего стола """
    logging.info("noxStart start")
    os.chdir('img/nox')
    try:
        x, y = p.locateCenterOnScreen("nox_shortcut.png", grayscale=True)
    except:
        logging.info("nox shortcut not find")
    else:
        logging.info("nox shortcut find")
        p.moveTo(x, y, 1)
        logging.info("mouse move to point")
        p.doubleClick(interval=0.3)
        time.sleep(30)
    logging.info("noxStart finish")

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

def lmStart():
    ''' Запускаем LM'''
    logging.info("lmStart start")
    os.chdir('c:/lod/img/lm')
    try:
        x, y = p.locateCenterOnScreen("lm_start.png", grayscale=True)
    except:
        logging.info("lm shortcut no find")
    else:
        logging.info("lm shortcut find")
        p.moveTo(x, y, 1)
        logging.info("mouse move to point")
        p.click(interval=0.3)
        time.sleep(40)
    i = 0
    for i in range(3):
        closeBtn()
        time.sleep(3)
        i += 1
    logging.info("lmStart finish")

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
            logging.info("mouse move to point")
            p.click(interval=0.3)
            time.sleep(2)
    logging.info("closeBtn finish")

def chestOpen():
    logging.info("chestOpen start")
    p.moveTo(686, 387, 1)
    p.click()
    time.sleep(1)
    p.moveTo(432, 350, 1)
    p.click(interval=0.2)
    time.sleep(2)
    logging.info("chestOpen finish")

def questBtn():
    logging.info("questBtn start")
    p.moveTo(491, 465, 1)
    p.click(interval=0.3)
    time.sleep(1)
    logging.info("questBtn finish")

def vipChestOpen():
    logging.info("vipChestOpen start")
    questBtn()
    p.moveTo(562, 122, 1)
    p.click(interval=0.3)
    time.sleep(1)
    logging.info("vipChestOpen finish")

def adminQuest():
    ''' открываем квесты дня '''
    logging.info("adminQuest start")
    questBtn()
    p.moveTo(362, 122, 1)
    p.click(interval=0.3)
    time.sleep(1)
    questChest()
    closeBtn()
    logging.info("adminQuest finish")

def guildQuest():
    ''' открываем квесты гильдии '''
    logging.info("guildChest start")
    questBtn()
    p.moveTo(503, 122, 1)
    p.click(interval=0.3)
    time.sleep(1)
    questChest()
    closeBtn()
    logging.info("guildChest finish")

def questChest():
    ''' открываем сундуки '''
    logging.info("questChest start")
    p.moveTo(648, 223, 1)
    for i in range(10):
        p.click(interval=0.3)
        time.sleep(2)
    logging.info("questChest finish")


if __name__ == '__main__':
    time.sleep(6)
    noxStart()
    accounts = ["js_trump", "brouk_baraka", "gam_balin"]
    for i in range(1):
        for account in accounts:
            lmStart()
            noxMove()
        logging.info("wait 60 min")
        time.sleep(3600)
    logging.info("well done")



