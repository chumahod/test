import pyautogui as p
import os
import time
import logging

t_wait = 5
# изменить  логи#
logging.basicConfig(
    level=logging.INFO,
    format=(u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s')
    )

def closeBtn():
    """ Нажимаем кнопку закрыть """
    logging.info("closeBtn start")
    os.chdir('img/close')
    l = os.listdir('img/close')
    for pic in l:
        try:
            x, y = p.locateCenterOnScreen(pic, grayscale=True, region=(0,0, 800, 490))
        except:
            logging.info("close btn not find")
        else:
            logging.info("close btn find")
            p.moveTo(x, y, 1)
            logging.info("mouse move to point", x, y)
            p.click(interval=0.3)
            time.sleep(2)
    logging.info("closeBtn finish")

def sendRss():
    # отправляем ресы
    pass

def onMap():
    # переключаемся на карту

def onCastle():
    # переключаемся в замок

def shieldEnable():
    if !(p.locateOnScreen("shield.png", region(750, 160, 0, 0)), grayscale=True):
        # запускаем щит
    else:
        loggin.info("shield enable")

if __name__ == '__main__':
    time.sleep(2)
    for i in range(2):
        shelter()
        print("wait ", t_wait, " sec")
        print("wait ", t_wait/60, " min")
        time.sleep(t_wait)
    print("well done")



