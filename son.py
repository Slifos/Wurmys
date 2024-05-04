import pygame
from player import Player

#Representation du jeu
def play_music(file_path):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.stop()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play(-1)

def play_sound(file_path):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.stop()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()