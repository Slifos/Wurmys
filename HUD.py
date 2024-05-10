import pygame
from fonction import*



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


def decompte(joueur1,joueur2,bg,T_platform,option):
    w, h = pygame.display.Info().current_w, pygame.display.Info().current_h
    screen = pygame.display.set_mode((w, h), pygame.RESIZABLE)

    position_chiffre = w*0.4,h*0.3
    trois = Image("ui/3.png", w * 0.2, (position_chiffre))
    deux = Image("ui/2.png", w * 0.2, (position_chiffre))
    un = Image("ui/1.png", w * 0.2, (position_chiffre))
    start = Image("ui/start.png", w*0.6, (w * 0.22, h * 0.32))



    i=0
    fps = pygame.time.Clock()
    tick = 0
    while i<400:
        i+=2
        screen.blit(bg, (0, 0))
        for j in range(len(T_platform)-1):
            T_platform[j+1].affichage_platform()
        joueur1.affichage_final()
        joueur2.affichage_final()

        if i>301:
            screen.blit(start.image,(start.rect))
            if tick==3:
                play_sound("sound/start.mp3",0.5,option.volume)
                tick+=1

        elif i>200:
            screen.blit(un.image,(un.rect))
            if tick==2:
                play_sound("sound/1.mp3",0.5,option.volume)
                tick+=1
        elif i>100:
            screen.blit(deux.image,(deux.rect))
            if tick==1:
                play_sound("sound/2.mp3",0.5,option.volume)
                tick+=1
        else:
            screen.blit(trois.image,(trois.rect))
            if tick==0:
                play_sound("sound/3.mp3",0.5,option.volume)
                tick+=1
        fps.tick(60)
        pygame.display.flip()