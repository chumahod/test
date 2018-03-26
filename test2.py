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
    changeAcc("brouk_baraka")
    logging.info("well done")



