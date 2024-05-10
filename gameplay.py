import pygame
from fonction import *

from player import Player
from Platform import platform

from Pause import pause
from victory import victory_screen
from HUD import*
#Representation du jeu
pygame.init()
def gameplay(option):

    #initialise le jeu

    screen = pygame.display.get_surface()
    w, h = pygame.display.Info().current_w, pygame.display.Info().current_h

    # initialise le fond en fonction des dimensions de l'écran (16:9 de préférence)
    background = pygame.image.load('bg/bg_game.jpg')
    background = pygame.transform.scale(background, (w,h))

    play_music("sound/game_theme2.mp3",0.2,option.volume)
    set_position = [(w * 0.1,h * 0.72),(w * 0.89,h * 0.72)]

    # initialise les joueurs
    K_player1 = option.joueur1_touche
    K_player2 = option.joueur2_touche
    player1 = Player("A", set_position[0],option)
    player2 = Player("B", set_position[1],option)
    mode = 2 #lancement du jeu
    # récupère tous les joueurs existant


    #limite de fps pour éviter que le jeu fasse crash
    fps= pygame.time.Clock()
    vie_joueur1 = option.vie
    vie_joueur2 = option.vie
    pygame.mouse.set_visible(False)
    victory = False
    while mode>=2:

        platform1=platform(w*0.3,(w*0.35,h*0.55))
        platform2 = platform(w*0.3,(w*0.02,h*0.28))
        platform3 = platform(w * 0.3, (w * 0.68, h * 0.28))
        floor = platform(w,(0,h*0.8))
        floor.affichage_platform()
        T_platform = [floor,platform1,platform2,platform3]


        if vie_joueur1<=0:
            victory=True
            joueur_victory = player2
        if vie_joueur2<=0:
            victory=True
            joueur_victory = player1
        player1 = Player("A", set_position[0], option)
        player2 = Player("B", set_position[1], option)

        T_joueur = [player1, player2]
        T_vie = [vie_joueur1,vie_joueur2]
        if not victory:
            manche=True
            decompte(player1, player2, background,T_platform,option)
        else:
            manche=False
            mode=victory_screen(joueur_victory,option)
        after_match = 0

        while manche==True and mode>=2:

            player1.update(T_joueur)
            player2.update(T_joueur)
            screen.blit(background, (0, 0))
            update_hud(T_vie)
            keys = pygame.key.get_pressed()
            if not player1.alive and after_match==0:
                vie_joueur1 -=1
                after_match += 1

            if not player2.alive and after_match==0:
                after_match += 1
                vie_joueur2 -=1
            if after_match>=1:
                after_match+=1
            if after_match>400:
                manche = False
            platform1.affichage_platform()
            platform2.affichage_platform()
            platform3.affichage_platform()

            player1.affichage_final()
            player2.affichage_final()

            if player1.alive:
                if keys[K_player1["left"]]:#détecte si il va à gauche
                    player1.move_left()
                if keys[K_player1["right"]]:#détecte si il va à droite
                    player1.move_right()
                if keys[K_player1["up"]]:#détecte le jump
                    player1.do_jump()
                if keys[K_player1["down"]]:
                    player1.go_down()
                player1.in_aire()
                player1.collision(T_platform)
                if keys[K_player1["aim_l"]]:
                    player1.aim_left()
                if keys[K_player1["aim_r"]]:
                    player1.aim_right()
                if keys[K_player1["atk"]]:
                    player1.attack(T_joueur)
                if keys[K_player1["switch"]]:
                    player1.arme_switch()

            if player2.alive:
                if keys[K_player2["left"]]:#détecte si il va à gauche
                    player2.move_left()
                if keys[K_player2["right"]]:#détecte si il va à droite
                    player2.move_right()
                if keys[K_player2["up"]]:#détecte le jump
                    player2.do_jump()
                player2.in_aire()
                player2.collision(T_platform)
                if keys[K_player2["aim_l"]]:
                    player2.aim_left()
                if keys[K_player2["aim_r"]]:
                    player2.aim_right()
                if keys[K_player2["atk"]]:
                    player2.attack(T_joueur)
                if keys[K_player2["switch"]]:
                    player2.arme_switch()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE or event.key == pygame.K_BACKSPACE:
                        play_sound("sound/escape.mp3",0.5,option.volume)
                        mode = pause(option)
            #optimise  le nombre d'images par seconde
            fps.tick(60)
            #mets à jour l'écran




            pygame.display.flip()


    if mode == -1: #restart le jeu avec un appel réccursif
        mode=gameplay(option)
    return mode


