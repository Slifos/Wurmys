import pygame


#Representation du jeu
def play_music(file_path):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.stop()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)

def play_sound(file_path):
    pygame.init()
    pygame.mixer.init()
    sound = pygame.mixer.Sound(file_path)
    sound.set_volume(0.5)
    sound.play()
