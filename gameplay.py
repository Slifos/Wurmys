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
    # initialise le fond en fonction des dimensions de l'écran (16:9 de préférence)
    background = pygame.transform.scale(background, (w,h))
    play_music("sound/game_theme.mp3")

    set_touche1 = {"left": pygame.K_q, "right": pygame.K_d, "up": pygame.K_z, "aim_l":pygame.K_f, "aim_r":K_g,"atk":K_SPACE}
    set_touche2 = {"left": pygame.K_LEFT, "right": pygame.K_RIGHT, "up": pygame.K_UP,"aim_l":pygame.K_KP1, "aim_r":pygame.K_KP2,"atk":pygame.K_KP0}
    set_position = [(w * 0.1,h * 0.72),(w * 0.89,h * 0.72)]

    # initialise les joueurs
    player1 = Player("A",set_position[0])
    K_player1 = set_touche1

    player2 = Player("A",set_position[1])
    K_player2 = set_touche2

    mode = 2 #lancement du jeu
    # récupère tous les joueurs existant
    T_joueur=[player1,player2]

    #limite de fps pour éviter que le jeu fasse crash
    fps= pygame.time.Clock()

    pygame.mouse.set_visible(False)
    while mode>=2:
        player1.update()
        player2.update()
        screen.blit(background, (0, 0))

        if player1.health>0:
            player1.affichage_final()


        if player2.health>0:
            player2.affichage_final()

        keys = pygame.key.get_pressed()
        if keys[K_player1["left"]]:#détecte si il va à gauche
            player1.move_left()


                
            
        if keys[K_player1["right"]]:#détecte si il va à droite
            player1.move_right()


        
        if keys[K_player1["up"]]:#détecte le jump
            player1.do_jump()
        player1.in_aire()
        player1.collision()
        if keys[K_player1["aim_l"]]:
            player1.aim_left()
        if keys[K_player1["aim_r"]]:
            player1.aim_right()
        if keys[K_player1["atk"]]:
            player1.attack(T_joueur)

        if keys[K_player2["left"]]:#détecte si il va à gauche
            player2.move_left()
        if keys[K_player2["right"]]:#détecte si il va à droite
            player2.move_right()
        if keys[K_player2["up"]]:#détecte le jump
            player2.do_jump()
        player2.in_aire()
        player2.collision()
        if keys[K_player2["aim_l"]]:
            player2.aim_left()
        if keys[K_player2["aim_r"]]:
            player2.aim_right()
        if keys[K_player2["atk"]]:
            player2.attack(T_joueur)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_BACKSPACE:
                    play_sound("sound/escape.mp3")
                    mode = pause(screen)
        #optimise  le nombre d'images par seconde
        fps.tick(60)
        #mets à jour l'écran




        pygame.display.flip()


    if mode == -1: #restart le jeu avec un appel réccursif
        mode=gameplay()
    return mode


