import pygame
from pygame.locals import *

from Inventaire import Inventaire
from Projetcile import *
from son import *
from player import Player
from Pause import pause
#Representation du jeu
pygame.init()
def gameplay():

    #initialise le jeu
    w, h = pygame.display.Info().current_w, pygame.display.Info().current_h
    screen = pygame.display.set_mode((w, h), pygame.RESIZABLE)
    background = pygame.image.load('bg/bg_game.jpg')
    background = pygame.transform.scale(background, (w,h))#initialise le fond en fonction des dimensions de l'écran (16:9 de préférence)
    play_music("sound/game_theme.mp3")#joue le thème du jeu

    # initialise les joueurs
    player1 = Player("A",w,h)
    player1.update_setting(w,h)#permets aux joueurs de changer ses settings
    #initialise les touches du joueur1
    K_player1 = {"left": pygame.K_q, "right": pygame.K_d, "up": pygame.K_z}
    mode = 2 #lancement du jeu

    inventaire = Inventaire()
    fps= pygame.time.Clock()
    pygame.mouse.set_visible(False)
    while mode>=2:
        player1.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_BACKSPACE:
                    mode = pause(screen)
        keys = pygame.key.get_pressed()




        #déplacement du joueur 1
        if keys[K_player1["left"]]:#détecte si il va à gauche
            player1.move_left()
        if keys[K_player1["right"]]:#détecte si il va à droite
            player1.move_right()
        if keys[K_player1["up"]]:#détecte le jump
            player1.do_jump()
        player1.in_aire() #calcule sa trajectoire si il est dans les aires
        #implémente ces différentes actions sur l'écran










        #optimise  le nombre d'images par seconde
        fps.tick(60)
        #mets à jour l'écran
        screen.blit(background, (0, 0))
        screen.blit(player1.image, (player1.rect_x, player1.rect_y))
        player1.update_health_bar( screen)


        pygame.display.flip()


    if mode == -1: #restart le jeu avec un appel réccursif
        mode=gameplay()
    return mode

gameplay()
