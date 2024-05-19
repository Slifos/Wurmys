import pygame
from fonction import*

# Initialisation de pygame


# Paramètres de la fenêtre

# Création de la fenêtre




"""afficahge de l'écran pause en jeu"""

def pause(option):
    screen = pygame.display.get_surface()
    info = pygame.display.Info()
    w = info.current_w
    h = info.current_h

    fps = pygame.time.Clock()


    resume = Image("ui/resume_button.png", w * 0.2, (w * 0.4, h * 0.3))
    restart = Image("ui/restart_button.png", w * 0.2, (w * 0.4, h * 0.5))
    exit = Image("ui/exit_button.png", w * 0.2, (w * 0.4, h * 0.7))
     #postion du bouton exit sur l'écran

    bg = pygame.Surface((w,h))
    bg.fill((0,0,0))
    bg.set_alpha(150)
    screen.blit(bg, (0, 0))
    pygame.display.flip()


    #titre pause
    titre = Image("ui/pause.png", 0.3*w, ( w * 0.35, h * 0))
    mode = 3
    screen.blit(resume.image, (resume.rect.x, resume.rect.y))
    screen.blit(exit.image, (exit.rect.x, exit.rect.y))
    screen.blit(titre.image, (titre.rect.x, titre.rect.y))
    screen.blit(restart.image, (restart.rect.x, restart.rect.y))
    pygame.mouse.set_visible(True)

    while mode==3:

        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:# appuie sur echappe = revenir au jeu
                if event.key == pygame.K_ESCAPE:
                    mode = 2
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # Récupérer les coordonnées du clic
                mouse_pos = pygame.mouse.get_pos()
                #click sur jouer -> lance le jeu
                if resume.rect.collidepoint(mouse_pos):
                    mode = 2

                # click sur restart -> relance le jeu
                if restart.rect.collidepoint(mouse_pos):
                    mode = -1
                    play_sound("sound/pressed.mp3",option)
                # click sur exit -> retourne à l'écran titre
                if exit.rect.collidepoint(mouse_pos):
                    mode = 1
                    play_sound("sound/exit.mp3",option)




        pygame.display.flip()
        fps.tick(60)

    return mode

