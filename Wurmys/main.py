import pygame
from game import Game
from Inventaire import Inventaire
from Projetcile import *
pygame.init()


# Generer la fenêtre du jeu
pygame.display.set_caption("Wurmys")
screen = pygame.display.set_mode((0, 0),pygame.RESIZABLE)

background = pygame.image.load('images/desert.jpg')
background=pygame.transform.scale(background,[1920,1080])
#charger le jeu
game = Game()

running = True

Largeur,Hauteur=pygame.display.get_surface().get_size()


inventair=Inventaire()
fpsClock=pygame.time.Clock()    
sol=800

pygame.mouse.set_visible(1)
while running:
    seconde=0

    screen.blit(background, (0, 0))

    #appliquer l'image du joueur
    screen.blit(game.player.image, game.player.rect)



    #vérifier où le joueur veut aller
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()



    #mettre à jour l'écran
    pygame.display.flip()

    #fermeture de la fenetre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                running = False
        if event.type == pygame.KEYDOWN:
           game.pressed[event.key] = True

        if event.type == pygame.KEYUP:
            game.pressed[event.key] = False
        
        if event.type== pygame.KEYDOWN:
            if event.key==pygame.K_g:
                game.player.arme=inventair.inven(True, screen)  #Renvoie l'arme choisit dans le menu 
        
        if event.type== pygame.KEYDOWN:
            if event.key==pygame.K_z:
                ball=Projectile(game.player.rect.x,game.player.rect.y,0,0,1)
                pos_dx=ball.x_pos
                pos_dh=ball.z_pos
                buton_clicked=0
                while  buton_clicked==0:
                    for event2 in pygame.event.get() :
                        
                        if event2.type == pygame.MOUSEBUTTONDOWN:
                                    
                                    
                            x,y =pygame.mouse.get_pos()
                            buton_clicked=1     
                            hauteur,longueur,vitesse=ball.vitesse(x,y)     
                
                            
                while ball.z_pos<sol or seconde<0.1:
                            
                            
                            
                            
                    ball.lancement(hauteur,longueur,seconde,pos_dx,pos_dh)
                    
                    screen.blit(background, (0,0 ))
                    screen.blit(game.player.image,game.player.rect)
      
                    ball.draw(screen)
                    
                    seconde+=0.01
                    pygame.display.flip()




                   
    
           
    fpsClock.tick(220)
    pygame.display.flip()

pygame.quit()
    