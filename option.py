import pygame

class Option:
    def __init__(self):
        self.screen = pygame.display.get_surface()

        self.w,self.h = self.screen.get_width(),self.screen.get_height()

        self.volume = 0.5

        self.joueur1_pseudo = "Yukali"
        self.joueur1_touche = {"left": pygame.K_q, "right": pygame.K_d, "up": pygame.K_z,"down":pygame.K_s, "aim_l":pygame.K_f, "aim_r":pygame.K_g,"atk":pygame.K_SPACE,"switch":pygame.K_e}
        self.joueur2_pseudo = "Toxies"
        self.joueur2_touche = {"left": pygame.K_LEFT, "right": pygame.K_RIGHT, "up": pygame.K_UP,"down":pygame.K_DOWN,"aim_l":pygame.K_KP1, "aim_r":pygame.K_KP2,"atk":pygame.K_KP0,"switch":pygame.K_KP4}
        self.vie = 3




