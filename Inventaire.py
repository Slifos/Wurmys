import pygame
class Inventaire:
    def __init__(self) :
# Initialisation de Pygame
        self.oui=1
         
    def inven(self,boole,screen):
        
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
                pygame.display.flip()
