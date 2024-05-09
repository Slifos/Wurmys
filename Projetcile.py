import pygame
from math import *




class Projectile(pygame.sprite.Sprite) :
    def __init__(self,x_pos,z_pos,x_speed,z_speed,id):
        super().__init__()
        self.x_pos=x_pos
        self.z_pos=z_pos
        self.x_speed=x_speed
        self.z_speed=z_speed
        self.id=id
        self.speed=0
        self.grenade=pygame.image.load('images/grenade.png')
        self.grenade = pygame.transform.scale(self.grenade, [90,80])

   
    def draw(self,screen):
        

        screen.blit(self.grenade,(self.x_pos,self.z_pos))


    def vitesse(self,x,y):
        hauteur=abs(self.z_pos-y)
        longueur=abs(self.x_pos-x)
        if x<self.x_pos:
            longueur=-longueur

        
        vitesse=sqrt((hauteur)**2+(longueur)**2)
        return hauteur+10,longueur,vitesse
    
    def lancement(self,hauteur,longueur,seconde,pos_dx,pos_dh):
        
                       
        
        self.z_speed=-941*seconde+pos_dh
        self.z_pos=((-941/2)*(seconde**2)+hauteur*seconde)*-1+pos_dh
        self.x_pos=longueur*seconde+pos_dx
        
       
        



    
    
    
    
    
    
    
    
    
    
    
    
    def vitesse_chute_libre(self,seconde):
            self.z_speed=9.81*seconde


    def gravity(self,largeur,seconde):
        bounce_stop=0.2
        if self.z_pos< largeur -self.radius :
            self.vitesse_chute_libre(seconde)
        else:
            print("SoOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOL")
            if self.z_speed> bounce_stop:
                self.z_speed=self.z_speed * (-1)* self.retention


            else:
                if abs(self.z_speed) <= bounce_stop:
                    self.z_speed=0
        print(self.z_speed)
        return self.z_speed
    def update(self):
        self.z_pos+=self.z_speed
        self.x_pos+=self.x_speed

   
        
