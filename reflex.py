
import keyboard
from PIL import ImageGrab
from pynput.mouse import Button, Controller

import images_tils

pressed = False
cached_corner = None
corners = None 
mouse = Controller()
while True:
    if corners == None:
            if keyboard.is_pressed('ctrl') and pressed != True:
                if cached_corner == None:
                    cached_corner = mouse.position
                else:
                    corners = [cached_corner, [mouse.position[0], cached_corner[1]], [cached_corner[0], mouse.position[1]], [mouse.position[0], mouse.position[1]]]
                pressed = True
            elif not keyboard.is_pressed('ctrl'):
                pressed = False
    
            print("CTRL on the top left corner" if cached_corner is None else "CTRL on the bottom right corner")
            continue

    px = ImageGrab.grab().load()
    pos = images_tils.find_color_on_screen(px, (75, 219, 106), corners)
    if pos != None:
        mouse.position = pos
        mouse.click(Button.left, 1)
