import pygame
from pygame.locals import *
from pygame.sprite import RenderUpdates
import pygame.freetype

import json
import sys

from enum import Enum

from constant import *
from background import Background
from spridesheet import SpriteSheet
from players import *
from level import *
from button import UIElement
from leaderboard import Rank
from levels import *


class GameState(Enum):
    QUIT = -1
    TITLE = 0
    GAME = 1
    SETTINGS = 2
    DEATH = 3
    LEADERBOARD = 4


class Game():

    
    def __init__(self) -> None:
        self.levels = []
        self.levels.append(Level(n1))
        self.levels.append(Level(n2))
        self.levels.append(Level(n3))
        self.levels.append(Level(n4))

        self.current_level_no = 0
        self.current_level = self.levels[self.current_level_no]
        self.current_level.build()

        self.background = Background("ressources/images/Game_background.png")
        self.dragon = Dragon(self.current_level.starting_point)
        self.dresseur = Dresseur(self.current_level.starting_dresseur)
        self.pokeball = PokeBall()

        self.movingsprites = pygame.sprite.Group()
        self.movingsprites.add(self.dragon)
        self.movingsprites.add(self.dresseur)
        
    def buttons_title(self):

        start_btn = UIElement(
            center_position=(WIDTH/2, HEIGHT/2),
            font_size=30,
            bg_rgb=None,
            text_rgb=WHITE,
            text="Start",
            action=GameState.GAME,
        )
        quit_btn = UIElement(
            center_position=(WIDTH/2, HEIGHT/2+200),
            font_size=30,
            bg_rgb=None,
            text_rgb=WHITE,
            text="Quit",
            action=GameState.QUIT,
        )
        leaderboard_btn = UIElement(
            center_position=(WIDTH/2, HEIGHT/2+100),
            font_size=30,
            bg_rgb=None,
            text_rgb=WHITE,
            text="Leaderboard",
            action=GameState.LEADERBOARD,
        )
        buttons = RenderUpdates(start_btn, quit_btn, leaderboard_btn)
        
        return buttons

    def menutitle(self, buttons):
        bgtitle = Background("ressources/images/Title_background.png")

        while True:


            mouse_up = False
            for event in pygame.event.get():
                # Will run when the close window button is clicked    
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit() 

                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    mouse_up = True               # For events that occur upon clicking the mouse (left click) 

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pass

                # Event handling for a range of different key presses    
                if event.type == pygame.KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit() 

            # --- Animation des boutons Check des action des boutons
            for button in buttons:
                ui_action = button.update(pygame.mouse.get_pos(), mouse_up)
                if ui_action is not None:
                    if ui_action == GameState.GAME:
                        self.__init__()
                    return ui_action



            # --- Render 
            bgtitle.render()
            buttons.draw(displaysurface)
            FPS_CLOCK.tick(FPS)
            # print(FPS_CLOCK, end='\r')
            pygame.display.update()

    def buttons_run(self):
        quit_btn = UIElement(
            center_position=(WIDTH-100, 0+30),
            font_size=30,
            bg_rgb=None,
            text_rgb=WHITE,
            text="Quit",
            action=GameState.QUIT,
        )
        buttons = RenderUpdates(quit_btn)

        return buttons

    def run(self, buttons):
        pygame.time.wait(100)
        while True:
            mouse_up = False
            # --- Check des events
            for event in pygame.event.get():
                # Will run when the close window button is clicked    
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit() 

                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    mouse_up = True
                # For events that occur upon clicking the mouse (left click) 
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pass
                # Event handling for a range of different key presses    
                if event.type == pygame.KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    if event.key == K_r: # For restart the game, ugly way
                        self.__init__()
                    if event.key == K_w: #################################################################### A enlever cette condition car ne sert à rien
                        return GameState.DEATH
                    if event.key == K_a: #################################################################### A enlever cette condition car ne sert à rien
                        self.dragon.health.lost_hp()
                    if event.key == K_0:
                        self.current_level_no = 0
                        self.current_level = self.levels[self.current_level_no]
                        self.current_level.build()
                        self.dragon.teleport(self.current_level.starting_point)
                        self.dresseur.teleport(self.current_level.starting_dresseur)
                    if event.key == K_1:
                        self.current_level_no = 1
                        self.current_level = self.levels[self.current_level_no]
                        self.current_level.build()
                        self.dragon.teleport(self.current_level.starting_point)
                        self.dresseur.teleport(self.current_level.starting_dresseur)
                    if event.key == K_2:
                        self.current_level_no = 2
                        self.current_level = self.levels[self.current_level_no]
                        self.current_level.build()
                        self.dragon.teleport(self.current_level.starting_point)
                        self.dresseur.teleport(self.current_level.starting_dresseur)
                    if event.key == K_3:
                        self.current_level_no = 3
                        self.current_level = self.levels[self.current_level_no]
                        self.current_level.build()
                        self.dragon.teleport(self.current_level.starting_point)
                        self.dresseur.teleport(self.current_level.starting_dresseur)
            # --- Animation des boutons Check des action des boutons
            for button in buttons:
                ui_action = button.update(pygame.mouse.get_pos(), mouse_up)
                if ui_action is not None:
                    return ui_action






            # --- Check de la vie restante
            if self.dragon.health.hp <= 0:
                return GameState.DEATH

            # --- Mouvance des dragon, dresseur et pokeball
            self.dragon.move(self.current_level.wall_list)
            self.dresseur.move(self.current_level.wall_list, self.current_level.road_list)
            self.pokeball.move(self.dresseur.rect.center, self.dresseur.direction) # Pas besoin ensuite de pokeball.update car pas d'animation
            if self.pokeball.throwed:
                self.pokeball.bouge(self.dragon)
            # --- Leur update()
            self.dragon.update()
            self.dresseur.update()
            
            if pygame.sprite.spritecollideany(self.dragon, self.current_level.finish_sprite, collided = None): # Pour le finish, si on passe au niveau suivant
                self.current_level_no = (self.current_level_no + 1 ) % len(self.levels)
                self.current_level = self.levels[self.current_level_no]
                self.current_level.build()
                self.dragon.points += 10
                self.dragon.teleport(self.current_level.starting_point)
                self.dresseur.teleport(self.current_level.starting_dresseur)


            # ------- Drawing the game
            self.background.render()

            self.current_level.wall_list.draw(displaysurface)
            self.current_level.start_sprite.draw(displaysurface)
            self.current_level.finish_sprite.draw(displaysurface)
            self.current_level.road_list.draw(displaysurface)

            self.movingsprites.draw(displaysurface)
            self.dragon.health.render()
            self.pokeball.render()
            buttons.draw(displaysurface)

            # Pour avoir un debug de la hitbox
            # for wall in current_level.wall_list:
            #     pygame.draw.rect(displaysurface, GREEN, wall.rect, 1)
            # pygame.draw.rect(displaysurface, RED, dragon.rect, 1)

            pygame.display.update()

            FPS_CLOCK.tick(FPS)
            # print(FPS_CLOCK, end='\r')

    def buttons_deathtitle(self):
        menu_btn = UIElement(
                    center_position=(400, 400),
                    font_size=30,
                    bg_rgb=None,
                    text_rgb=WHITE,
                    text="Return to Menu",
                    action=GameState.TITLE,
        )
        quit_btn = UIElement(
            center_position=(400, 500),
            font_size=30,
            bg_rgb=None,
            text_rgb=WHITE,
            text="Quit",
            action=GameState.QUIT,
        )

        buttons = RenderUpdates(menu_btn, quit_btn)
        
        return buttons

    def deathtitle(self, buttons):
        bdeath = Background("ressources/images/GameOver.png")
        while True:
            mouse_up = False
            for event in pygame.event.get():
                # Will run when the close window button is clicked    
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit() 
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    mouse_up = True
                # For events that occur upon clicking the mouse (left click) 
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pass

                # Event handling for a range of different key presses    
                if event.type == pygame.KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit() 
            # --- Animation des boutons  Check des action des boutons
            for button in buttons:
                ui_action = button.update(pygame.mouse.get_pos(), mouse_up)
                if ui_action is not None:
                    return ui_action


            # --- Render
            bdeath.render()
            buttons.draw(displaysurface)

            pygame.display.update()

    def buttons_leaderboard(self):
        menu_btn = UIElement(
            center_position=(WIDTH*0.2, HEIGHT*0.8),
            font_size=30,
            bg_rgb=None,
            text_rgb=WHITE,
            text="Return to Menu",
            action=GameState.TITLE,
        )
        quit_btn = UIElement(
            center_position=((WIDTH/2), HEIGHT*0.9),
            font_size=30,
            bg_rgb=None,
            text_rgb=WHITE,
            text="Quit",
            action=GameState.QUIT,
        )
        game_btn = UIElement(
            center_position=((WIDTH/3)*2.2, HEIGHT*0.8),
            font_size=30,
            bg_rgb=None,
            text_rgb=WHITE,
            text="Go to Game",
            action=GameState.GAME,
        )


        buttons = RenderUpdates(menu_btn, quit_btn, game_btn)
        
        return buttons

    def leaderboard(self, buttons):
        bleaderboard = Background("ressources/images/Leaderboard_background.png")

        while True:
            mouse_up = False
            for event in pygame.event.get():
                # Will run when the close window button is clicked    
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit() 
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    mouse_up = True
                # For events that occur upon clicking the mouse (left click) 
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pass

                # Event handling for a range of different key presses    
                if event.type == pygame.KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit() 
            # --- Animation des boutons Check des action des boutons
            for button in buttons:
                ui_action = button.update(pygame.mouse.get_pos(), mouse_up)
                if ui_action is not None:
                    return ui_action


            # --- Render
            bleaderboard.render()
            buttons.draw(displaysurface)
            Rank(displaysurface)
            

            pygame.display.update()
    
    def save_game(self):
        with open("scores.json", 'r') as f:
            data_dict = json.load(f)

        tmp_data_dict = {}
        last_key = ""
        change = False
        for key in data_dict:
            # print(key, data_dict[key])
            if change:
                tmp_data_dict[str(int(key)+1)] = data_dict[key]
            if data_dict[key]["points"] < self.dragon.points:
                tmp_data_dict[str(int(key)+1)] = data_dict[key]
                tmp_data_dict[key] = {"name":"dragon", "points":self.dragon.points}
                # print(tmp_data_dict)
                change = True
            
            if not change:
                tmp_data_dict[key] = data_dict[key]
            last_key = key
        
        # print("LA:", tmp_data_dict)
        if not change:
            tmp_data_dict[str(int(last_key)+1)] = {"name":"dragon", "points":self.dragon.points}

            
        # print("FIN\n", tmp_data_dict)
        with open("scores.json", 'w') as f:
            json.dump(tmp_data_dict, f,  indent=4)
        # print("SAVED")


def main():


    game = Game()
    game_state = GameState.TITLE

    while True:
        if game_state == GameState.TITLE:
            game_state = game.menutitle(game.buttons_title())
        if game_state == GameState.GAME:
            game_state = game.run(game.buttons_run())
            if game_state == GameState.QUIT:
                game.save_game()
        if game_state == GameState.DEATH:
            game_state = game.deathtitle(game.buttons_deathtitle())
        if game_state == GameState.LEADERBOARD:
            game_state = game.leaderboard(game.buttons_leaderboard())
        if game_state == GameState.QUIT:
            pygame.quit()
            sys.exit() 



if __name__ == '__main__':
    main()