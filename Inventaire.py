import pygame
from player import Player
class Inventaire:
    def __init__(self) :
# Initialisation de Pygame
        self.oui=1
       
         
    def inven(self,boole,screen):
        
            # Paramètres de la fenêtre
            

            inven = pygame.image.load('images/inventaire.png')
            inven=pygame.transform.scale(inven,[600,500])
            #charger le jeu


            # Couleurs
        

            # Définition des éléments de l'inventaire
            inventory_items = {
                "gun": pygame.image.load("images/pistolet.png"),
                "grenad":pygame.image.load("images/Grenade.png"),
                # Ajoutez d'autres éléments ici
            }
            inventory_items["gun"]=pygame.transform.scale(inventory_items["gun"],[150,120])
            inventory_items["grenad"]=pygame.transform.scale(inventory_items["grenad"],[160,89])
            # Position de départ de l'inventaire
            inventory_x = 515
            inventory_y = 460
            # Boucle principale
            items_position={}
            zone_click_pistolet=pygame.Rect(514,454,90,90)
            zone_click_grenade=pygame.Rect(615,454,90,90)



 

            
            arme=""
            while boole:
                screen.blit(inven,(500,400 ))
                # Affichage des éléments de l'inventaire
                x, y = inventory_x, inventory_y
                for item_name, item_image in inventory_items.items():
                    screen.blit(item_image, (x, y))
                    items_position[item_name]=x,y
                    x+=65
                    y=y-10
                for event in pygame.event.get():
                
                    if event.type== pygame.KEYDOWN:
                        if event.key==pygame.K_g:
                            boole=False
                    if event.type==pygame.MOUSEBUTTONDOWN:     # Choisir l'arme dans l'inventaire
                        
                        x,y=pygame.mouse.get_pos()
                        if zone_click_pistolet.collidepoint(event.pos):    
                            arme="gun"
                        if zone_click_grenade.collidepoint(event.pos):
                            arme="grenade"
                            print("c'est bon")
                        
                pygame.display.flip()
            return arme

