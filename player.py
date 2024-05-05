import pygame



#Representation du joueur

class Player(pygame.sprite.Sprite):

    def __init__(self,skin):
        super().__init__()

        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.all_projectiles = pygame.sprite.Group()
        self.arme="" 
        self.isjumping = False
        if skin == "A":
            self.idle = "perso/worm_idle_A.png"
            self.walk = "perso/worm_walking_A.png"
            self.jump = "perso/worm_jump_A.png"
            self.jumping = "perso/worm_jumping_A.png"
    def update_setting(self,w,h):
        self.w = w
        self.h = h
        self.w_worm = w * 0.035
        self.spray = pygame.image.load("perso/worm_idle_A.png")
        self.image = pygame.transform.scale(self.spray, (self.w_worm, self.w_worm * 1.85))
        self.rect = self.image.get_rect()
        self.g = h * 0.0025
        self.jump_power = h * 0.05
        self.velocity_y = self.jump_power/5
        self.floor = h * 0.72
        self.rect_x = w * 0.1
        self.rect_y = h * 0.72
        self.w_worm = w * 0.035
        self.vitesse = w * 0.003
        self.falling= False
        self.jump_limit = self.h*0.23
        self.jump_start = 0
        print(self.h * 0.0025)

    def update(self):
        if not self.falling:

            self.vitesse_x = 0
            self.vitesse_y = 0
    #mouvement
    def move_right(self):
        if not self.falling:
            self.rect_x += self.vitesse
            self.vitesse_x = self.vitesse/2.5
    def move_left(self):
        if not self.falling:
            self.rect_x -= self.vitesse
            self.vitesse_x = -self.vitesse/3.5
    def do_jump(self):
        if not self.falling:
            self.vitesse_y = self.vitesse*1.3
            self.jump_start_x = self.rect_x
            self.jump_start_y = self.rect_y
            self.t = 1
            self.falling = True
            self.isjumping=True
            self.rect_x += self.vitesse_x * self.t
            self.rect_y -= self.vitesse_y * self.t - (1 / 2) * self.g * self.t * self.t
            print('jump')
    def in_aire(self):
        if self.falling:
            self.rect_x += self.vitesse_x*self.t
            self.rect_y -= self.vitesse_y*self.t -(1/2)*self.g*self.t*self.t
            self.t+= self.vitesse*0.03
            print("falling")
        if self.rect_y >= self.floor:
            print("terre")
            self.isjumping = False
            self.falling = False


        """if self.isjumping and not self.falling:
            self.rect_y -= self.velocity_y
        if self.falling:
            print("gravité")
            self.rect_y += self.gravity

        if self.rect_y <=(self.jump_start-self.jump_limit):
            self.falling = True

        if self.rect_y >= self.floor:
            print("lolu")
            self.isjumping = False
            self.falling = False"""
