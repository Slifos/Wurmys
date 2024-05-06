import pygame
from pygame.locals import *

from Inventaire import Inventaire
from Projetcile import *
from son import *
from player import Player
from Pause import pause
#Representation du jeu
pygame.init()
def gameplay():

    #initialise le jeu
    w, h = pygame.display.Info().current_w, pygame.display.Info().current_h
    screen = pygame.display.set_mode((w, h), pygame.RESIZABLE)
    background = pygame.image.load('bg/bg_game.jpg')
    background = pygame.transform.scale(background, (w,h))#initialise le fond en fonction des dimensions de l'écran (16:9 de préférence)
    play_music("sound/game_theme.mp3")#joue le thème du jeu

    # initialise les joueurs
    player1 = Player("A",w,h)
    player1.update_setting(w,h)#permets aux joueurs de changer ses settings
    #initialise les touches du joueur1
    K_player1 = {"left": pygame.K_q, "right": pygame.K_d, "up": pygame.K_z}
    player2 = Player("A",w,h)
    player2.update_setting(w,h)#permets aux joueurs de changer ses settings
    #initialise les touches du joueur1
    K_player2 = {"left": pygame.K_LEFT, "right": pygame.K_RIGHT, "up": pygame.K_UP}
    mode = 2 #lancement du jeu

    inventaire = Inventaire()
    fps= pygame.time.Clock()
    pygame.mouse.set_visible(True)
    while mode>=2:
        seconde=0

        player1.update()
        player2.update()
        keys = pygame.key.get_pressed()
        if keys[K_player1["left"]]:#détecte si il va à gauche
            player1.move_left()
            if player1.pos==0:
                player1.image=pygame.transform.flip(player1.image,True,False)
                player1.pos=1

                
            
        if keys[K_player1["right"]]:#détecte si il va à droite
            player1.move_right()
            if player1.pos==1:
                player1.image=pygame.transform.flip(player1.image,True,False)
                player1.pos=0

        
        if keys[K_player1["up"]]:#détecte le jump
            player1.do_jump()
        player1.in_aire()


        if keys[K_player2["left"]]:#détecte si il va à gauche
            player2.move_left()
        if keys[K_player2["right"]]:#détecte si il va à droite
            player2.move_right()
        if keys[K_player2["up"]]:#détecte le jump
            player2.do_jump()
        player2.in_aire()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_g:
                    player1.arme=inventaire.inven(True, screen)
                    if not(player1.arme ==""):
                        player1.idle="perso/worm_idle_A_"+player1.arme+".png"  #Renvoie l'arme choisit dans le menu 
                        player1.update_setting(w,h)
                        screen.blit(player1.image, (player1.rect_x, player1.rect_y))                        

                if event.key == pygame.K_ESCAPE or event.key == pygame.K_BACKSPACE:
                    mode = pause(screen)
          
                if player1.arme =="grenade":
                    if event.key==pygame.K_e:
                        
                        ball=Projectile(player1.rect_x,player1.rect_y,0,0,1)
                        pos_dx=ball.x_pos
                        pos_dh=ball.z_pos
                        buton_clicked=0
                        
                        while  buton_clicked==0:
                            for event2 in pygame.event.get() :
                                
                                if event2.type == pygame.MOUSEBUTTONDOWN:
                                            
                                            
                                    x,y =pygame.mouse.get_pos()
                                    buton_clicked=1     
                                    hauteur,longueur,vitesse=ball.vitesse(x,y)     
                        

                        while ball.z_pos<(h-175) or seconde<0.1:
                                    
                                    
                                    
                                    
                            ball.lancement(hauteur,longueur,seconde,pos_dx,pos_dh)
                            screen.blit(background, (0,0 ))
                            screen.blit(player1.image, (player1.rect_x, player1.rect_y))                        
                            ball.draw(screen)
                            
                            seconde+=0.01
                            pygame.display.flip()       

        




      








        #optimise  le nombre d'images par seconde
        fps.tick(60)
        #mets à jour l'écran
        screen.blit(background, (0, 0))
        screen.blit(player1.image, (player1.rect_x, player1.rect_y))
        screen.blit(player2.image, (player2.rect_x, player2.rect_y))

        player1.update_health_bar( screen)
        player2.update_health_bar(screen)


        pygame.display.flip()


    if mode == -1: #restart le jeu avec un appel réccursif
        mode=gameplay()
    return mode


