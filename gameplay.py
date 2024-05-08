import pygame
from pygame.locals import *

from Inventaire import Inventaire
from Projetcile import *
from son import *
from player import Player
from Pause import pause
#Representation du jeu
pygame.init()
def update_hud(T_vie):
    screen = pygame.display.get_surface()
    w, h = screen.get_width(), screen.get_height()
    localisation1= [w*0.02,w*0.10,w*0.18]
    localisation2 = [w * 0.74, w * 0.82, w * 0.9]
    localisation_y= h*0.02
    ratio_vie = (w*0.08,w*0.08*1.1)
    fond = pygame.image.load("ui/button2.png")
    pomme = pygame.image.load("ui/pomme.png")
    fond = pygame.transform.scale(fond,ratio_vie)
    pomme = pygame.transform.scale(pomme, ratio_vie)
    max_vie = 3
    for elt in localisation1:
        screen.blit(fond,(elt,localisation_y))

    for elt in localisation2:
        screen.blit(fond,(elt,localisation_y))
    for i in range(T_vie[0]):
        screen.blit(pomme, (localisation1[i], localisation_y))
    for i in range(T_vie[1]):
        screen.blit(pomme, (localisation2[2-i], localisation_y))

def victory_screen(victory_player):
    w, h = pygame.display.Info().current_w, pygame.display.Info().current_h
    screen = pygame.display.set_mode((w, h), pygame.RESIZABLE)
    play_music("sound/victory_theme.mp3")

    bg_victory = pygame.image.load("bg/bg_victory.jpg")
    bg_victory = pygame.transform.scale(bg_victory,(w,h))

    player_image = pygame.image.load(victory_player.idle)
    ratio_player = (w*0.2, w*0.2*1.85)
    player_image = pygame.transform.scale(player_image,ratio_player)

    ratio_button = (w * 0.2, w * 0.2 / 2)
    restart_button = pygame.image.load("ui/restart_button.png")
    restart_button = pygame.transform.scale(restart_button, ratio_button)
    restart_rect = restart_button.get_rect()
    restart_rect.x,restart_rect.y = w*0.7, h*0.4

    exit_button = pygame.image.load("ui/exit_button.png")
    exit_button = pygame.transform.scale(exit_button, ratio_button)
    exit_rect = exit_button.get_rect()
    exit_rect.x,exit_rect.y = w*0.7,h*0.8

    ratio_victory = w*0.4,w*0.4*0.28
    victory_txt = pygame.image.load("ui/victory_txt.png")
    victory_txt = pygame.transform.scale(victory_txt, ratio_victory)
    victory_rect = victory_txt.get_rect()
    victory_rect.x, victory_rect.y = w * 0.3, h * 0.02
    mode = 4
    pygame.mouse.set_visible(True)
    fps = pygame.time.Clock()
    while mode>=2:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if restart_rect.collidepoint(mouse_x, mouse_y):
                    mode =-1
                    play_sound("sound/pressed.mp3")
                if exit_rect.collidepoint(mouse_x, mouse_y):
                    mode =1
                    play_sound("sound/exit.mp3")
        screen.blit(bg_victory,(0,0))
        screen.blit(player_image,(w*0.1,h*0.4))
        screen.blit(restart_button,(restart_rect.x,restart_rect.y))
        screen.blit(exit_button, (exit_rect.x, exit_rect.y))
        screen.blit(victory_txt, (victory_rect.x, victory_rect.y))
        pygame.display.flip()
        fps.tick(60)
    return mode
def decompte(joueur1,joueur2,bg):
    w, h = pygame.display.Info().current_w, pygame.display.Info().current_h
    screen = pygame.display.set_mode((w, h), pygame.RESIZABLE)
    ratio_chiffre = w*0.2,w*0.2*1.22
    trois = pygame.image.load("ui/3.png")
    trois = pygame.transform.scale(trois, ratio_chiffre)
    deux = pygame.image.load("ui/2.png")
    deux = pygame.transform.scale(deux, ratio_chiffre)
    un = pygame.image.load("ui/1.png")
    un = pygame.transform.scale(un, ratio_chiffre)
    ratio_start = w*0.6,w*0.6*0.344
    start = pygame.image.load("ui/start.png")
    start = pygame.transform.scale(start, ratio_start)
    i=0
    fps = pygame.time.Clock()
    tick = 0
    while i<400:
        i+=2
        screen.blit(bg, (0, 0))
        joueur1.affichage_final()
        joueur2.affichage_final()
        if i>301:
            screen.blit(start,(w*0.2,h*0.35))
            if tick==3:
                play_sound("sound/start.mp3")
                tick+=1

        elif i>200:
            screen.blit(un,(w*0.4,h*0.3))
            if tick==2:
                play_sound("sound/1.mp3")
                tick+=1
        elif i>100:
            screen.blit(deux,(w*0.4,h*0.3))
            if tick==1:
                play_sound("sound/2.mp3")
                tick+=1
        else:
            screen.blit(trois,(w*0.4,h*0.3))
            if tick==0:
                play_sound("sound/3.mp3")
                tick+=1
        fps.tick(60)
        pygame.display.flip()



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

    K_player1 = set_touche1


    K_player2 = set_touche2
    player1 = Player("A", set_position[0])
    player2 = Player("B", set_position[1])
    mode = 2 #lancement du jeu
    # récupère tous les joueurs existant


    #limite de fps pour éviter que le jeu fasse crash
    fps= pygame.time.Clock()
    vie_joueur1 = 3
    vie_joueur2 = 3
    pygame.mouse.set_visible(False)
    victory = False
    while mode>=2:

        if vie_joueur1<=0:
            victory=True
            joueur_victory = player2
        if vie_joueur2<=0:
            victory=True
            joueur_victory = player1
        player1 = Player("A", set_position[0])
        player2 = Player("B", set_position[1])

        T_joueur = [player1, player2]
        T_vie = [vie_joueur1,vie_joueur2]
        if not victory:
            manche=True
            decompte(player1, player2, background)
        else:
            manche=False
            mode=victory_screen(joueur_victory)
        after_match = 0
        while manche==True and mode>=2:

            player1.update()
            player2.update()
            screen.blit(background, (0, 0))
            update_hud(T_vie)
            keys = pygame.key.get_pressed()
            if not player1.is_alive() and after_match==0:
                vie_joueur1 -=1
                after_match += 1

            if not player2.is_alive() and after_match==0:
                after_match += 1
                vie_joueur2 -=1
            if after_match>=1:
                after_match+=1
            if after_match>400:
                manche = False

            player1.affichage_final()
            player2.affichage_final()

            if player1.is_alive():
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
            if player2.is_alive():
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


