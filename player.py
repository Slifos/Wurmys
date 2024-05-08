import pygame
from pygame.locals import *
from math import *
from son import *
#Representation du joueur

class Player(pygame.sprite.Sprite):

    def __init__(self,skin,position):
        """skin = choix de l'apparence du ver, w,h = position x,y de départ du ver"""
        super().__init__()
        self.screen = pygame.display.get_surface()
        self.w, self.h = self.screen.get_width(), self.screen.get_height()
        self.health = 100
        self.max_health = 100
        if skin == "A":
            self.idle = "perso/worm_idle_A.png"
            self.death = "perso/worm_walking_A.png"
            self.jump = "perso/worm_jump_A.png"
            self.jumping = "perso/worm_jumping_A.png"
        if skin == "B":
            self.idle = "perso/worm_idle_B.png"
            self.death = "perso/worm_walking_B.png"
            self.jump = "perso/worm_jump_B.png"
            self.jumping = "perso/worm_jumping_B.png"

        self.sensi = 0.14
        self.attacking = False
        self.isjumping = False
        self.w_worm = self.w * 0.035
        self.spray = pygame.image.load(self.idle)
        self.image_worm = pygame.transform.scale(self.spray, (self.w_worm, self.w_worm * 1.85))

        self.hit=0
        self.rect = self.image_worm.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.cd_attacking = 0
        self.viser = 0
        self.viser_x = 0
        self.viser_y = 0
        self.epee_image = "objet/epee2.png"
        self.degat_epee = 30
        self.w_epee = self.w*0.05
        self.ratio_epee = (self.w_epee, self.w_epee)
        self.g = self.h * 0.0025  # calcule la gravité en fonction de la hauteur de l'écran
        self.vitesse = self.w * 0.0035  # calcule la vitesse gauche droite en fonction de la taille de l'écran
        self.floor = self.h * 0.72  # ordonnée ou se situe le sol
        self.w_worm = self.w * 0.035
        self.spray = pygame.image.load(self.idle)
        self.image_worm = pygame.transform.scale(self.spray,
                                                 (self.w_worm, self.w_worm * 1.85))  # adapte la taille du ver à l'écran
        if position[0]>self.w*0.5:
            self.image_worm = pygame.transform.flip(self.image_worm,True,False)
        self.falling = False





        """===============================================================ACTION================================================================================="""
    def move_right(self):
        if not self.falling:
            self.rect.x += self.vitesse
            self.vitesse_x = self.vitesse/2.5
            self.sens = 1#sert pour le saut
            self.rect.y = self.rect.y + self.h * 0.001 * sin(self.rect.x)
        self.image_worm = pygame.image.load(self.idle)
        self.image_worm = pygame.transform.scale(self.image_worm,
                                                 (self.w_worm, self.w_worm * 1.85))
    def move_left(self):
        if not self.falling :
            self.rect.x -= self.vitesse
            self.vitesse_x = -self.vitesse/3.5
            self.sens =-1#sert au saut
            self.rect.y = self.rect.y-self.h*0.001*sin(self.rect.x+7)

        self.image_worm = pygame.image.load(self.idle)
        self.image_worm = pygame.transform.scale(self.image_worm,
                                                 (self.w_worm, self.w_worm * 1.85))
        self.image_worm = pygame.transform.flip(self.image_worm,True,False)

    def aim_left(self):
        self.viser -=self.sensi
    def aim_right(self):
        self.viser +=self.sensi
    def take_damage(self,damage):

        self.health -=damage
        if self.health<=0:
            self.health = 0
            self.ratio_death = self.w * 0.035, self.w * 0.035 * 0.46
            self.image_worm = pygame.image.load(self.death)
            self.image_worm = pygame.transform.scale(self.image_worm, self.ratio_death)
            play_sound("sound/death.mp3")
            play_sound("sound/victory_effect.mp3")
        else:
            if self.hit%3==0:

                play_sound("sound/get_hit.mp3")
            elif self.hit%3==1:
                play_sound("sound/get_hit2.mp3")
            else:
                play_sound("sound/get_hit3.mp3")
            self.hit+=1
    def attack(self, T_joueur):
        """récupère l'endroit viser par l'arme le joueur qui attaque
        et un tableau des joueurs et leur coordonnées pour voir si ils recoivent les damages"""

        if self.attacking==False:
            #couldown avant de pouvoir réattaquer
            self.cd_attacking = 0
            self.attacking=True
            hit = 0
            coord_x,coord_y=self.viser_x,self.viser_y
            for joueur in T_joueur:
                if  joueur != self:
                    self.slash = pygame.image.load("objet/slash.png")
                    self.slash= pygame.transform.scale(self.slash, (self.ratio_epee))
                    self.rect_slash = self.slash.get_rect()
                    self.rect_slash.x,self.rect_slash.y = (self.viser_x-self.ratio_epee[0]/2,self.viser_y)
                    if self.viser_x < self.rect.x+self.w_worm/2:
                        self.slash = pygame.transform.flip(self.slash,True,False)
                    self.screen.blit(self.slash,(self.rect_slash.x,self.rect_slash.y))
                    if self.rect_slash.colliderect(joueur.rect):
                        joueur.take_damage(self.degat_epee)
                        play_sound("sound/slash_hit.mp3")
                        hit =1
            if hit == 0:
                play_sound("sound/slash.mp3")


    def do_jump(self):
        """Action de sauté en fonction des inputs de vitesses (gauche, droite)"""
        #détecte si il peut sauter (ex: tu ne peux pas sauter dans les aires)
        if not self.falling:
            self.vitesse_y = self.vitesse*1.3 #vitesse du saut
            self.t = 1 #génération artificielle du temps
            #génére le commencement du saut
            self.rect.x += self.vitesse_x * self.t
            self.rect.y -= self.vitesse_y * self.t - (1 / 2) * self.g * self.t * self.t
            #changement d'état après le saut
            self.falling = True
            self.isjumping = True



    """============================================Mise à jour constante du jeu ================================================================================================="""
    def is_alive(self):
        if self.health>0:
            return True
        return False
    def update(self):
        """Permets de maj les vecteurs vitesses en fonction de si le joueur bouge ou non
        cela sert pour les trajectoires de saut"""

        self.rayon = self.w * 0.044
        self.viser_x = self.rect.x + self.w_worm / 2 + cos(self.viser) * self.rayon
        self.viser_y = self.rect.y + self.w_worm * 1.85 / 2 + sin(self.viser) * self.rayon

        if not self.falling:
            self.vitesse_x = 0
            self.vitesse_y = 0
        if self.cd_attacking<7:#temps limite avant de pouvoir reattaquer
            self.cd_attacking+=0.1
        else:
            self.attacking = False
    def in_aire(self):
        """Fonction qui détecte se qu il se passe en état de chute
        cette fonction est lié au saut"""
        if self.falling:
            #fonction des lois des mouvement de newton si il détecte que l'on tombe
            self.rect.x += self.vitesse_x*self.t
            self.rect.y -= self.vitesse_y*self.t -(1/2)*self.g*self.t*self.t
            self.t+= self.vitesse*0.03

        if self.rect.y >= self.floor:
            #détecte si le joueur a attéri pour changer d'état
            self.isjumping = False
            self.falling = False

    def collision(self):
        """calcule si le joueur respecte bien les collision
        sinon sa position ne change pas"""
        #collision avec les bords de map
        if self.rect.x <0:
            self.rect.x = 0
        if self.rect.x >self.w*0.97:
            self.rect.x=self.w*0.97


    """============================================AFFICHAGE==============================================================="""




    def update_health_bar(self):
        """affichage de la barre de vie"""
        pygame.draw.line(self.screen, (150, 0, 0), (self.rect.x-self.w*0.02, self.rect.y-self.h*0.05),
                         (self.rect.x-self.w*0.02+self.w*0.08, self.rect.y - self.h*0.05), int(self.h*0.02))
        pygame.draw.line(self.screen, (0, 150, 0), (self.rect.x - self.w * 0.02, self.rect.y - self.h * 0.05),
                         (self.rect.x-self.w*0.02 + self.w*0.08*(self.health/self.max_health), self.rect.y - self.h * 0.05), int(self.h * 0.02))



    def cursor(self):
        """affichage du curseur pour viser"""
        pygame.draw.circle(self.screen, (150, 0, 0), (self.viser_x,self.viser_y),
                         5, int(self.h * 0.02))



    def affichage_final(self):

        self.coord_arme_x = self.rect.x
        self.coord_arme_y = self.rect.y
        self.dx = self.viser_x - self.coord_arme_x
        self.dy = self.viser_y - self.coord_arme_y
        self.angle = degrees(atan2(-self.dy, self.dx))
        self.image_arme = pygame.image.load(self.epee_image)
        self.image_arme = pygame.transform.scale(self.image_arme,(self.ratio_epee))

        self.image_arme = pygame.transform.rotate(self.image_arme,-90+self.angle)
        self.screen.blit(self.image_worm, (self.rect.x, self.rect.y))
        self.screen.blit(self.image_arme, (self.rect.x-self.w_epee/4,self.rect.y-self.w_epee/10))
        self.update_health_bar()
        self.cursor()


