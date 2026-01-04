import pygame as py
import keyboard as key
import sys
import config

py.init()
screen = py.display.set_mode((450,450))
py.display.set_caption('Choose Guns CS1.6')
time = py.time.Clock()
text = py.font.Font(None,20)
text_2 = py.font.Font(None,20)
text_3 = py.font.Font(None,20)
text_surface = text.render(f"Presiona 0 para {config.tecla_1}",True,"white")
text_surface_2 = text_2.render(f"Presiona 9 para {config.tecla_2}",True,"white")
text_surface_3 = text_3.render(f"Presiona 8 para {config.tecla_3}",True,"white")
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
    screen.blit(text_surface,(50,100))
    screen.blit(text_surface_2,(50,200))
    screen.blit(text_surface_3,(50,300))
    py.display.flip()
    time.tick(60)

py.quit()
