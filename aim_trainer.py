import ctypes

import keyboard
from pynput.mouse import Button, Controller

import images_tils

corners = None 
user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

pressed = False
cached_corner = None
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

    if keyboard.is_pressed("b"):
        continue


    pos = images_tils.find_color_on_screen((149, 195, 232), corners)  
    if pos != None:
        mouse.position = pos
        mouse.click(Button.left, 1)
