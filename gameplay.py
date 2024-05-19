import pygame
from fonction import *

from player import Player
from Platform import platform

from Pause import pause
from victory import victory_screen
from HUD import*
#Representation du jeu
pygame.init()
"""coeur du gameplay du jeu"""
def gameplay(option):

    #initialise le jeu

    screen = pygame.display.get_surface()
    w, h = pygame.display.Info().current_w, pygame.display.Info().current_h
    fond  = pygame.Surface((w,h),pygame.SRCALPHA)
    stop_music()

    # initialise le fond en fonction des dimensions de l'écran (16:9 de préférence)
    background = pygame.image.load('bg/bg_game.jpg')
    background = pygame.transform.scale(background, (w,h))
    """initialise les touches clavier"""
    K_player1 = {"left": pygame.K_q, "right": pygame.K_d, "up": pygame.K_z,"down":pygame.K_s, "aim_l":pygame.K_f, "aim_r":pygame.K_g,"atk":pygame.K_SPACE,"switch":pygame.K_e}
    K_player2 = {"left": pygame.K_LEFT, "right": pygame.K_RIGHT, "up": pygame.K_UP,"down":pygame.K_DOWN,"aim_l":pygame.K_KP1, "aim_r":pygame.K_KP2,"atk":pygame.K_KP0,"switch":pygame.K_KP4}
    set_position = [(w * 0.1,h * 0.72),(w * 0.89,h * 0.72)]
    """initialise la manette"""
    pygame.joystick.init()
    joystick_count = pygame.joystick.get_count()
    if joystick_count == 0:
        print("Aucune manette détectée.")
    if joystick_count >= 1:
        # Sélectionner la première manette détectée

        joystick = pygame.joystick.Joystick(0)
        joystick.init()
        print("Manette détectée: " + joystick.get_name())
    if joystick_count >= 2:
        # Sélectionner et initialiser la deuxième manette
        joystick2 = pygame.joystick.Joystick(1)
        joystick2.init()
        print("Manette 2 détectée: " + joystick2.get_name())

    # initialise les joueurs
    mode = 2
    fps= pygame.time.Clock()
    vie_joueur1 = option.max_vie
    vie_joueur2 = option.max_vie
    pygame.mouse.set_visible(False)
    victory = False
    while mode>=2:
        """initialisation de chaque rounds"""
        if vie_joueur1<=0:
            victory=True
            joueur_victory = player2
        if vie_joueur2<=0:
            victory=True
            joueur_victory = player1

        """initialise les joueurs pour le prochain round"""
        option.T_vie = [vie_joueur1, vie_joueur2]
        player1 = Player(set_position[0], option,0)
        player2 = Player(set_position[1], option,1)
        option.T_joueurs = [player1, player2]

        """affichage des vies"""
        HUD = update_hud(option)

        """initialise les platforms pour le prochain round"""
        platform1=platform(w*0.3,(w*0.35,h*0.55))
        platform2 = platform(w*0.3,(w*0.02,h*0.28))
        platform3 = platform(w * 0.3, (w * 0.68, h * 0.28))
        option.T_platform = [platform1,platform2,platform3]
        fond.blit(background,(0,0))
        fond.blit(HUD,(0,0))
        for elt in option.T_platform:
            fond.blit(elt.image,elt.platform_rect)





        if not victory:
            """s'il n'y a pas de victoire alors la partie continue"""
            manche=True
            decompte(fond,option)

            play_music("sound/game_theme2.mp3", option)
        else:
            """si victoire alors affichage du joueur gagnant"""
            manche=False
            mode=victory_screen(joueur_victory,option)
        after_match = 0

        while manche==True and mode>=2:
            #récupère les input clavier
            keys = pygame.key.get_pressed()
            """affichage du fond par dessous les joueurs à chaques itérations"""
            screen.blit(fond, (0, 0))

            """maj des images joueurs + propriétés du joueurs (pv, placement, etc)"""
            if player1.alive:

                player1.update(option)
            if player2.alive:

                player2.update(option)

            if not player1.alive and after_match==0:
                vie_joueur1 -=1
                after_match += 1

                stop_music()
                play_sound("sound/victory_effect.mp3", option)

            if not player2.alive and after_match==0:
                after_match += 1
                vie_joueur2 -=1

                stop_music()
                play_sound("sound/victory_effect.mp3",option)
            """permet au joueur de continuer à se déplacer meme après la mort de l'un des joueurs"""
            if after_match>=1:
                after_match+=1
            if after_match>400:
                manche = False


            """vérifie si une manette ou 2 manettes sont connectés
            sinon ils donnent les inputs clavier"""
            if joystick_count>=1:

                axe_x = joystick.get_axis(0)
                axe_y =joystick.get_axis(1)
                gachette = joystick.get_axis(5)
                axe2_x,axe2_y = joystick.get_axis(2),joystick.get_axis(3)

                player1.aim(axe2_x, axe2_y)
                player1.move(axe_x)

                if joystick.get_button(0):
                    player1.do_jump()

                if gachette>0.3:
                    player1.attack()

                if joystick.get_button(4) or joystick.get_button(5):
                    player1.arme_switch()
            else:
                if keys[K_player1["left"]]:
                    player1.move_left()
                if keys[K_player1["right"]]:
                    player1.move_right()
                if keys[K_player1["up"]]:
                    player1.do_jump()
                if keys[K_player1["aim_l"]]:
                    player1.aim_left()
                if keys[K_player1["aim_r"]]:
                    player1.aim_right()
                if keys[K_player1["atk"]]:
                    player1.attack()
                if keys[K_player1["switch"]]:
                    player1.arme_switch()
            if joystick_count >= 2:
                axe_x2 = joystick2.get_axis(0)
                gachette2 = joystick2.get_axis(5)
                axe2_x2, axe2_y2 = joystick2.get_axis(2), joystick2.get_axis(3)
                player2.move(axe_x2)
                player2.aim(axe2_x2, axe2_y2)
                if joystick2.get_button(0):
                    player2.do_jump()

                if gachette2 > 0.3:
                    player2.attack()

                if joystick2.get_button(4) or joystick2.get_button(5):
                    player2.arme_switch()
            else:
                if keys[K_player2["left"]]:
                    player2.move_left()
                if keys[K_player2["right"]]:
                    player2.move_right()
                if keys[K_player2["up"]]:
                    player2.do_jump()
                if keys[K_player2["aim_l"]]:
                    player2.aim_left()
                if keys[K_player2["aim_r"]]:
                    player2.aim_right()
                if keys[K_player2["atk"]]:
                    player2.attack()
                if keys[K_player2["switch"]]:
                    player2.arme_switch()


            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        play_sound("sound/escape.mp3",option)
                        mode = pause(option)

            #optimise  le nombre d'images par seconde
            fps.tick(60)
            #mets à jour l'écran




            pygame.display.flip()


    if mode == -1: #restart le jeu avec un appel réccursif en fonction du screen_pause
        mode=gameplay(option)
    return mode



