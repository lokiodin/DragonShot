import pygame
from pygame.constants import RESIZABLE

pygame.init()  # Begin pygame
 
# Declaring variables to be used through the program
TITLE = "Dragonshot"
vec = pygame.math.Vector2
ACC = 0.3
FRIC = -0.10
FPS = 60
FPS_CLOCK = pygame.time.Clock()

WIDTH = 860
TAILLE_CELL = int(WIDTH/20)
HEIGHT = WIDTH+TAILLE_CELL

TAILLE_DRAGON = TAILLE_CELL - 10
TAILLE_DRESSEUR = TAILLE_CELL - 10

BLACK = (0, 0, 0) 
GREEN = (150, 255, 150)
RED = (255, 0, 0)
BLUE = (106, 159, 181)
WHITE = (255, 255, 255)

displaysurface = pygame.display.set_mode((WIDTH, HEIGHT), RESIZABLE)
pygame.display.set_caption(TITLE)
