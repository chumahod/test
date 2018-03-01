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

def helpGuild():
    logging.info("helpGuild start")
    os.chdir('c:/lod/img/help')
    try:
        x, y = p.locateCenterOnScreen("help_guild.png", grayscale=True)
    except:
        logging.info("helpGuild not find")
    else:
        logging.info("helpGuild find")
        p.moveTo(x, y, 1)
        logging.info("mouse move to point")
        p.click(interval=0.3)
        time.sleep(2)
        p.moveTo(384, 472, 1)
        p.click(interval=0.3)
        time.sleep(2)
        p.moveTo(757, 72, 1)
        p.click(interval=0.3)
        closeBtn()
    logging.info("helpGuild finish")

def huntChest():
    logging.info("huntChestOpen start")
    os.chdir('c:/lod/img/hunt')
    p.moveTo(346, 474, 1) # open menu
    p.click()
    time.sleep(2)
    p.moveTo(581, 210, 1)   # open chest menu
    p.click()
    time.sleep(2)
    for i in range(10):
        try:
            x, y = p.locateCenterOnScreen("huntchestopen.png", grayscale=True)
        except:
            logging.info("close btn not find")

        else:
            logging.info("close btn find")
            logging.info("mouse move to point")
            p.moveTo(602, 120, 1)
            p.click()
            p.moveTo(622, 198, 1)
            p.click()
            p.moveTo(610, 265, 1)
            p.click()
            p.moveTo(631, 348, 1)
            p.click()
            p.moveTo(614, 421, 1)
            p.click()
            p.moveTo(618, 487, 1)
            p.click()
            p.moveTo(602, 120, 1)
            p.click()
            time.sleep(2)
    closeBtn()
    time.sleep(1)
    closeBtn()
    time.sleep(1)
    logging.info("huntChestOpen finish")

def chestOpen():
    '''открываем тайнственные коробки'''
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

def vipChestOpen():
    logging.info("vipChestOpen start")
    questBtn()
    p.moveTo(562, 122, 1)
    p.click(interval=0.3)
    time.sleep(2)
    p.moveTo(240, 285, 1)
    p.click(interval=0.3)
    time.sleep(1)
    p.moveTo(388, 265, 1)
    p.click(interval=0.3)
    time.sleep(1)
    p.moveTo(566, 258, 1)
    p.click(interval=0.3)
    time.sleep(1)
    p.moveTo(227, 368, 1)
    p.click(interval=0.3)
    time.sleep(1)
    p.moveTo(391, 371, 1)
    p.click(interval=0.3)
    time.sleep(1)
    p.moveTo(580, 369, 1)
    p.click(interval=0.3)
    time.sleep(1)
    closeBtn()
    logging.info("vipChestOpen finish")

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

def changeAcc(twink):
    logging.info("changeAcc start")
    os.chdir('c:/lod/img/lm')
    if p.locateCenterOnScreen("other.png"):
        x, y = p.locateCenterOnScreen("other.png", grayscale=True)
        p.moveTo(x, y, 1)
        p.click()
        time.sleep(1)
        if p.locateCenterOnScreen("account.png"):
            x, y = p.locateCenterOnScreen("account.png", grayscale=True)
            p.moveTo(x, y, 1)
            p.click()
            time.sleep(1)
            if p.locateCenterOnScreen("switchaccount.png"):
                x, y = p.locateCenterOnScreen("switchaccount.png", grayscale=True)
                p.moveTo(x, y, 1)
                p.click()
                time.sleep(1)
                if p.locateCenterOnScreen("signin.png"):
                    x, y = p.locateCenterOnScreen("signin.png", grayscale=True)
                    p.moveTo(x, y, 1)
                    p.click()
                    time.sleep(3)
                    os.chdir('c:/lod/img/account')
                    print(twink)
                    if twink == "gam_balin":
                        x, y = p.locateCenterOnScreen("gam_balin.png", grayscale=True)
                        p.moveTo(x, y, 1)
                        p.click()
                        time.sleep(1)
                    elif twink == "brouk_baraka":
                        x, y = p.locateCenterOnScreen("brouk_baraka.png", grayscale=True)
                        p.moveTo(x, y, 1)
                        p.click()
                        time.sleep(1)
                    elif twink == "js_trump":
                        x, y = p.locateCenterOnScreen("js_trump.png", grayscale=True)
                        p.moveTo(x, y, 1)
                        p.click()
                        time.sleep(1)

                    if p.locateCenterOnScreen("change_acc_ok.png"):
                        x, y = p.locateCenterOnScreen("change_acc_ok.png", grayscale=True)
                        p.moveTo(x, y, 1)
                        p.click()
                        time.sleep(5)

                    if p.locateCenterOnScreen("change_acc_confirm.png"):
                        x, y = p.locateCenterOnScreen("change_acc_confirm.png", grayscale=True)
                        p.moveTo(x, y, 1)
                        p.click()
                        time.sleep(3)

                    if p.locateCenterOnScreen("change_acc_close.png"):
                        x, y = p.locateCenterOnScreen("change_acc_close.png", grayscale=True)
                        p.moveTo(x, y, 1)
                        p.click()
                        time.sleep(3)

if __name__ == '__main__':
    time.sleep(6)
    noxStart()
    accounts = ["js_trump", "brouk_baraka", "gam_balin"]
    for i in range(240):
        for account in accounts:
            lmStart()
            noxMove()
            chestOpen()
            shelter()
            helpGuild()
            huntChest()
            adminQuest()
            guildQuest()
            vipChestOpen()
            chestOpen()
            changeAcc(account)

        logging.info("wait 60 min")
        time.sleep(60)
    logging.info("well done")



