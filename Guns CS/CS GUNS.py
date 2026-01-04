import pygame as py
import keyboard as key
import sys
import config

py.init()
screen = py.display.set_mode((450,450))
py.display.set_caption('Choose Guns CS1.6')
time = py.time.Clock()
running = True
while running:
    for event in py.event.get():
        if event.type==py.QUIT:
            running = False
            sys.exit

    lista = config.tecla_1
    lista_2 = config.tecla_2
    lista_3 = config.tecla_3
    if key.is_pressed('+'):
        running = False
        sys.exit
    if key.is_pressed('0'):
        for tecla in lista:
            for buy in tecla:
                key.press_and_release(buy)
                py.time.delay(160)
    if key.is_pressed('9'):
        for tecla in lista_2:
            for buy in tecla:
                key.press_and_release(buy)
                py.time.delay(160)



    if key.is_pressed('8'):
        for tecla in lista_3:
            for buy in tecla:
                key.press_and_release(buy)
                py.time.delay(160)
    screen.fill(('black'))
    py.display.flip()
    time.tick(60)

py.quit()