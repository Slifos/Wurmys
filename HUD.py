import pygame
from fonction import*



def update_hud(option):
    """Renvoie l'hud des vie avec les pommes et ses contours"""
    screen = pygame.display.get_surface()
    surface = pygame.Surface((option.w, option.h), pygame.SRCALPHA)
    w, h = screen.get_width(), screen.get_height()
    ratio = w/(len(option.T_vie)*option.max_vie*len(option.T_vie))
    fond = Image("ui/button2.png",ratio,(0,0))
    pomme = Image("ui/pomme.png", ratio, (0, 0))
    marge_hauteur = h*0.01
    for i in range(len(option.T_vie)-1):

        for j in range(option.max_vie):
            surface.blit(fond.image,(ratio*j+(w/len(option.T_vie)+ratio*len(option.T_vie))*i,marge_hauteur))


        for j in range(option.T_vie[i]):
            surface.blit(pomme.image, (ratio*j+(w/len(option.T_vie)+ratio*len(option.T_vie))*i,marge_hauteur))

        pseudo = writting(option.joueurs[i].pseudo,ratio*(2/len(option.joueurs[i].pseudo)))
        surface.blit(pseudo,((w/len(option.T_vie)+ratio*len(option.T_vie))*i+ratio,marge_hauteur+ratio))
    for j in range(option.max_vie):
            surface.blit(fond.image, (w-(ratio*(j+1)),marge_hauteur))

    for j in range(option.T_vie[i+1]):
            surface.blit(pomme.image, (w-(ratio*(j+1)),marge_hauteur))
    pseudo = writting(option.joueurs[i+1].pseudo, ratio * (2 / len(option.joueurs[i].pseudo)))
    surface.blit(pseudo, ((w-(ratio*2)),marge_hauteur+ratio))
    return surface




def decompte(fond,option):
    """animation du decompte à chaque début de round"""
    w, h = pygame.display.Info().current_w, pygame.display.Info().current_h
    screen = pygame.display.set_mode((w, h), pygame.RESIZABLE)

    position_chiffre = w*0.4,h*0.3
    trois = Image("ui/3.png", w * 0.2, (position_chiffre))
    deux = Image("ui/2.png", w * 0.2, (position_chiffre))
    un = Image("ui/1.png", w * 0.2, (position_chiffre))
    start = Image("ui/start.png", w*0.6, (w * 0.22, h * 0.32))
    surface = pygame.surface.Surface((option.w,option.h),pygame.SRCALPHA)
    surface.blit(fond,(0,0))
    surface.blit(update_hud(option),(0,0))
    for elt in option.T_joueurs:
        surface.blit(elt.worm.image, elt.worm.rect)

    i=0
    fps = pygame.time.Clock()
    tick = 0
    while i<400:
        i+=2
        screen.blit(surface, (0, 0))



        if i>301:
            screen.blit(start.image,(start.rect))
            if tick==3:
                play_sound("sound/start.mp3",option)
                tick+=1

        elif i>200:
            screen.blit(un.image,(un.rect))
            if tick==2:
                play_sound("sound/1.mp3",option)
                tick+=1
        elif i>100:
            screen.blit(deux.image,(deux.rect))
            if tick==1:
                play_sound("sound/2.mp3",option)
                tick+=1
        else:
            screen.blit(trois.image,(trois.rect))
            if tick==0:
                play_sound("sound/3.mp3",option)
                tick+=1
        fps.tick(60)
        pygame.display.flip()
