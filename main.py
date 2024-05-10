import pygame


from menu import menu
from gameplay import gameplay
from option import Option
from pygame.locals import*

import sys



pygame.init()
#fenetre du jeux
w, h = pygame.display.Info().current_w,pygame.display.Info().current_h
pygame.display.set_caption("Wurmys le jeu")
logo = pygame.image.load('ui/logo.png')
pygame.display.set_icon(logo)
screen = pygame.display.set_mode((w,h),pygame.RESIZABLE)
mode = 1 # défini le stade du jeu (quitter le jeu = 0, Menu = 1, Jeu = 2)
option = Option()
while mode>0:
    if mode == 1:

        mode=menu(option)

    if mode == 2:
        mode=gameplay(option)






pygame.quit()
    
