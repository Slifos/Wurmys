import pygame
pygame.init()
import math
from pygame.locals import*
#fenetre du jeux
screen_width =1270
screen_height=780
pygame.display.set_caption("Wurmys le jeu")
screen = pygame.display.set_mode((screen_width,screen_height),pygame.RESIZABLE)

jeu = 0
principoption = 0
principjeu    = 0
nombrejoueurs = 0
font= pygame.font.SysFont("LEMONMILK",40)

bg= pygame.image.load("images/1440xAUTO_processed_article_2023_08_bb08a0a5-e781-424d-8e2c-a11a5242e558-banner-master.jpg").convert()
bgoption = pygame.image.load("images/claude-monet-Impression-soleil-levant-1872-Musee-Marmottan-Monet-Paris-©-SLB-Christian-Baraja-1600x900.jpg").convert()
bgjeu = pygame.image.load("images/John_Martin_Le_Pandemonium_Louvre.jpg").convert()
bgjeu = pygame.transform.scale(bgjeu, [1270,780])
carrenoir = pygame.image.load("images/carrénoir.png").convert_alpha()
carrenoir.fill((100, 100, 100, 125), special_flags=BLEND_RGBA_MULT)
carrenoir = pygame.transform.scale(carrenoir, [170,60])
boutonjouer = pygame.image.load("images/bouton jouer.png").convert_alpha()
boutonjouer = pygame.transform.scale(boutonjouer, [200,60])
Text_color =(255,255,255)
def draw_texte (texte,font,text_color,x,y):
    img=font.render(texte,True,text_color)
    screen.blit(img,(x,y))


running =True
#boucle
while running:

    pygame.display.flip()
    screen.blit(bg, (0, 0))
    pos = pygame.mouse.get_pos()
    carrenoir = pygame.transform.scale(carrenoir, [170, 60])
    if (pos[0] > 780 and pos[0] < 940) and (pos[1] > 280 and pos[1] < 340):
        screen.blit(carrenoir,(768,280))
    if (pos[0] > 255 and pos[0] < 430) and (pos[1] > 280 and pos[1] < 340):
        screen.blit(carrenoir, (255, 280))
    if (pos[0] > 990 and pos[0] < 1300) and (pos[1] > 680 and pos[1] < 720):
        screen.blit(carrenoir,(990,680))
    draw_texte("MENU",font,Text_color,550,20)
    draw_texte("Options",font,Text_color,800,300)
    draw_texte("Jouer", font, Text_color, 300, 300)
    draw_texte("Quitter jeu", font, Text_color, 1000, 700)

    # récuperation d'input


    for event in pygame.event.get() :
        if event.type == pygame.MOUSEBUTTONDOWN:
            if (event.pos[0] > 780 and event.pos[0] < 940) and (event.pos[1] > 300 and event.pos[1] < 500) :
                principoption = 1
            if (event.pos[0] > 235 and event.pos[0] < 450) and (event.pos[1] > 280 and event.pos[1] < 340) :
                principjeu = 1
            if (event.pos[0] > 1000 and event.pos[0] < 1300) and (event.pos[1] > 650 and event.pos[1] < 900):
                running=False
        # si on clique sur la croix ça ferme le jeu
        if event.type == pygame.QUIT :
            running=False

    while principoption == 1 :
        pygame.display.flip()
        screen.blit(bgoption,(-50,0))
        draw_texte("OPTIONS", font, Text_color, 500, 20)
        draw_texte("Retour", font,Text_color,1000,700)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (event.pos[0] > 1000 and event.pos[0] < 1300) and (event.pos[1] > 650 and event.pos[1] < 900):
                    principoption = 0

    while principjeu == 1 :
        pygame.display.flip()
        screen.blit(bgjeu, (0, 0))
        carrenoir = pygame.transform.scale(carrenoir, [80, 80])
        pos = pygame.mouse.get_pos()

        if (pos[0] > 590 and pos[0] < 690) and (pos[1] > 170 and pos[1] < 270):
            screen.blit(carrenoir, (590, 170))
        if (pos[0] > 590 and pos[0] < 690) and (pos[1] > 320 and pos[1] < 420):
            screen.blit(carrenoir, (590, 320))
        if (pos[0] > 590 and pos[0] < 690) and (pos[1] > 470 and pos[1] < 570):
            screen.blit(carrenoir, (590, 470))
        if (pos[0] > 990 and pos[0] < 1300) and (pos[1] > 680 and pos[1] < 720):
            carrenoir = pygame.transform.scale(carrenoir, [180, 60])
            screen.blit(carrenoir, (950, 680))

        draw_texte("Sélectionnez le nombre de joueurs : ",font,Text_color,430,20)
        draw_texte("Retour", font,Text_color,1000,700)
        draw_texte("2", font, Text_color, 620, 200)
        draw_texte("3", font, Text_color, 620, 350)
        draw_texte("4", font, Text_color, 620, 500)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (event.pos[0] > 1000 and event.pos[0] < 1300) and (event.pos[1] > 650 and event.pos[1] < 900):
                    principjeu = 0
                if (event.pos[0] > 570 and event.pos[0] < 670) and (event.pos[1] > 150 and event.pos[1] < 250):
                    nombrejoueurs = 2
                    jeu = 1
                    principjeu = 0
                if (event.pos[0] > 570 and event.pos[0] < 670) and (event.pos[1] > 300 and event.pos[1] < 400):
                    nombrejoueurs = 3
                    jeu = 1
                    principjeu = 0
                if (event.pos[0] > 570 and event.pos[0] < 670) and (event.pos[1] > 450 and event.pos[1] < 550):
                    nombrejoueurs = 4
                    jeu = 1
                    principjeu = 0

    pygame.display.update()
pygame.quit()
