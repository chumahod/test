import pyautogui as p
for i in range(10):
    print(i, end='\t')
    print("mouse position: ", p.position())
    try:
        x, y = p.locateCenterOnScreen("food.png", grayscale=True )
        print("hand find")
        p.moveTo(x, y, 1)
        print("mouse move to point", x, y)
        p.click(interval=0.2)
    except:
        print("not find")