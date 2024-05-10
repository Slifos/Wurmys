import pygame

"""Fonctions liées à la simplification de l'outil pygame"""

class Image:
    def __init__(self,path,ratio,position):
        pygame.init()

        super().__init__()
        self.image = pygame.image.load(path)


        w=self.image.get_width()*ratio
        l = self.image.get_height()*ratio
        self.ratio_image =l/w
        self.dimension = (ratio,ratio*self.ratio_image)

        self.image = pygame.transform.scale(self.image,self.dimension)

        self.rect = self.image.get_rect()
        self.dim_x,self.dim_y = self.image.get_width(),self.image.get_height()
        self.rect.x = position[0]
        self.rect.y = position[1]



    def switch_image(self,path, ratio):
        self.image = pygame.image.load(path)
        w = self.image.get_width() * ratio
        l = self.image.get_height() * ratio
        self.ratio_image = l / w
        self.dimension = (ratio, ratio * self.ratio_image)
        self.image = pygame.transform.scale(self.image, self.dimension)
    def get_center(self):
        self.center_x, self.center_y = self.rect.x + self.dim_x / 2, self.rect.y + self.dim_y / 2
        return self.center_x,self.center_y
    def go_center(self,center_x,center_y):
        self.center_x = center_x
        self.center_y = center_y
        self.rect.x,self.rect.y=self.center_x-self.dim_x/2,self.center_y-self.dim_y/2
    def flip(self):
        self.image = pygame.transform.flip(self.image,True,False)





def couldown(max,seconde,fin):
    """Permet de définir un temps d'attente en fonction du
    nb de seconde max, des seconde actuel et de si l'attente est fini"""
    if not fin:
        seconde+=1
    return max,seconde,seconde>=max

def play_music(file_path,volume,option):
    pygame.mixer.init()
    pygame.mixer.music.stop()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.set_volume(volume*option)
    pygame.mixer.music.play(-1)

def play_sound(file_path,volume,option):
    pygame.mixer.init()
    sound = pygame.mixer.Sound(file_path)
    sound.set_volume(volume*option)
    sound.play()

