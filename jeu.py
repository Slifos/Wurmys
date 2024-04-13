import pygame
from player import player
from Inventaire import Inventaire
from Projetcile import *
import time 
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



Largeur,Hauteur=pygame.display.get_surface().get_size()

ball=Projectile(500,1000,10,5,.8,'green',0,0,1)

inventair=Inventaire()
fpsClock=pygame.time.Clock()    
sol=1010
while continuer:    
    draw_texte("Quitter jeu", font, Text_color, 1000, 700)
    screen.blit(bgjeu, (0,0 ))
    # ici on crée un rectangle de couleur rose, en x=0, y=0 et de taille 300 sur 200
    # nous verrons plus tard comment faire plus en détail :g)
    #faire apparaitre joueur
    screen.blit(player.image,player.rect)
    pos_dx=ball.x_pos
    pos_dh=ball.z_pos
    seconde=0
    pygame.mouse.set_visible(1)
    ball.draw(screen)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                continuer = False
        if event.type== pygame.KEYDOWN:
            if event.key==pygame.K_g:
                inventair.inven(True, screen)
                print("oui")
            
        if event.type== pygame.KEYDOWN:
            if event.key==pygame.K_z:
                
                buton_clicked=0
                print ("oonsgoognsgsngon\n\toj")
                while  buton_clicked==0:
                    for event2 in pygame.event.get() :
                        
                        if event2.type == pygame.MOUSEBUTTONDOWN:
                                    
                            print("fongalacouaqui")  
                                    
                            x,y =pygame.mouse.get_pos()
                            buton_clicked=1     
                            hauteur,longueur,vitesse=ball.vitesse(x,y)     
                
                            
                print(seconde,"la ici \n")
                bo=0
                while ball.z_pos<sol:
                    
                            
                            
                            
                            
                    ball.lancement(hauteur,longueur,seconde,pos_dx,pos_dh)
                    
                    screen.blit(bgjeu, (0,0 ))
                    screen.blit(player.image,player.rect)
      
                    ball.draw(screen)
                    
                    seconde+=0.01
                    bo=1
                    pygame.display.flip()




                   
    
           
    fpsClock.tick(220)
    # ici on actualise l'écran, car on a affiché un rectangle rose, et on veut qu'il soit
    # visible. Si l'on avait pas mit cette instruction, on n'aurait jamais vu le rectangle !
    pygame.display.flip()

pygame.quit()