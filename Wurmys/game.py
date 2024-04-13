import pygame
from player import Player

#Representation du jeu
class Game:
    def __init__(self):
        #generer le joueur
        self.player = Player()
        self.pressed = {}
