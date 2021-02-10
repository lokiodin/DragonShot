import pygame
from pygame.sprite import Sprite
from constant import *

class Background(pygame.sprite.Sprite):
    def __init__(self, filename):
        super().__init__()
        self.bgimage = pygame.image.load(filename)
        self.bgimage = pygame.transform.scale(self.bgimage, (WIDTH, HEIGHT))
        image = pygame.Surface([WIDTH, HEIGHT]).convert()
 
        # Copy the sprite from the large sheet onto the smaller image
        self.image = image.blit(self.bgimage, (0, 0), (0, 0, WIDTH, HEIGHT))
        self.bgY = 0
        self.bgX = 0

    def render(self):
        displaysurface.blit(self.bgimage, (self.bgX, self.bgY))