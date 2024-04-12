import pygame
from math import *




class Projectile(pygame.sprite.Sprite) :
    def __init__(self,x_pos,z_pos,radius,mass,retention,color,x_speed,z_speed,id):
        super().__init__()
        self.x_pos=x_pos
        self.z_pos=z_pos
        self.radius=radius
        self.color=color
        self.mass=mass
        self.retention=retention
        self.x_speed=x_speed
        self.z_speed=z_speed
        self.id=id
        self.circle= ''
        self.speed=0
        
   
    def draw(self,screen):

        self.circle=pygame.draw.circle(screen,self.color,(self.x_pos,self.z_pos),self.radius)


    def vitesse(self,x,y):
        hauteur=abs(self.z_pos-y)
        longueur=abs(self.x_pos-x)
        vitesse=sqrt((hauteur)**2+(longueur)**2)
        return hauteur,longueur,vitesse
    
    def lancement(self,hauteur,longueur,seconde):
        
                       
        
        print("seconde: ",seconde,"\n")
        self.z_speed=-941*seconde+1000
        self.z_pos=((-941/2)*(seconde**2)+1000*seconde)*-1+1000
        self.x_pos=700*seconde
        print("Z :" ,self.z_pos,"\t Zspeed: ",self.z_speed)
        print("X:",self.x_pos)
        



    
    
    
    
    
    
    
    
    
    
    
    
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

   
        
