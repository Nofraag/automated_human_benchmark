import easyocr
import keyboard
import numpy as np
from PIL import ImageGrab
from pynput.mouse import Controller

reader = easyocr.Reader(['en'])
result = None

cached_corner = None
corners = None 
mouse = Controller()
pressed = False
while True: 

    if corners == None:
        if keyboard.is_pressed("ctrl") and pressed != True:
            if cached_corner == None:
                cached_corner = mouse.position
            else:
                corners = [cached_corner, [mouse.position[0], cached_corner[1]], [cached_corner[0], mouse.position[1]], [mouse.position[0], mouse.position[1]]]
            pressed = True
        elif not keyboard.is_pressed("ctrl"):
            pressed = False

        print("CTRL on the top left corner" if cached_corner is None else "CTRL on the bottom right corner")
        continue

    if keyboard.is_pressed("alt"):
        continue

    if result == None:
        img = ImageGrab.grab(bbox=(corners[0][0], corners[1][1], corners[3][0], corners[3][1]))
        result = reader.readtext(np.array(img), detail = 0)
        result = " ".join(result)
        str.removeprefix(result, "I")
        print(result)
        
    for key in result:
        keyboard.press_and_release(key)
    
    break 


