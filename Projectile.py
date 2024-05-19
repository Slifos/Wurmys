import pygame
from math import *
from fonction import*
import math


class Fleche(pygame.sprite.Sprite) :
    def __init__(self,lanceur,vitesse_x,vitesse_y,position_depart_x,position_depart_y,T_joueur):
        """récupère toutes les propriétés de la flèche pour pouvoir la lancer à la bonne position
        et de manière cohérente"""
        super().__init__()
        screen = pygame.display.get_surface()
        self.w,self.h = screen.get_size()
        self.lanceur = lanceur
        self.T_joueur = T_joueur
        self.screen = pygame.display.get_surface()
        self.w, self.h = self.screen.get_width(), self.screen.get_height()
        self.angle2 = degrees(atan2(-vitesse_x, -vitesse_y))
        self.gravity = self.h*0.6
        self.vitesse_x = vitesse_x*20
        self.vitesse_y = -vitesse_y*20
        self.position_depart=(position_depart_x,position_depart_y)
        self.fleche = Image("objet/arrow.png",self.w*0.01,(self.position_depart[0],self.position_depart[1]))
        self.fleche.image = pygame.transform.rotate(self.fleche.image,self.angle2)
        self.damage=10
        self.t = 0

    def update(self,option):
        """affichage continu de la flèche + vérifie la collision avec les joueurs non lanceurs"""
        self.t+=0.01
        self.fleche.rect.x = self.position_depart[0] + self.vitesse_x*self.t
        self.fleche.rect.y = self.position_depart[1] -self.vitesse_y*self.t +(1/2)*self.gravity*self.t*self.t
        for joueur in self.T_joueur:
            if joueur!=self.lanceur:
                if joueur.worm.rect.collidepoint(self.fleche.rect.x,self.fleche.rect.y):
                    joueur.take_damage(self.damage)
                    play_sound("sound/arrow_hit.mp3",  option)
                    self.t=100
        self.screen.blit(self.fleche.image, self.fleche.rect)

