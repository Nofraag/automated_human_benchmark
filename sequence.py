import time

import keyboard
import numpy
from PIL import ImageGrab
from pynput.mouse import Button, Controller

import images_tils

steps = []
current_steps = []
steps_amount = 0
pressed = False
last_step = None
cached_corner = None
corners = None 
mouse = Controller()
started = False
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
        steps_amount = 0
        steps.clear()
        started = True
        continue

    if keyboard.is_pressed("alt"):
        break

    if not started:
        continue

    px = ImageGrab.grab().load()
    pos = images_tils.find_color_on_screen(px, (255,255,255), corners)
    to_remove =[]
    for step in current_steps:
        if px[step] == (37, 115, 193):
            to_remove.append(step)

    for removable in to_remove:
        current_steps.remove(removable)

    if len(steps) >= steps_amount and len(current_steps) == 0:
        for step in steps:
            mouse.position = step
            time.sleep(0.05)
            mouse.click(Button.left, 1)
            time.sleep(0.08)
        steps.clear()
        steps_amount += 1
    elif len(steps) < steps_amount and pos != None:
        append = True
        for step in current_steps:
            if numpy.abs(pos[0] - step[0]) < 40 or numpy.abs(pos[1] - step[1]) < 40:
                append = False

        if append:
            steps.append(pos)
            current_steps.append(pos)