import pygame

class player(pygame.sprite.Sprite) :
    def __init__(self) :
        super().__init__()
        self.health =100
        self.maxhealth= 100
        self.attack= 10
        self.velocity= 5
        self.image = pygame.image.load('images/Worms.png')
        self.image = pygame.transform.scale(self.image, [120,120])


        self.rect = self.image.get_rect()
        self.rect.y= 700