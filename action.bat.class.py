# ICS3U
# Assignment 2: Action
# Jazmin M

import pygame
GREY = (155,149,150)

class Bat(pygame.sprite.Sprite):

    def __init__(self,color,width,height):
        super().__init__()

        self.image = pygame.Surface([width,height])
        self.image.fill(GREY)
        self.image.set_colorkey(GREY)

        pyagme.draw.polygon(self.image, color, [[0,0],[10,10],[0,10]]
        self.polygon = self.image.get_polygon()

        
