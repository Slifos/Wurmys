import pygame
from Player import player
pygame.init()
font= pygame.font.SysFont("LEMONMILK",40)
ecran = pygame.display.set_mode((0, 0), pygame.RESIZABLE)
Text_color =(255,255,255)
bgjeu = pygame.image.load("images/maps.png").convert()
bgjeu = pygame.transform.scale(bgjeu, [1920,1080])
# charger joueur
player= player()
continuer = True
def draw_texte (texte,font,text_color,x,y):
    img=font.render(texte,True,text_color)
    ecran.blit(img,(x,y))

while continuer:    
    draw_texte("Quitter jeu", font, Text_color, 1000, 700)
    ecran.blit(bgjeu, (0,0 ))
    # ici on crée un rectangle de couleur rose, en x=0, y=0 et de taille 300 sur 200
    # nous verrons plus tard comment faire plus en détail :)
    #faire apparaitre joueur
    ecran.blit(player.image,player.rect)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            continuer = False
    # ici on actualise l'écran, car on a affiché un rectangle rose, et on veut qu'il soit
    # visible. Si l'on avait pas mit cette instruction, on n'aurait jamais vu le rectangle !
    pygame.display.flip()

pygame.quit()