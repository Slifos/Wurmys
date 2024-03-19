import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Paramètres de la fenêtre
WIDTH, HEIGHT = 800, 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Inventaire")
screen = pygame.display.set_mode((1080, 720))

background = pygame.image.load('images/inventaire_wurmys.png')
background=pygame.transform.scale(background,[1270,780])
#charger le jeu



# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Définition des éléments de l'inventaire
inventory_items = {
    "sword": pygame.image.load("images/Worms.png"),
    "potion": pygame.image.load("images/maps.png"),
    # Ajoutez d'autres éléments ici
}

# Position de départ de l'inventaire
inventory_x = 50
inventory_y = 50

# Boucle principale
while True:
    WINDOW.fill(WHITE)
    screen.blit(background, (0, 0))
    # Affichage des éléments de l'inventaire
    x, y = inventory_x, inventory_y
    for item_name, item_image in inventory_items.items():
        WINDOW.blit(item_image, (x, y))
        x += item_image.get_width() + 10

    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Mise à jour de l'affichage
    pygame.display.update()
