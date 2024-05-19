import pygame
"""option du jeu permet de changer les paramètre du jeu tel que la vie,le nombre de joueur sur le terrain le pseudo et les skin des vers"""
class Option:
    def __init__(self):
        self.screen = pygame.display.get_surface()

        self.w,self.h = self.screen.get_width(),self.screen.get_height()

        self.volume = 0.1
        self.joueurs = [Joueur(0), Joueur(1)]
        self.nb_joueurs = 2

        #game
        self.max_vie = 3
        self.T_vie = []
        self.T_joueurs=[]
        self.T_platform = []




class Joueur():
    def __init__(self,id):
        if id ==0:

            self.pseudo = "Yukali"
            self.skin= "thug"
        if id == 1:
            self.pseudo = "Toxies"
            self.skin = "chad"


