import pygame
from pygame.locals import *


#Representation du joueur

class Player(pygame.sprite.Sprite):

    def __init__(self,skin,w,h):
        super().__init__()

        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.all_projectiles = pygame.sprite.Group()
        self.arme="" 
        self.isjumping = False
        self.rect_x = w * 0.1
        self.rect_y = h * 0.72
        if skin == "A":
            self.idle = "perso/worm_idle_A.png"
            self.walk = "perso/worm_walking_A.png"
            self.jump = "perso/worm_jump_A.png"
            self.jumping = "perso/worm_jumping_A.png"
    def update_setting(self,w,h):
        self.w = w
        self.h = h

        # génére l'image du ver avec des dimensions qui dépendent de l'écran
        self.w_worm = w * 0.035
        self.spray = pygame.image.load("perso/worm_idle_A.png")
        self.image = pygame.transform.scale(self.spray, (self.w_worm, self.w_worm * 1.85))#adapte la taille du ver à l'écran
        self.rect = self.image.get_rect() #dessine le ver

        self.g = h * 0.0025 #calcule la gravité en fonction de la hauteur de l'écran
        self.vitesse = w * 0.003 #calcule la vitesse gauche droite en fonction de la taille de l'écran
        self.floor = h * 0.72 #ordonnée ou se situe le sol

        self.falling= False

    def update(self):
        """Permets de maj les vecteurs vitesses en fonction de si le joueurnouge ou non
        cela sert pour les trajectoires de saut"""
        if not self.falling:

            self.vitesse_x = 0
            self.vitesse_y = 0
    #mouvement
    def move_right(self):
        if not self.falling:
            self.rect_x += self.vitesse
            self.vitesse_x = self.vitesse/2.5#sert pour le saut
    def move_left(self):
        if not self.falling:
            self.rect_x -= self.vitesse
            self.vitesse_x = -self.vitesse/3.5#sert au saut
    def do_jump(self):
        """Action de sauté en fonction des inputs de vitesses (gauche, droite)"""
        #détecte si il peut sauter (ex: tu ne peux pas sauter dans les aires)
        if not self.falling:
            self.vitesse_y = self.vitesse*1.3 #vitesse du saut
            self.t = 1 #génération artificielle du temps
            #génére le commencement du saut
            self.rect_x += self.vitesse_x * self.t
            self.rect_y -= self.vitesse_y * self.t - (1 / 2) * self.g * self.t * self.t
            #changement d'état après le saut
            self.falling = True
            self.isjumping = True
    def in_aire(self):
        """Fonction qui détecte se qu il se passe en état de chute
        cette fonction est lié au saut"""
        if self.falling:
            #fonction des lois des mouvement de newton si il détecte que l'on tombe
            self.rect_x += self.vitesse_x*self.t
            self.rect_y -= self.vitesse_y*self.t -(1/2)*self.g*self.t*self.t
            self.t+= self.vitesse*0.03

        if self.rect_y >= self.floor:
            #détecte si le joueur a attéri pour changer d'état
            self.isjumping = False
            self.falling = False

    def update_health_bar(self, screen):
        pygame.draw.line(screen, (150, 0, 0), (self.rect_x-self.w*0.02, self.rect_y-self.h*0.05),
                         (self.rect_x-self.w*0.02+self.w*0.08, self.rect_y - self.h*0.05), int(self.h*0.02))
        pygame.draw.line(screen, (0, 150, 0), (self.rect_x - self.w * 0.02, self.rect_y - self.h * 0.05),
                         (self.rect_x-self.w*0.02 + self.w*0.08*(self.health/self.max_health)*0.01, self.rect_y - self.h * 0.05), int(self.h * 0.02))
