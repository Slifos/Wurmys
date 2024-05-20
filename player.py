import pygame
from fonction import*
from math import *
from Projectile import*
#Representation du joueur
"""fichier du joueur et de chacunes de ses propriétés (PV, attack, mouvement)"""
class Player(pygame.sprite.Sprite):

    def __init__(self,position,option,id):
        """position initial, option du jeu, id du joueur"""
        super().__init__()
        self.option = option
        self.screen = option.screen
        self.id = id


        self.alive = True
        self.health = 100
        self.max_health = 100


        self.skin_init(option.joueurs[id].skin)
        self.worm = Image(self.idle, self.option.w * 0.035, (position))
        self.meter = self.worm.image.get_height()
        self.floor = self.option.h * 0.7
        self.rayon_viser = self.option.w * 0.044

        self.seconde = 0.15
        self.direction =-1
        self.vitesse = self.meter*self.seconde/3
        self.vitesse_vol = 0
        self.viser_x,self.viser_y = 0,0
        self.viser = 0
        self.sensi = self.option.w*0.000045
        self.hit = 0
        self.pc = False
        self.T_fleche = []


        if position[0]>self.option.w*0.5:
            self.worm.flip()
            self.direction = 1
        self.falling = False
        self.arme_init()

    def skin_init(self,skin):
        """donne une apparence au ver"""
        if skin == "thug":
            self.idle = "skin/worm_idle_thug.png"
        elif skin == "masque":
            self.idle = "skin/worm_idle_masque.png"
        elif skin == "chad":
            self.idle = "skin/worm_idle_chad.png"
    def arme_init(self):
        """établie les setting par défauts de l'épée et de l'arc"""
        self.tir = False
        self.attacking = False
        self.flip = False
        self.arc = Image("objet/bow.png", self.option.w * 0.02, (self.worm.rect.x, self.worm.rect.y))
        self.arc_degats = 20
        self.tir_arc = False
        self.s_bow = 10

        self.epee = Image("objet/epee2.png", self.option.w * 0.05, (self.worm.rect.x, self.worm.rect.y))
        self.slash = Image("objet/slash.png",self.option.w*0.06,(0,0))
        self.epee_degats = 25
        self.s_epee = 10
        self.tir_epee = False


        self.s_switch =10
        self.arme_image =self.epee.image
        self.arme = 0
        self.degats = self.epee_degats
        self.s_switch = 10

    def arme_switch(self):
        """permet d'interchanger entre 2 armes (épée, arc)"""
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

    def attack_epee(self):
        """récupère l'endroit viser par l'arme le joueur qui attaque
        et un tableau des joueurs et leur coordonnées pour voir si ils recoivent les damages
        si l'image du slash touche l'image d'un autre joueur alors il recoit des dégats"""
        hit = 0
        if self.tir_epee==False:
            #couldown avant de pouvoir réattaquer

            self.tir_epee=True
            self.s_epee = 0
            for joueur in self.T_joueur:
                if  joueur != self:
                    self.slash.go_center(self.viser_x,self.viser_y)
                    slash_hit = self.slash.image
                    slash_hit = pygame.transform.rotate(slash_hit,self.angle)
                    self.screen.blit(slash_hit,(self.slash.rect))
                    if self.slash.rect.colliderect(joueur.worm.rect):
                        joueur.take_damage(self.degats)
                        play_sound("sound/slash_hit.mp3",self.option)
                        hit =1
            if hit == 0:
                play_sound("sound/slash.mp3",self.option)

    def attack_arc(self):
        """ lance un projectile temporaire qui vérifie si il est en collision avec tous les joueurs sur le terrain
        sauf le lanceur, si le projectile touche l'image d un autre joueur alors le projectile disparait pour laisser des dégats"""
        if self.tir_arc ==False:
            self.tir_arc=True
            self.s_bow=0
            play_sound("sound/bow_shot.mp3",self.option)
            self.vitesse_fleche_x = self.viser_x - self.worm.get_center()[0]
            self.vitesse_fleche_y = self.viser_y - self.worm.get_center()[1]
            tir = Fleche(self,self.vitesse_fleche_x,self.vitesse_fleche_y,self.viser_x,self.viser_y,self.T_joueur)
            self.T_fleche.append(tir)

    def cd_bow(self, max):
        """ couldown/ temps de récupération du tir à l'arc"""
        if self.s_bow<max:
            self.s_bow+=0.02
        else:
            self.tir_arc = False
    def cd_epee(self, max):
        """ couldown/ temps de récupération du coup d'épée"""
        if self.s_epee<max:
            self.s_epee+=0.02
        else:
            self.tir_epee = False
    def cd_switch(self,max):
        """ couldown/ temps de récupération du changement entre 2 armes"""
        if self.s_switch<max:
            self.s_switch+=0.02
        else:
            self.switching = False


    def attack(self):
        """ tire ou fait un coup d'épée en fonction de l'arme utilisée"""
        if self.arme % 2 == 1:

            self.attack_epee()
        else:
            self.attack_arc()
    def affichage_arme(self):
        """ affiche l'arme équipé, elle doit pointer dans la direction du curseur du joueur"""

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


    def move(self,x):
        """permet de se déplacer à la manette"""
        self.x_avant = self.worm.rect.x
        self.vitesse_vol += self.vitesse*x/4

        if not self.falling :
            self.worm.rect.x += self.vitesse*x
            self.vitesse_x = self.meter*x*1.5
            self.sens =-1#sert au saut
            if self.x_avant != self.worm.rect.x:
                self.worm.rect.y = self.worm.rect.y-self.option.h*0.00075*sin(self.worm.rect.x+7)

        if self.direction==-1 and x<0:
            self.direction=1
            self.worm.flip()
        if self.direction==1 and x>0:
            self.direction=-1
            self.worm.flip()
    def move_right(self):
        """permet de se déplacer à droite sur clavier"""
        if not self.falling:
            self.worm.rect.x += self.vitesse
            self.vitesse_x = self.meter*1.5
            self.sens = 1#sert pour le saut
            self.worm.rect.y = self.worm.rect.y + self.h * 0.001 * sin(self.worm.rect.x)
        self.vitesse_vol = self.vitesse/4
        if self.direction==1:
            self.direction=-1
            self.worm.flip()
    def move_left(self):
        """permet de se déplacer à gauche sur clavier"""
        if not self.falling :
            self.worm.rect.x -= self.vitesse
            self.vitesse_x = -self.meter*1.5
            self.sens =-1#sert au saut
            self.worm.rect.y = self.worm.rect.y-self.h*0.001*sin(self.worm.rect.x+7)
        self.vitesse_vol = -self.vitesse/4
        if self.direction==-1:
            self.direction=1
            self.worm.flip()
    def do_jump(self):
        """Action de sauté en fonction des inputs de vitesses (gauche, droite)"""
        #détecte si il peut sauter (ex: tu ne peux pas sauter dans les aires)
        if not self.falling:

            self.vitesse_y = self.meter*7#vitesse du saut
            self.t = 0.02 #génération artificielle du temps
            #génére le commencement du saut
            self.v0x = self.worm.rect.x
            self.v0y = self.worm.rect.y
            self.worm.rect.x = self.v0x+(self.vitesse_x) * self.t
            self.worm.rect.y = self.v0y-self.vitesse_y * self.t + (1 / 2) * self.g * self.t * self.t
            #changement d'état après le saut
            self.falling = True
    def in_aire(self):
        """Fonction qui détecte se qu il se passe en état de chute
        cette fonction est lié au saut"""
        if self.falling:
            #fonction des lois des mouvement de newton si il détecte que l'on tombe
            self.worm.rect.x = self.v0x +(self.vitesse_x+self.vitesse_vol)*self.t
            self.worm.rect.y = self.v0y -self.vitesse_y*self.t +(1/2)*self.g*self.t*self.t

            self.t+= 0.02
    def aim(self,x,y):
        """permet de viser à la manette en fonction du joystick droit"""

        self.viser_x = self.worm.get_center()[0] + x * self.rayon_viser
        self.viser_y = self.worm.get_center()[1] + y * self.rayon_viser
    def aim_left(self):
        """permet de viser à gauche en cercle autour du joueur avec le clavier"""
        self.pc = True
        self.viser -=self.sensi
    def aim_right(self):
        """permet de viser à droite en cercle autour du joueur avec le clavier"""
        self.pc = True
        self.viser +=self.sensi
    
    def take_damage(self,damage):
        """le joueur recoit des dégats"""

        self.health -=damage
        if self.health<=0:
            self.health = 0
            self.alive = False


        else:
            if self.hit%3==0:

                play_sound("sound/get_hit.mp3",self.option)
            elif self.hit%3==1:
                play_sound("sound/get_hit2.mp3",self.option)
            else:
                play_sound("sound/get_hit3.mp3",self.option)
            self.hit+=1






    """============================================Mise à jour constante du jeu ================================================================================================="""

    def update(self,option):
        """Mets à jour l'environment du joueur à chaque boucle tel que son curseur (PC), son image, ses collisions et son statut en jeu
        /!\ fonction super importante dans le fonctionnement du joueur"""

        self.option = option
        self.T_platform = option.T_platform
        self.T_joueur = option.T_joueurs

        if self.pc:
            self.viser_x = self.worm.get_center()[0] + cos(self.viser) * self.rayon_viser
            self.viser_y = self.worm.get_center()[1] + sin(self.viser) * self.rayon_viser
        self.g = self.meter*9.81
        self.w = option.w
        self.h= option.h

        self.cd_bow(1.2)
        self.cd_epee(1)
        self.cd_switch(0.3)
        if not self.falling:
            self.vitesse_y=0
            self.vitesse_vol = 0
        self.in_aire()
        self.collision()
        self.screen.blit(self.worm.image, (self.worm.rect.x, self.worm.rect.y))
        self.affichage_arme()
        self.update_health_bar()
        self.cursor()
        if self.falling==False:
            self.vitesse_x = 0

        i = 0
        while i < len(self.T_fleche):
            self.T_fleche[i].update(self.option)
            if self.T_fleche[i].t > 3:
                del (self.T_fleche[i])
            else:
                i += 1








    def collision(self):
        """calcule si le joueur respecte bien les collision entre les platforms, le sol et les cotés
                sinon sa position ne change pas"""
        for platform in self.T_platform:
            if self.worm.rect.colliderect(platform.platform_rect) and self.worm.rect.bottom >= platform.platform_rect.top and self.worm.rect.bottom < platform.platform_rect.top * self.h * 0.00136:  # and self.worm.rect.top<platform.platform_rect.bottom:
                self.falling = False
                break
            else:
                if self.falling==False:
                    self.falling= True
                    self.t = 0
                    self.v0x = self.worm.rect.x
                    self.v0y = self.worm.rect.y
        #collision avec les bords de map
        if self.worm.rect.x <0:
            self.worm.rect.x = self.option.w*0.97
            self.v0x = self.worm.rect.x-(self.vitesse_x)*self.t
        elif self.worm.rect.x >self.option.w*0.97:
            self.worm.rect.x=0
            self.v0x = self.worm.rect.x-(self.vitesse_x)*self.t
        if self.worm.rect.y > self.floor:
            self.falling = False
            if self.worm.rect.y>self.floor+self.option.h*0.05:
                self.worm.rect.y = self.floor


    """============================================AFFICHAGE==============================================================="""



    def update_health_bar(self):
        """affichage de la barre de vie au dessus du joueur"""
        pygame.draw.line(self.screen, (150, 0, 0), (self.worm.rect.x-self.option.w*0.02, self.worm.rect.y-self.option.h*0.05),
                         (self.worm.rect.x-self.option.w*0.02+self.option.w*0.08, self.worm.rect.y - self.option.h*0.05), int(self.option.h*0.02))
        pygame.draw.line(self.screen, (0, 150, 0), (self.worm.rect.x - self.option.w * 0.02, self.worm.rect.y - self.option.h * 0.05),
                         (self.worm.rect.x-self.option.w*0.02 + self.option.w*0.08*(self.health/self.max_health), self.worm.rect.y - self.option.h * 0.05), int(self.option.h * 0.02))
    def cursor(self):
        """affichage du curseur pour viser"""
        pygame.draw.circle(self.screen, (150, 0, 0), (self.viser_x,self.viser_y),
                         5, int(self.option.h * 0.02))





