import pyautogui as p
import os
import time
import logging
# изменить  логи#
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

def questBtn():
    logging.info("questBtn start")
    p.moveTo(491, 465, 1)
    p.click(interval=0.3)
    time.sleep(1)
    logging.info("questBtn finish")

def vipQuest():
    ''' открываем квесты дня '''
    logging.info("adminQuest start")
    questBtn()
    p.moveTo(362, 122, 1)
    p.click(interval=0.3)
    time.sleep(1)
    questChest()
    closeBtn()
    logging.info("adminQuest finish")

if __name__ == '__main__':
    time.sleep(2)
    for i in range(2):
        shelter()
        print("wait 60 min")
        time.sleep(5)
    print("well done")



