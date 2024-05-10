import pygame
from fonction import*
from math import *
from Projectile import*
#Representation du joueur

class Player(pygame.sprite.Sprite):

    def __init__(self,skin,position,option):
        """skin = choix de l'apparence du ver, w,h = position x,y de départ du ver"""
        super().__init__()
        self.option = option
        self.screen = pygame.display.get_surface()
        self.w, self.h = self.screen.get_width(), self.screen.get_height()
        self.health = 100
        self.max_health = 100

        if skin == "A":
            self.idle = "perso/worm_idle_A.png"
            self.death = "perso/worm_walking_A.png"
        if skin == "B":
            self.idle = "perso/worm_idle_B.png"
            self.death = "perso/worm_walking_B.png"

        self.worm = Image(self.idle, self.w * 0.035, (position))
        self.alive = True
        self.sensi = 0.14
        self.direction =-1
        self.attacking = False
        self.isjumping = False

        self.T_fleche = []
        self.hit=0
        self.cd_attacking = 0
        self.viser = 0
        self.viser_x = 0
        self.viser_y = 0
        self.vitesse = self.w * 0.0035
        self.L_projectile = []

        if position[0]>self.w*0.5:
            self.worm.flip()
            self.direction = 1
        self.falling = False
        self.arme_init()
    def arme_init(self):
        self.tir = False
        self.attacking = False
        self.flip = False
        self.arc = Image("objet/bow.png", self.w * 0.02, (self.worm.rect.x, self.worm.rect.y))
        self.arc_degats = 20
        self.tir_arc = False
        self.s_bow = 10

        self.epee = Image("objet/epee2.png", self.w * 0.05, (self.worm.rect.x, self.worm.rect.y))
        self.slash = Image("objet/slash.png",self.w*0.06,(0,0))
        self.epee_degats = 25
        self.s_epee = 10
        self.tir_epee = False


        self.s_switch =10
        self.arme_image =self.epee.image
        self.arme = 1
        self.degats = self.epee_degats
        self.s_switch = 10

    def arme_switch(self):



        if self.switching==False:
            self.s_switch = 0
            self.switching = True
            self.arme += 1
            if self.arme %2 == 1:
                self.arme_image = self.epee.image
                self.degats = self.epee_degats

            else:
                self.arme_image = self.arc.image
                self.degats = self.arc_degats

    def attack_epee(self, T_joueur):
        """récupère l'endroit viser par l'arme le joueur qui attaque
        et un tableau des joueurs et leur coordonnées pour voir si ils recoivent les damages"""
        hit = 0
        if self.tir_epee==False:
            #couldown avant de pouvoir réattaquer

            self.tir_epee=True
            self.s_epee = 0
            for joueur in T_joueur:
                if  joueur != self:
                    self.slash.go_center(self.viser_x,self.viser_y)
                    slash_hit = self.slash.image
                    slash_hit = pygame.transform.rotate(slash_hit,self.angle)
                    self.screen.blit(slash_hit,(self.slash.rect))
                    if self.slash.rect.colliderect(joueur.worm.rect):
                        joueur.take_damage(self.degats)
                        play_sound("sound/slash_hit.mp3",0.5,self.option.volume)
                        hit =1
            if hit == 0:
                play_sound("sound/slash.mp3",0.5,self.option.volume)

    def attack_arc(self,T_joueur):
        if self.tir_arc ==False:
            self.tir_arc=True
            self.s_bow=0
            play_sound("sound/bow_shot.mp3",0.5,self.option.volume)
            self.vitesse_fleche_x = self.viser_x - self.worm.get_center()[0]
            self.vitesse_fleche_y = self.viser_y - self.worm.get_center()[1]
            print(self.viser_x,self.worm.get_center()[0], self.worm.rect.x+self.worm.get_center()[0] , self.worm.rect.y+self.worm.get_center()[1])
            tir = Fleche(self,self.vitesse_fleche_x,self.vitesse_fleche_y,self.viser_x,self.viser_y,T_joueur)
            self.T_fleche.append(tir)

    def cd_bow(self, max):
        if self.s_bow<max:
            self.s_bow+=0.02
        else:
            self.tir_arc = False
    def cd_epee(self, max):
        if self.s_epee<max:
            self.s_epee+=0.02
        else:
            self.tir_epee = False
    def cd_switch(self,max):
        if self.s_switch<max:
            self.s_switch+=0.02
        else:
            self.switching = False


    def attack(self,T_joueur):
        if self.arme % 2 == 1:

            self.attack_epee(T_joueur)
        else:
            self.attack_arc(T_joueur)
    def affichage_arme(self):

        self.dx = self.viser_x - self.worm.get_center()[0]
        self.dy = self.viser_y - self.worm.get_center()[1]
        self.angle = degrees(atan2(-self.dy, self.dx))

        if self.arme % 2 == 1:
            self.epee.go_center(self.worm.get_center()[0], self.worm.get_center()[1])
            self.degats = self.arc_degats

            self.arme_image = pygame.transform.rotate(self.epee.image, self.angle)
            self.arme_rect = self.epee.rect

        else:
            self.arc.go_center(self.worm.get_center()[0],self.worm.get_center()[1])
            self.degats = self.arc_degats
            self.arme_image = pygame.transform.rotate(self.arc.image, self.angle)
            self.arme_rect = self.arc.rect

        self.screen.blit(self.arme_image, self.arme_rect)




        """===============================================================ACTION================================================================================="""
    def move_right(self):
        if not self.falling:
            self.worm.rect.x += self.vitesse
            self.vitesse_x = self.vitesse/5
            self.sens = 1#sert pour le saut
            self.worm.rect.y = self.worm.rect.y + self.h * 0.001 * sin(self.worm.rect.x)
        self.vitesse_vol = self.vitesse/5
        if self.direction==1:
            self.direction=-1
            self.worm.flip()
    def move_left(self):
        if not self.falling :
            self.worm.rect.x -= self.vitesse
            self.vitesse_x = -self.vitesse/5
            self.sens =-1#sert au saut
            self.worm.rect.y = self.worm.rect.y-self.h*0.001*sin(self.worm.rect.x+7)
        self.vitesse_vol = -self.vitesse / 5
        if self.direction==-1:
            self.direction=1
            self.worm.flip()

    def aim_left(self):
        self.viser -=self.sensi
    def aim_right(self):
        self.viser +=self.sensi
    def take_damage(self,damage):

        self.health -=damage
        if self.health<=0:
            self.health = 0
            self.worm.switch_image(self.death,self.w*0.2)
            self.alive = False
            self.dodge = True
            play_sound("sound/death.mp3",0.5,self.option.volume)
            play_sound("sound/victory_effect.mp3",0.5,self.option.volume)
        else:
            if self.hit%3==0:

                play_sound("sound/get_hit.mp3",0.5,self.option.volume)
            elif self.hit%3==1:
                play_sound("sound/get_hit2.mp3",0.5,self.option.volume)
            else:
                play_sound("sound/get_hit3.mp3",0.5,self.option.volume)
            self.hit+=1


    def go_down(self):
        self.g = self.g + 0.0007*self.h
    def do_jump(self):
        """Action de sauté en fonction des inputs de vitesses (gauche, droite)"""
        #détecte si il peut sauter (ex: tu ne peux pas sauter dans les aires)
        if not self.falling:
            self.vitesse_y = self.vitesse*1.3 #vitesse du saut
            self.t = 1 #génération artificielle du temps
            #génére le commencement du saut
            self.worm.rect.x += (self.vitesse_x+self.vitesse_vol) * self.t
            self.worm.rect.y -= self.vitesse_y * self.t - (1 / 2) * self.g * self.t * self.t
            #changement d'état après le saut
            self.falling = True
            self.isjumping = True



    """============================================Mise à jour constante du jeu ================================================================================================="""

    def update(self,T_joueur):
        """Permets de maj les vecteurs vitesses en fonction de si le joueur bouge ou non
        cela sert pour les trajectoires de saut"""

        self.rayon = self.w * 0.044
        self.viser_x = self.worm.get_center()[0] + cos(self.viser) * self.rayon
        self.viser_y = self.worm.get_center()[1] + sin(self.viser) * self.rayon
        self.g = self.h * 0.0025
        self.vitesse_vol = 0
        self.cd_bow(1.2)
        self.cd_epee(1)
        self.cd_switch(0.3)
        if not self.alive:
            self.worm.rect.y = self.worm.rect.y - self.h * 0.8
        if not self.falling:
            self.vitesse_x = 0
            self.vitesse_y = 0



    def in_aire(self):
        """Fonction qui détecte se qu il se passe en état de chute
        cette fonction est lié au saut"""
        if self.falling:
            #fonction des lois des mouvement de newton si il détecte que l'on tombe
            self.worm.rect.x += (self.vitesse_x+self.vitesse_vol)*self.t
            self.worm.rect.y -= self.vitesse_y*self.t -(1/2)*self.g*self.t*self.t
            self.t+= self.vitesse*0.03



    def collision(self,T_platform):
        """calcule si le joueur respecte bien les collision
                sinon sa position ne change pas"""
        for platform in T_platform:

            if self.worm.rect.colliderect(platform.platform_rect) and self.worm.rect.bottom > platform.platform_rect.top and self.worm.rect.top<platform.platform_rect.bottom:
                self.falling=False
                break


            else:
                if self.falling==False:

                    self.t = 0
                    self.falling=True


        #collision avec les bords de map
        if self.worm.rect.x <0:
            self.worm.rect.x = 0
        if self.worm.rect.x >self.w*0.97:
            self.worm.rect.x=self.w*0.97


    """============================================AFFICHAGE==============================================================="""




    def update_health_bar(self):
        """affichage de la barre de vie"""
        pygame.draw.line(self.screen, (150, 0, 0), (self.worm.rect.x-self.w*0.02, self.worm.rect.y-self.h*0.05),
                         (self.worm.rect.x-self.w*0.02+self.w*0.08, self.worm.rect.y - self.h*0.05), int(self.h*0.02))
        pygame.draw.line(self.screen, (0, 150, 0), (self.worm.rect.x - self.w * 0.02, self.worm.rect.y - self.h * 0.05),
                         (self.worm.rect.x-self.w*0.02 + self.w*0.08*(self.health/self.max_health), self.worm.rect.y - self.h * 0.05), int(self.h * 0.02))



    def cursor(self):
        """affichage du curseur pour viser"""
        pygame.draw.circle(self.screen, (150, 0, 0), (self.viser_x,self.viser_y),
                         5, int(self.h * 0.02))
    def affichage_final(self):
        self.screen.blit(self.worm.image, (self.worm.rect.x,self.worm.rect.y))
        self.affichage_arme()
        self.update_health_bar()
        self.cursor()

        i=0
        while i<len(self.T_fleche):
            self.T_fleche[i].update(self.option)
            if self.T_fleche[i].t>3:
                del(self.T_fleche[i])
            else:
                i+=1


