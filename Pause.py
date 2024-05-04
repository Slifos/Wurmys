from son import *
import pygame
import sys

# Initialisation de pygame
pygame.init()

# Paramètres de la fenêtre

# Création de la fenêtre





# Fonction pour afficher un menu
def pause(screen):
    info = pygame.display.Info()
    w = info.current_w
    h = info.current_h
    fps = pygame.time.Clock()

    w_button, h_button = w*0.2, h*0.2
    resume_button = pygame.image.load("ui/resume_button.png")
    resume_button = pygame.transform.scale(resume_button, (w_button, h_button))
    resume_x,resume_y = w*0.4,h*0.3#postion du bouton play sur l'écran

    restart_button = pygame.image.load("ui/restart_button.png")
    restart_button = pygame.transform.scale(restart_button, (w_button, h_button))
    restart_x, restart_y = w * 0.4, h * 0.5

    exit_button = pygame.image.load("ui/exit_button.png")
    exit_button = pygame.transform.scale(exit_button, (w_button, h_button))
    exit_x, exit_y = w * 0.4, h * 0.7 #postion du bouton exit sur l'écran

    bg = pygame.Surface((w,h))
    bg.fill((0,0,0))
    # Replace "your_image_path.jpg" with the path to your image file
    bg.set_alpha(150)
    screen.blit(bg, (0, 0))
    pygame.display.flip()

    #titre pause
    title = pygame.image.load("ui/pause.png")
    w_title = 0.3*w
    title = pygame.transform.scale(title, (w_title, w_title*0.21))
    title_x, title_y = w * 0.35, h * 0  # position du titre sur l'écran
    mode = 3
    pygame.mouse.set_visible(True)
    while mode==3:

        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:# appuie sur echappe = revenir au jeu
                if event.key == pygame.K_ESCAPE:
                    mode = 2
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # Récupérer les coordonnées du clic
                mouse_x, mouse_y = pygame.mouse.get_pos()
                #click sur jouer -> lance le jeu
                if mouse_x > resume_x and mouse_x < resume_x + w_button and mouse_y > resume_y and mouse_y < resume_y + h_button:
                    mode = 2
                # click sur restart -> relance le jeu
                if mouse_x > restart_x and mouse_x < restart_x + w_button and mouse_y > restart_y and mouse_y < restart_y + h_button:
                    mode = -1
                # click sur exit -> retourne à l'écran titre
                if mouse_x > exit_x and mouse_x < exit_x + w_button and mouse_y > exit_y and mouse_y < exit_y + h_button:
                    mode = 1



        screen.blit(resume_button,(resume_x,resume_y))
        screen.blit(exit_button,(exit_x,exit_y))
        screen.blit(title, (title_x, title_y))
        screen.blit(restart_button, (restart_x, restart_y))
        pygame.display.flip()
        fps.tick(60)

    return mode

