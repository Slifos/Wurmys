from fonction import *
import pygame


# Initialisation de pygame
pygame.init()

# Paramètres de la fenêtre

# Création de la fenêtre





# Fonction pour afficher un menu
def menu(option):
    info = pygame.display.Info()
    w = info.current_w
    h = info.current_h
    screen = pygame.display.set_mode((w, h))
    fps = pygame.time.Clock()

    bg = pygame.image.load("bg/bg_menu.png")
    bg = pygame.transform.scale(bg, (w, h))

    play_button = Image("ui/play_button.png",w*0.2,(w*0.4,h*0.3))
    exit_button = Image("ui/exit_button.png", w * 0.2, (w * 0.4, h * 0.7))
    title = Image("ui/title.png",w*0.35,(w * 0.35, h * 0))


    mode = 1
    play_music("sound/theme.mp3",0.5,option.volume)
    pygame.mouse.set_visible(True)
    screen.blit(bg, (0, 0))
    screen.blit(title.image, (title.rect))
    screen.blit(play_button.image, (play_button.rect))
    screen.blit(exit_button.image, (exit_button.rect))
    while mode==1:

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # Récupérer les coordonnées du clic
                mouse_pos = pygame.mouse.get_pos()
                #click sur jouer -> lance le jeu
                if play_button.rect.collidepoint(mouse_pos):
                    play_sound("sound/pressed.mp3",0.5,option.volume)
                    mode = 2

                # click sur exit -> Quitte le Jeu
                if exit_button.rect.collidepoint(mouse_pos):
                    mode = 0
                    play_sound("sound/exit.mp3",0.5,option.volume)



        pygame.display.flip()
        fps.tick(60)
    return mode

