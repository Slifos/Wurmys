import pygame
"""Générateur de platform sur la map"""
class platform:
    def __init__(self,ratio,position):
        self.screen = pygame.display.get_surface()
        self.platform = pygame.image.load("ui/platform.png")
        self.ratio_platform = ratio,ratio*0.224
        self.image = pygame.transform.scale(self.platform, self.ratio_platform)
        self.platform_rect = self.platform.get_rect()
        self.platform_rect.x,self.platform_rect.y = position[0],position[1]
    def affichage_platform(self):
        self.screen.blit(self.platform, self.p)
