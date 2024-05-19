import pygame


from menu import menu
from gameplay import gameplay
from option import Option
from fonction import*




"""fichier qui permet de lancer le jeu"""

pygame.init()
#fenetre du jeux
w, h = pygame.display.Info().current_w,pygame.display.Info().current_h
pygame.display.set_caption("Wurmys: The battle of worms")
logo = pygame.image.load('ui/logo.png')
pygame.display.set_icon(logo)
screen = pygame.display.set_mode((w,h),pygame.RESIZABLE)
mode = 1 # défini le stade du jeu (quitter le jeu = 0, Menu = 1, Jeu = 2)
option = Option()
play_music("sound/theme.mp3", option)
while mode>0:
    """interchange entre le menu et le jeu en fonction des inputs du joueur"""
    if mode == 1:
        mode=menu(option)

    if mode == 10:
        mode=gameplay(option)
        play_music("sound/theme.mp3", option)






pygame.quit()
    
