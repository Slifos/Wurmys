import pygame
from Player import player
from Inventaire import Inventaire
from Projetcile import *
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
pos_d=500
inventair=Inventaire()
fpsClock=pygame.time.Clock()
while continuer:    
    draw_texte("Quitter jeu", font, Text_color, 1000, 700)
    screen.blit(bgjeu, (0,0 ))
    # ici on crée un rectangle de couleur rose, en x=0, y=0 et de taille 300 sur 200
    # nous verrons plus tard comment faire plus en détail :g)
    #faire apparaitre joueur
    screen.blit(player.image,player.rect)
    
    
    temps=0
    seconde=0
    pygame.mouse.set_visible(1)
    
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
                
                while  buton_clicked==0:
                    event2= pygame.event.poll()
                        
                    if event2.type == pygame.MOUSEBUTTONDOWN:
                                
                        print("oui")  
                                
                        x,y =pygame.mouse.get_pos()
                        ball.angle=ball.get_angle(x,y)
                        print(x,y)
                        buton_clicked=1                       
                    while ball.z_pos<1700:
                        print(seconde)
                        print("45")               
                        print("angle",ball.angle)  

                        ball.lancement(screen,seconde,pos_d)
                        seconde=(pygame.time.get_ticks() - temps) /1000
                        pygame.display.flip()
                       

                   

                
    #fpsClock.tick(60)
    # ici on actualise l'écran, car on a affiché un rectangle rose, et on veut qu'il soit
    # visible. Si l'on avait pas mit cette instruction, on n'aurait jamais vu le rectangle !
    pygame.display.flip()

pygame.quit()