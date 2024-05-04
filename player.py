import pygame

#Representation du joueur

class Player(pygame.sprite.Sprite):

    def __init__(self,):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.vitesse = 2
        self.all_projectiles = pygame.sprite.Group()
        self.original_image = pygame.image.load("images/worm.png")
        self.image = pygame.transform.scale(self.original_image, (100, 60))  # Redimensionner l'image
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 800
        self.credit=0
        self.arme=""

    def move_right(self):
        self.rect.x += self.vitesse

    def move_left(self):
        self.rect.x -= self.vitesse

    def update_health_bar(self, surface):
        pygame.draw.rect(surface, (60, 63, 60), (self.rect.x + 30, self.rect.y - 20, self.max_health, 5), 7)
        pygame.draw.rect(surface, (111, 210, 46), (self.rect.x + 30, self.rect.y - 20, self.health, 5), 7)
