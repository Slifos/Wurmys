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

    screen = pygame.display.set_mode((0, 0), pygame.RESIZABLE)
    w,h = pygame.display.get_surface().get_size()
    background = pygame.image.load('bg/bg_game.jpg')
    background = pygame.transform.scale(background, (w,h))
    # charger le jeu
    player1 = Player("A")
    player1.update_setting(w,h)
    K_player1 = {"left": pygame.K_q, "right": pygame.K_d, "up": pygame.K_z}

    mode = 2
    play_music("sound/game_theme.mp3")
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
        seconde = 0
        keys = pygame.key.get_pressed()



        screen.blit(background, (0, 0))
        if keys[K_player1["left"]]:
            player1.move_left()
        if keys[K_player1["right"]]:
            player1.move_right()
        if keys[K_player1["up"]]:
            player1.do_jump()
        player1.in_aire()
        screen.blit(player1.image, (player1.rect_x,player1.rect_y) ) #(player1.rect_x,player1.rect_y)

        # vérifier où le joueur veut aller


        # mettre à jour l'écran
        pygame.display.flip()






        fps.tick(60)
        pygame.display.flip()
    if mode == -1: #restart le jeu avec un appel réccursif
        mode=gameplay()
    return mode

