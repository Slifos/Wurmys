import pygame
from Inventaire import Inventaire
from Projetcile import *
from menu import menu
from gameplay import gameplay
from pygame.locals import*
from son import play_music, play_sound
import sys



pygame.init()
#fenetre du jeux
w, h = pygame.display.Info().current_w,pygame.display.Info().current_h
pygame.display.set_caption("Wurmys le jeu")
screen = pygame.display.set_mode((w,h),pygame.RESIZABLE)
mode = 1 # défini le stade du jeu (quitter le jeu = 0, Menu = 1, Jeu = 2)
while mode>0:
    if mode == 1:
        mode=menu()
    if mode == 2:
        mode=gameplay() 





pygame.quit()
    
