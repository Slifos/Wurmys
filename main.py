import pygame
from game import Game
pygame.init()


# Generer la fenêtre du jeu
pygame.display.set_caption("Wurmys")
screen = pygame.display.set_mode((1080, 720))

background = pygame.image.load('images/desert.jpg')
#charger le jeu
game = Game()

running = True

while running:

    screen.blit(background, (0, 0))

    #appliquer l'image du joueur
    screen.blit(game.player.image, game.player.rect)



    #vérifier où le joueur veut aller
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()


    print(game.player.rect.x)

    #mettre à jour l'écran
    pygame.display.flip()

    #fermeture de la fenetre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")
        elif event.type == pygame.KEYDOWN:
           game.pressed[event.key] = True

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False