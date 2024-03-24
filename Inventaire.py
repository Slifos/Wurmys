import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Paramètres de la fenêtre
WIDTH, HEIGHT = 800, 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Inventaire")
screen = pygame.display.set_mode((1080, 720))

background = pygame.image.load('images/inventaire.png')
background=pygame.transform.scale(background,[1080,720])
#charger le jeu



# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Définition des éléments de l'inventaire
inventory_items = {
    "gun": pygame.image.load("images/pistolet.png"),
    "grenad":pygame.image.load("images/Grenade.png"),
    # Ajoutez d'autres éléments ici
}
inventory_items["grenad"]=pygame.transform.scale(inventory_items["grenad"],[200,120])
# Position de départ de l'inventaire
inventory_x = 27
inventory_y = 75

# Boucle principale
items_position={}
while True:
    WINDOW.fill(WHITE)
    screen.blit(background, (0, 0))
    # Affichage des éléments de l'inventaire
    x, y = inventory_x, inventory_y
    for item_name, item_image in inventory_items.items():
        WINDOW.blit(item_image, (x, y))
        items_position[item_name]=x,y
        x+=150
        print(items_position[item_name])

    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Mise à jour de l'affichage
    pygame.display.update()
