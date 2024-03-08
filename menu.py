import pygame
pygame.init()
import math
#fenetre du jeux
screen_width =1270
screen_height=780
pygame.display.set_caption("Wurmys le jeu")
screen =pygame.display.set_mode((screen_width,screen_height),pygame.RESIZABLE)

jeu = 0
principoption = 0
principjeu    = 0
nombrejoueurs = 0
font= pygame.font.SysFont("LEMONMILK",40)

bg= pygame.image.load("1440xAUTO_processed_article_2023_08_bb08a0a5-e781-424d-8e2c-a11a5242e558-banner-master.jpg").convert()
bgoption = pygame.image.load("claude-monet-Impression-soleil-levant-1872-Musee-Marmottan-Monet-Paris-©-SLB-Christian-Baraja-1600x900.jpg").convert()
bgjeu = pygame.image.load("John_Martin_Le_Pandemonium_Louvre.jpg").convert()
bgjeu = pygame.transform.scale(bgjeu, [1270,780])
boutonjouer = pygame.image.load("bouton jouer.png").convert_alpha()
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
    screen.blit(boutonjouer, (235, 280))
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