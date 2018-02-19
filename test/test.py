import pyautogui as p
for i in range(10):
    print(i, end='\t')
    print("mouse position: ", p.position())
    try:
        print("try")
        x, y = p.locateCenterOnScreen('1.png', grayscale=True)
        p.moveTo(x, y, 1)
 #       print("mouse move to point", x, y)

    except:
        print("none")