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
        self.angle=3.141592/4
    def get_angle(self,x,y):

        angle=atan(y/x)
        return angle 
    def draw(self,screen):

        self.circle=pygame.draw.circle(screen,self.color,(self.x_pos,self.z_pos),self.radius)
    
    def lancement(self,screen,seconde,pos_d):
        sol=1700
        
        

        self.z_speed=-9.81*seconde+sin(3.141592/6)*220
        self.z_pos=((-9.81/2)*(seconde**2)+(sin(3.14/4)*1000)*seconde+pos_d)*-1+1000
        self.x_pos=(cos(3.14/4)*1000)*seconde+500
        print("Z :" ,self.z_pos)
        pygame.display.flip()




    
    
    
    
    
    
    
    
    
    
    
    
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

   
        
