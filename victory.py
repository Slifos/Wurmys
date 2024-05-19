import pygame
from fonction import*
"""Fonction qui permet d'afficher l'écran de victoire à la fin du jeu"""
def victory_screen(victory_player,option):
    w, h = pygame.display.Info().current_w, pygame.display.Info().current_h
    screen = pygame.display.set_mode((w, h), pygame.RESIZABLE)
    play_music("sound/victory_theme.mp3",option)

    bg_victory = pygame.image.load("bg/bg_victory.jpg")
    bg_victory = pygame.transform.scale(bg_victory,(w,h))

    player = Image(victory_player.idle, w * 0.2, (w*0.1,h*0.4))
    restart = Image("ui/restart_button.png", w * 0.2, (w*0.7, h*0.5))
    exit = Image("ui/exit_button.png", w * 0.2, (w*0.7,h*0.7))
    victory_txt = Image("ui/victory_txt.png", w * 0.4, (w * 0.3, h * 0.02))
    pseudo = writting(option.joueurs[victory_player.id].pseudo, w*0.05)

    """affichage du fond"""
    screen.blit(bg_victory, (0, 0))
    screen.blit(player.image, (player.rect))
    screen.blit(restart.image, (restart.rect.x, restart.rect.y))
    screen.blit(exit.image, (exit.rect.x, exit.rect.y))
    screen.blit(victory_txt.image, (victory_txt.rect.x, victory_txt.rect.y))
    screen.blit(pseudo,(w*0.1,h*0.24))

    mode = 4
    pygame.mouse.set_visible(True)
    fps = pygame.time.Clock()
    while mode>=2:
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if restart.rect.collidepoint(mouse_pos) :
                    mode =-1
                    play_sound("sound/pressed.mp3",option)
                if exit.rect.collidepoint(mouse_pos):
                    mode =1
                    play_sound("sound/exit.mp3",option)

        #affichage

        pygame.display.flip()
        fps.tick(60)
    return mode
