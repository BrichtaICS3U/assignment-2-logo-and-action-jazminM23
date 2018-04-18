# ICS3U
# Assignment 2: Action
# Jazmin M

import pygame
GREY = (155,149,150)
WHITE = (255,255,255)
class Bat(pygame.sprite.Sprite):

    def __init__(self,color,width,height):
        super().__init__()

        self.image = pygame.Surface([width,height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        pygame.draw.polygon(self.image, color, [[0,0],[20,0],[10,20]])
        self.rect = self.image.get_rect()

        
