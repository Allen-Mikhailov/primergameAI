import pyautogui as gui
import pynput 
from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener
from PIL import Image
import pytesseract
from time import sleep

exiting = False
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\allenmik\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

mouseX, mouseY = 0, 0

headsbox1X, headsbox1Y = 0, 0
headsbox2X, headsbox2Y = 0, 0

flipboxX, flipboxY = 0, 0

cheaterboxX, cheaterboxY = 0, 0
fairboxX, fairboxY = 0, 0

def getText(image_path):
    # Opening the image & storing it in an image object
    img = Image.open(image_path)
    
    # Providing the tesseract executable
    # location to pytesseract library
    # pytesseract.tesseract_cmd = path_to_tesseract
    
    return pytesseract.image_to_string(img, lang='eng',
           config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')

def exit():
    if exiting:
        quit()

checking = 0
mouse = pynput.mouse.Controller()
def loop():

    print(headsbox1X, headsbox1Y)
    print(headsbox2X, headsbox2Y)

    exit()

    # flipping
    mouse.position = (flipboxX, flipboxY)
    sleep(1)
    mouse.click(pynput.mouse.Button.left)
    sleep(1)
    mouse.click(pynput.mouse.Button.left)

    exit()

    sleep(1)

    # reading heads
    gui.screenshot("head.png", region=(headsbox1X,headsbox1Y, headsbox2X-headsbox1X, headsbox2Y- headsbox1Y))
    heads = int(getText("head.png") or "5") or 5

    if heads > 6:
        mouse.position = (cheaterboxX, cheaterboxY)
    else:
        mouse.position = (fairboxX, fairboxY)
    sleep(.5)
    mouse.click(pynput.mouse.Button.left)

    sleep(3)


# im = pyautogui.screenshot(region=(0,0, 300, 400))

def on_move(x, y):
    global mouseX, mouseY

    mouseX = x 
    mouseY = y

# Collect events until released
ml = MouseListener(
        on_move=on_move)
ml.start()

def OnPress(key):
    global exiting
    global checking
    global tailsbox1X, tailsbox1Y
    global tailsbox2X, tailsbox2Y
    global headsbox1X, headsbox1Y
    global headsbox2X, headsbox2Y
    global cheaterboxX, cheaterboxY
    global fairboxX, fairboxY
    global flipboxX, flipboxY

    # try:
    k = '{0}'.format(key)
    if (k == "'s'"):
        if checking == 0:
            headsbox1X, headsbox1Y = mouseX, mouseY
        elif checking == 1:
            headsbox2X, headsbox2Y = mouseX, mouseY
        elif checking == 2:
            cheaterboxX, cheaterboxY = mouseX, mouseY
        elif checking == 3:
            fairboxX, fairboxY = mouseX, mouseY
        elif checking == 4:
            flipboxX, flipboxY = mouseX, mouseY
        checking = ( checking + 1 ) % 5
    elif (k == "'l'"):
        print("Loop started")
        while True:
            loop()

    elif (k == "'\\x03'"):
        exiting = True
        quit()
    # except:
    #     print("error")
    #     pass


kl = KeyboardListener(on_press=OnPress)
kl.start()
kl.join()