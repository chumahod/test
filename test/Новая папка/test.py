import pyautogui as p
for i in range(3):
    print(i, end='\t')
    print("mouse position: ", p.position())
    try:
        print("try")
        x, y = p.locateCenterOnScreen('close.png')
        p.moveTo(x, y, 1)
        p.click(interval=0.2)

    except:
        print("none")