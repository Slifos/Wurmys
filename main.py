import pygame
from pygame.locals import *
import math

pygame.init()

hauteur_fenetre = 780
largeur_fenetre = 1270
balle_largeur = 10
balle_hauteur = 10
v = 1
a = 0.1
norme = [0]*2

fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
fond = pygame.image.load("04.jpeg").convert()
balle = pygame.image.load("white-circle-free-png.png").convert_alpha()
balle = pygame.transform.scale(balle, [balle_largeur,balle_hauteur])
position_balle = (balle.get_rect())


continuer = True
while continuer :
	deplacement_y = 0
	deplacement_x = 0
	pygame.display.flip()
	fenetre.blit(fond, (0, 0))
	fenetre.blit(balle,(position_balle.left,position_balle.top))
	if position_balle.top < 980-balle_hauteur :
		position_balle.top += 1 * a
		a+=0.1
	if position_balle.top > hauteur_fenetre - balle_hauteur:
		position_balle.top = hauteur_fenetre-balle_hauteur
	for event in pygame.event.get():
		if event.type == pygame.MOUSEBUTTONDOWN:
			norme[0] = (event.pos[0])-(position_balle.center[0])
			norme[1] = (event.pos[1])-(position_balle.center[1])
			longueur = math.sqrt(norme[0]*norme[0]+norme[1]*norme[1])
			print(longueur)
			angle = math.acos(norme[0]/longueur)/(2*3.14159265359) * 360
			print(angle)
			if longueur > 1000 :
				longueur = 1000
			vitesse = (longueur * 2)/10
			deplacement_x = vitesse * math.cos((angle*2*3.14159265359)/360)/40
			deplacement_y = vitesse * math.sin((angle*2*3.14159265359)/360)/30
			a = 0.1
			verifa= 0
		if event.type == QUIT:
			continuer = False

	while deplacement_y != 0 or deplacement_x != 0 :
		pygame.display.flip()
		#fenetre.blit(fond, (0,0))
		fenetre.blit(balle, (position_balle.left, position_balle.top))
		position_balle.top -= deplacement_y
		print("x :   ",deplacement_x,"          y :", deplacement_y)
		deplacement_y -= (1*a)/10
		a+=0.005
		if verifa== 0 and deplacement_y<0 :
			a=0.1
			verifa=1
		position_balle.left += deplacement_x
		print("position top : ", position_balle.top)
		if position_balle.top >hauteur_fenetre-balle_hauteur :
			deplacement_y = 0
			deplacement_x = 0


	pygame.display.update()
pygame.quit()
