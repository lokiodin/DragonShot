import pygame
from constant import *
from spridesheet import *
from pygame.locals import *

class CellMaze(pygame.sprite.Sprite):

    def __init__(self, x: int, y: int, type: str) -> None:
        super().__init__()
        sprite_sheet = SpriteSheet("ressources/images/tiles_spritesheet.png")

        # Load all the right image for each type of cell (finish, start or a wall)
        if type == "start":
            image = sprite_sheet.get_image(292, 216, 354-292, 285-216)
            self.image = pygame.transform.scale(image, (TAILLE_CELL, TAILLE_CELL))
        elif type == "finish":
            image = sprite_sheet.get_image(288, 360, 357-288, 429-360)
            self.image = pygame.transform.scale(image, (TAILLE_CELL, TAILLE_CELL))
        elif type == "wall":
            image = sprite_sheet.get_image(504, 288, 573-504, 357-288)
            self.image = pygame.transform.scale(image, (TAILLE_CELL, TAILLE_CELL))
        elif type == "road":
            image = sprite_sheet.get_image(864, 72, 911-864, 141-72)
            self.image = pygame.transform.scale(image, (TAILLE_CELL, TAILLE_CELL))
        else:
            raise ValueError("Wrong type for CellMaze (only start, finish or wall)")

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def __repr__(self) -> str:
        return super().__repr__()

class Level():
    """ Créé un niveau avec la map renseignée. """

    wall_list = None
    start_sprite = None
    finish_sprite = None
    road_list = None

    def __init__(self, levelfile: str) -> None:
        self.levelfile = levelfile
        self.wall_list = pygame.sprite.Group()
        self.start_sprite = pygame.sprite.Group()
        self.finish_sprite = pygame.sprite.Group()
        self.road_list = pygame.sprite.Group()

        
        # with open(levelfile, 'r') as f:
        #     self.levelraw = f.readlines()
        self.levelraw = levelfile.split("\n")

    def build(self) -> None:

        self.wall_list.empty()
        self.start_sprite.empty()
        self.finish_sprite.empty()
        
        for nrow in range(len(self.levelraw)):
            row = self.levelraw[nrow]
            for ncol in range(len(row)):
                if row[ncol] == "w":
                    wall = CellMaze(ncol*TAILLE_CELL, nrow*TAILLE_CELL, "wall")
                    self.wall_list.add(wall)
                elif row[ncol] == "s":
                    start = CellMaze(ncol*TAILLE_CELL, nrow*TAILLE_CELL, "start")
                    self.start_sprite.add(start)
                    self.starting_point = pygame.sprite.Group.sprites(self.start_sprite)[0].rect.center
                elif row[ncol] == "f":
                    finish = CellMaze(ncol*TAILLE_CELL, nrow*TAILLE_CELL, "finish")
                    self.finish_sprite.add(finish)
                    self.finish_point = (ncol*TAILLE_CELL, nrow*TAILLE_CELL)
                elif row[ncol] == "c":
                    road = CellMaze(ncol*TAILLE_CELL, nrow*TAILLE_CELL, "road")
                    self.road_list.add(road)
                    # if ncol == int(len(row)/2):
                    self.starting_dresseur = pygame.sprite.Group.sprites(self.road_list)[0].rect.center


    def __repr__(self) -> str:
        return f'level({self.levelfile})'

