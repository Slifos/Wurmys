from son import *
import pygame
import sys

# Initialisation de pygame
pygame.init()

# Paramètres de la fenêtre

# Création de la fenêtre





# Fonction pour afficher un menu
def menu():
    info = pygame.display.Info()
    w = info.current_w
    h = info.current_h
    screen = pygame.display.set_mode((w, h))
    fps = pygame.time.Clock()

    w_button, h_button = w*0.2, h*0.2
    play_button = pygame.image.load("ui/play_button.png")
    play_button = pygame.transform.scale(play_button, (w_button, h_button))
    play_x,play_y = w*0.4,h*0.3#postion du bouton play sur l'écran

    exit_button = pygame.image.load("ui/exit_button.png")
    exit_button = pygame.transform.scale(exit_button, (w_button, h_button))
    exit_x, exit_y = w * 0.4, h * 0.5 #postion du bouton exit sur l'écran

    bg = pygame.image.load("bg/bg_menu.png")  # Replace "your_image_path.jpg" with the path to your image file
    bg = pygame.transform.scale(bg, (w, h))

    title = pygame.image.load("ui/title.png")
    w_title = 0.35*w
    title = pygame.transform.scale(title, (w_title,w_title*0.31))
    title_x, title_y = w * 0.35, h * 0  # position du titre sur l'écran

    mode = 1
    play_music("sound/theme.mp3")
    pygame.mouse.set_visible(True)
    while mode==1:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # Récupérer les coordonnées du clic
                mouse_x, mouse_y = pygame.mouse.get_pos()
                #click sur jouer -> lance le jeu
                if mouse_x > play_x and mouse_x < play_x + w_button and mouse_y > play_y and mouse_y < play_y + h_button:
                    play_sound("sound/pressed.mp3")
                    mode = 2

                # click sur exit -> Quitte le Jeu
                if mouse_x > exit_x and mouse_x < exit_x + w_button and mouse_y > exit_y and mouse_y < exit_y + h_button:
                    mode = 0
                    play_sound("sound/exit.mp3")

        screen.blit(bg, (0, 0))
        screen.blit(title, (title_x, title_y))
        screen.blit(play_button,(play_x,play_y))
        screen.blit(exit_button,(exit_x,exit_y))

        pygame.display.flip()
        fps.tick(60)
    return mode

