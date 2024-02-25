import pygame
import pygame_menu
import pyautogui
import os
from ping_pong import *
pygame.init()
sw = 600
sh = 500
window = pygame.display.set_mode((sw,sh))
font = pygame_menu.font.FONT_8BIT
mytheme = pygame_menu.Theme(widget_font=font,background_color=(3,45,123,0),
                                title_background_color = (255,255,255))
def start():

    
    starting()
    

    
def end():
    pygame_menu,exit()

def help():
    
    help_main = pygame_menu.Menu("Main menu",sw,sh,theme=mytheme)
    def returnen():
        main.enable()
        help_main.disable()
    help_main.add.button("Exit",end)
    help_main.add.button("return",returnen)
    main.disable()
    help_main.mainloop(window)
    

main = pygame_menu.Menu("Main menu",sw,sh,theme=pygame_menu.themes.THEME_DARK.copy())
main.add.button("Запустити гру",start)
main.add.button("Зупинити гру",end)
main.add.button("help",help)
main.mainloop(window)



