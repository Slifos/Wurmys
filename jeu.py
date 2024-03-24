import pygame
from player import player
from Inventaire import Inventaire
pygame.init()
font= pygame.font.SysFont("LEMONMILK",40)
screen = pygame.display.set_mode((0, 0), pygame.RESIZABLE)
Text_color =(255,255,255)
bgjeu = pygame.image.load("images/maps.png").convert()
bgjeu = pygame.transform.scale(bgjeu, [1920,1080])
# charger joueur
player= player()
continuer = True
def draw_texte (texte,font,text_color,x,y):
    img=font.render(texte,True,text_color)
    screen.blit(img,(x,y))



'''def inventair(boole):
     
        # Paramètres de la fenêtre
        

        inven = pygame.image.load('images/inventaire.png')
        inven=pygame.transform.scale(inven,[900,720])
        #charger le jeu



        # Couleurs
     

        # Définition des éléments de l'inventaire
        inventory_items = {
            "gun": pygame.image.load("images/pistolet.png"),
            "grenad":pygame.image.load("images/Grenade.png"),
            # Ajoutez d'autres éléments ici
        }
        inventory_items["gun"]=pygame.transform.scale(inventory_items["gun"],[240,120])
        inventory_items["grenad"]=pygame.transform.scale(inventory_items["grenad"],[200,120])
        # Position de départ de l'inventaire
        inventory_x = 515
        inventory_y = 500
        # Boucle principale
        items_position={}
        while boole:
            screen.blit(inven,(500,400 ))
            # Affichage des éléments de l'inventaire
            x, y = inventory_x, inventory_y
            for item_name, item_image in inventory_items.items():
                screen.blit(item_image, (x, y))
                items_position[item_name]=x,y
                x+=125
                y=y-10
            for event in pygame.event.get():
               
                if event.type== pygame.KEYDOWN:
                    if event.key==pygame.K_g:
                        boole=False
            pygame.display.flip()'''

inventair=Inventaire()

while continuer:    
    draw_texte("Quitter jeu", font, Text_color, 1000, 700)
    screen.blit(bgjeu, (0,0 ))
    # ici on crée un rectangle de couleur rose, en x=0, y=0 et de taille 300 sur 200
    # nous verrons plus tard comment faire plus en détail :g)
    #faire apparaitre joueur
    screen.blit(player.image,player.rect)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            continuer = False
        if event.type== pygame.KEYDOWN:
            if event.key==pygame.K_g:
                inventair.inven(True, screen)
                print("oui")
                

    # ici on actualise l'écran, car on a affiché un rectangle rose, et on veut qu'il soit
    # visible. Si l'on avait pas mit cette instruction, on n'aurait jamais vu le rectangle !
    pygame.display.flip()

pygame.quit()