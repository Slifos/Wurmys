import pygame

"""Fonctions liées à la simplification de l'outil pygame"""

class Image:
    """génère une image et permet de récupéré toutes ses propriétés ainsi que les changer
    outil bcp plus optimal mais aussi plus simple pour la génération d'image"""
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
        """récupère les coord centrales de l'image"""
        self.center_x, self.center_y = self.rect.x + self.dim_x / 2, self.rect.y + self.dim_y / 2
        return self.center_x,self.center_y
    def go_center(self,center_x,center_y):
        """positionne par rapport au centre l'image"""
        self.center_x = center_x
        self.center_y = center_y
        self.rect.x,self.rect.y=self.center_x-self.dim_x/2,self.center_y-self.dim_y/2
    def flip(self):
        """interchange le sens de l'image de gauche vers la droite et inversement"""
        self.image = pygame.transform.flip(self.image,True,False)

class Image_h:
    """meme classe excepté que le ratio est fait en fonction de la hauteur de l'écran"""
    def __init__(self, path, ratio, position):
        pygame.init()

        super().__init__()
        self.image = pygame.image.load(path)

        w = self.image.get_width() * ratio
        l = self.image.get_height() * ratio
        self.ratio_image = w/l
        self.dimension = ( ratio* self.ratio_image, ratio)

        self.image = pygame.transform.scale(self.image, self.dimension)







def stop_music():
    pygame.mixer.init()
    pygame.mixer.music.stop()

def play_music(file_path,option):
    """joue une musique en boucle"""
    pygame.mixer.init()
    pygame.mixer.music.stop()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.set_volume(option.volume)
    pygame.mixer.music.play(-1)

def play_sound(file_path,option):
    """joue un son une fois"""
    pygame.mixer.init()
    sound = pygame.mixer.Sound(file_path)
    sound.set_volume(option.volume)
    sound.play()
def volume(volume):
    pygame.mixer.init()
    pygame.mixer.music.set_volume(volume)

def writting(word,espace):
    """permet de générer un mot sous la forme d'une image redimensionnée"""
    word=word.lower()
    screen = pygame.display.get_surface()
    w, h = screen.get_width(), screen.get_height()
    surface  = pygame.Surface((w,h),pygame.SRCALPHA)
    i=0

    for letter in word:
        if letter == "a":
            l = Image_h("alpha/a.png",espace,(0,0))
        elif letter == "b":
            l = Image_h("alpha/b.png",espace,(0,0))
        elif letter == "c":
            l = Image_h("alpha/c.png",espace,(0,0))
        elif letter == "d":
            l = Image_h("alpha/d.png",espace,(0,0))
        elif letter == "e":
            l = Image_h("alpha/e.png",espace,(0,0))
        elif letter == "f":
            l = Image_h("alpha/f.png",espace,(0,0))
        elif letter == "g":
            l = Image_h("alpha/g.png",espace,(0,0))
        elif letter == "h":
            l = Image_h("alpha/h.png",espace,(0,0))
        elif letter == "i":
            l = Image_h("alpha/i.png",espace,(0,0))
        elif letter == "j":
            l = Image_h("alpha/j.png",espace,(0,0))
        elif letter == "k":
            l = Image_h("alpha/k.png",espace,(0,0))
        elif letter == "l":
            l = Image_h("alpha/l.png",espace,(0,0))
        elif letter == "m":
            l = Image_h("alpha/m.png",espace,(0,0))
        elif letter == "n":
            l = Image_h("alpha/n.png",espace,(0,0))
        elif letter == "o":
            l = Image_h("alpha/o.png",espace,(0,0))
        elif letter == "p":
            l = Image_h("alpha/p.png",espace,(0,0))
        elif letter == "q":
            l = Image_h("alpha/q.png",espace,(0,0))
        elif letter == "r":
            l = Image_h("alpha/r.png",espace,(0,0))
        elif letter == "s":
            l = Image_h("alpha/s.png",espace,(0,0))
        elif letter == "t":
            l = Image_h("alpha/t.png",espace,(0,0))
        elif letter == "u":
            l = Image_h("alpha/u.png",espace,(0,0))
        elif letter == "v":
            l = Image_h("alpha/v.png",espace,(0,0))
        elif letter == "w":
            l = Image_h("alpha/w.png",espace,(0,0))
        elif letter == "x":
            l = Image_h("alpha/x.png",espace,(0,0))
        elif letter == "y":
            l = Image_h("alpha/y.png",espace,(0,0))
        elif letter == "z":
            l = Image_h("alpha/z.png",espace,(0,0))
        elif letter == "0":
            l = Image_h("alpha/0.png",espace,(0,0))
        elif letter == "1":
            l = Image_h("alpha/1.png",espace,(0,0))
        elif letter == "2":
            l = Image_h("alpha/2.png",espace,(0,0))
        elif letter == "3":
            l = Image_h("alpha/3.png",espace,(0,0))
        elif letter == "4":
            l = Image_h("alpha/4.png",espace,(0,0))
        elif letter == "5":
            l = Image_h("alpha/5.png",espace,(0,0))
        elif letter == "6":
            l = Image_h("alpha/6.png",espace,(0,0))
        elif letter == "7":
            l = Image_h("alpha/7.png",espace,(0,0))
        elif letter == "8":
            l = Image_h("alpha/8.png",espace,(0,0))
        elif letter == "9":
            l = Image_h("alpha/9.png",espace,(0,0))
        surface.blit(l.image,(espace/1.7*i,0))
        #pygame.image.save(surface, "mot.png")

        i+=1
    return surface
"""utile dans le futur"""
def input():
    taping = False
    while taping==False:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                running = False

                return event.key
