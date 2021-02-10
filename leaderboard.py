# import pygame

import json
from os import name
import pygame.freetype

from button import create_surface_with_text
from button import *
from constant import *

class RowRank():

    def __init__(self, no, name, points) -> None:
        
        self.no = int(no)
        self.name = name
        self.points = int(points)
        self.text = f"{self.no}      {self.name}      {self.points}"
        self.text_surface = create_surface_with_text(text=self.text, font_size=20, text_rgb=RED, bg_rgb=None)
        self.rect = self.text_surface.get_rect()
        self.rect.x = WIDTH/3
        self.rect.y = 250 + 50 * self.no


    def draw(self, surface):
        surface.blit(self.text_surface, self.rect)

class Rank():

    def __init__(self, surface) -> None:
        self.surface = surface

        self.parse_scores()


    def parse_scores(self, file="scores.json"):
        
        with open(file) as json_data:
            data_dict = json.load(json_data)
        
        for row in data_dict:
            RowRank(no=row, name=data_dict[row]["name"], points=data_dict[row]["points"]).draw(self.surface)
            
    def draw(self):
        for rank in self.ranks:
            rank.draw(self.surface)


