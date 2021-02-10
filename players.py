import pygame
from constant import *
from spridesheet import *
from pygame.locals import *


class HealthBar(pygame.sprite.Sprite):

    def __init__(self, hp) -> None:
        super().__init__()

        image = pygame.image.load("ressources/images/Heart.png")
        self.image = pygame.transform.scale(image, (int(TAILLE_CELL*0.7), int(TAILLE_CELL*0.7)))

        self.hp = hp
        self.heath_animation = [self.image] * hp

    def lost_hp(self, value: int = 1):
        self.hp -= value
        self.heath_animation = [self.image] * self.hp

    def render(self):
        for i in range(self.hp):
            displaysurface.blit(self.image, (i*int(TAILLE_CELL*0.7), 10))



class Dragon(pygame.sprite.Sprite):
    def __init__(self, start: tuple):
        super().__init__()
 
        self.last_tick = pygame.time.get_ticks()

        # Position and direction
        self.vitesse = 10

        self.points = 0
        
        self.health = HealthBar(hp = 5)

        self.pos = vec(start)
        self.direction = "RIGHT"    # Direction possible : RIGHT, LEFT, UP, DOWN

        self.move_frame = 0

        self.walking_frames_RIGHT = []
        self.walking_frames_LEFT = []
        self.walking_frames_UP = []
        self.walking_frames_DOWN = []

        sprite_sheet = SpriteSheet("ressources/images/Dragon/flying_dragon-red-RGB.png")

        # Load all the right facing images into a list -- UP
        image = sprite_sheet.get_image(0, 29, 190-0, 149-29)
        image = pygame.transform.scale(image, (TAILLE_DRAGON, TAILLE_DRAGON))
        self.walking_frames_UP.append(image)
        image = sprite_sheet.get_image(194, 22, 377-194, 148-22)
        image = pygame.transform.scale(image, (TAILLE_DRAGON, TAILLE_DRAGON))
        self.walking_frames_UP.append(image)
        image = sprite_sheet.get_image(392, 19, 558-392, 147-19)
        image = pygame.transform.scale(image, (TAILLE_DRAGON, TAILLE_DRAGON))
        self.walking_frames_UP.append(image)

        # Load all the right facing images into a list -- DOWN
        image = sprite_sheet.get_image(6, 349, 188-6, 455-349)
        image = pygame.transform.scale(image, (TAILLE_DRAGON, TAILLE_DRAGON))
        self.walking_frames_DOWN.append(image)
        image = sprite_sheet.get_image(203, 355, 375-203, 446-355)
        image = pygame.transform.scale(image, (TAILLE_DRAGON, TAILLE_DRAGON))
        self.walking_frames_DOWN.append(image)
        image = sprite_sheet.get_image(415, 358, 544-415, 460-358)
        image = pygame.transform.scale(image, (TAILLE_DRAGON, TAILLE_DRAGON))
        self.walking_frames_DOWN.append(image)

        # Load all the right facing images into a list -- RIGHT
        image = sprite_sheet.get_image(11, 166, 160-11, 282-166)
        image = pygame.transform.scale(image, (TAILLE_DRAGON, TAILLE_DRAGON))
        self.walking_frames_RIGHT.append(image)
        image = sprite_sheet.get_image(200, 203, 351-200, 282-203)
        image = pygame.transform.scale(image, (TAILLE_DRAGON, TAILLE_DRAGON))
        self.walking_frames_RIGHT.append(image)
        image = sprite_sheet.get_image(394, 210, 541-394, 284-210)
        image = pygame.transform.scale(image, (TAILLE_DRAGON, TAILLE_DRAGON))
        self.walking_frames_RIGHT.append(image)

        # Load all the right facing images into a list -- LEFT
        image = sprite_sheet.get_image(32, 532, 179-32, 607-532)
        image = pygame.transform.scale(image, (TAILLE_DRAGON, TAILLE_DRAGON))
        self.walking_frames_LEFT.append(image)
        image = sprite_sheet.get_image(221, 525, 371-221, 604-525)
        image = pygame.transform.scale(image, (TAILLE_DRAGON, TAILLE_DRAGON))
        self.walking_frames_LEFT.append(image)
        image = sprite_sheet.get_image(413, 488, 562-413, 604-488)
        image = pygame.transform.scale(image, (TAILLE_DRAGON, TAILLE_DRAGON))
        self.walking_frames_LEFT.append(image)

        self.image = self.walking_frames_RIGHT[0]
        self.rect = self.image.get_rect()

        # self.rect.topright = start  # Update rect with new pos
        self.rect.center = start


    def move(self, walls):

        pressed_keys = pygame.key.get_pressed()
        # Accelerates the player in the direction of the key press
        if pressed_keys[K_LEFT]:
            self.rect.left -= self.vitesse
            hitted_wall = pygame.sprite.spritecollideany(self, walls)
            if hitted_wall != None:
                self.rect.left = hitted_wall.rect.right
            self.direction = "LEFT"
        if pressed_keys[K_RIGHT]:
            self.rect.right += self.vitesse
            hitted_wall = pygame.sprite.spritecollideany(self, walls)
            if hitted_wall != None:
                self.rect.right = hitted_wall.rect.left
            self.direction = "RIGHT"
        if pressed_keys[K_UP]:
            self.rect.top -= self.vitesse
            hitted_wall = pygame.sprite.spritecollideany(self, walls)
            if hitted_wall != None:
                self.rect.top = hitted_wall.rect.bottom
            self.direction = "UP"
        if pressed_keys[K_DOWN]:
            self.rect.bottom += self.vitesse
            hitted_wall = pygame.sprite.spritecollideany(self, walls)
            if hitted_wall != None:
                self.rect.bottom = hitted_wall.rect.top
            self.direction = "DOWN"        

        # This causes character warping from one point of the screen to the other
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left< 0:
            self.rect.left = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top< 0:
            self.rect.top = 0

    def teleport(self, coord: tuple) -> None:
        # To move to tuple(x,y)
        self.rect.center = coord

    def update(self):
        # Return to base frame if at end of movement sequence 
        if self.move_frame > 2:
            self.move_frame = 0
            return
        
        tmp = pygame.time.get_ticks()
        if self.direction == "RIGHT":
            self.image = self.walking_frames_RIGHT[self.move_frame]
        elif self.direction == "LEFT":
            self.image = self.walking_frames_LEFT[self.move_frame]
        elif self.direction == "UP":
            self.image = self.walking_frames_UP[self.move_frame]
        elif self.direction == "DOWN":
            self.image = self.walking_frames_DOWN[self.move_frame]
        
        # Pour pas que l'animation soit trop rapide
        if tmp - self.last_tick > 200:
            self.move_frame += 1
            self.last_tick = tmp
        
class PokeBall(pygame.sprite.Sprite):

    def __init__(self) -> None:
        super().__init__()
        
        image = pygame.image.load("ressources/images/Dresseur/ballepokemon2.png").convert_alpha()
        self.image = pygame.transform.scale(image, (50, 50))
        self.rect = self.image.get_rect()

        self.vitesse = 10
        self.visible = False
        self.throwed = False
        self.direction_throwd = ''

    def move(self, coord: tuple, direction: str):
        
        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[K_SPACE] and self.throwed == False:
            self.rect.center = coord
            self.direction_throwd = direction
            self.visible = True
            self.throwed = True

    def bouge(self, dragon: Dragon):
        if self.direction_throwd == 'UP':
            if pygame.sprite.collide_rect(self, dragon):
                self.visible = False
                self.throwed= False
                dragon.health.lost_hp()
            elif self.rect.top < 0:
                self.visible = False
                self.throwed= False
            else:
                self.rect.move_ip(0, -self.vitesse)
        elif self.direction_throwd == 'DOWN':
            if pygame.sprite.collide_rect(self, dragon):
                self.visible = False
                self.throwed= False
                dragon.health.lost_hp()
            elif self.rect.bottom > HEIGHT:
                self.visible = False
                self.throwed= False
            else:
                self.rect.move_ip(0, self.vitesse)
        elif self.direction_throwd == 'RIGHT':
            if pygame.sprite.collide_rect(self, dragon):
                self.throwed= False
                self.visible = False
                dragon.health.lost_hp()
            elif self.rect.right > WIDTH:
                self.visible = False
                self.throwed= False
            else:
                self.rect.move_ip(self.vitesse, 0)
        elif self.direction_throwd == 'LEFT':
            if pygame.sprite.collide_rect(self, dragon):
                self.visible = False
                self.throwed= False
                dragon.health.lost_hp()
            elif self.rect.left < 0:
                self.visible = False
                self.throwed= False
            else:
                self.rect.move_ip(-self.vitesse, 0)
        return

    def render(self):
        if self.visible:
            displaysurface.blit(self.image, self.rect)
            pygame.display.update()


class Dresseur(pygame.sprite.Sprite):
    def __init__(self, start: tuple):
        super().__init__()
 
        self.last_tick = pygame.time.get_ticks()

        # Position and direction
        self.vitesse = 10

        self.pos = vec(start)
        self.direction = "UP"    # Direction possible : RIGHT, LEFT, UP, DOWN

        self.move_frame = 0
        self.walking_frames_RIGHT = []
        self.walking_frames_LEFT = []
        self.walking_frames_UP = []
        self.walking_frames_DOWN = []

        sprite_sheet = SpriteSheet("ressources/images/Dresseur/Dresseur.png")

        # Load all the right facing images into a list -- UP
        image = sprite_sheet.get_image(121, 7, 17, 28)
        image = pygame.transform.scale(image, (TAILLE_DRESSEUR, TAILLE_DRESSEUR))
        self.walking_frames_UP.append(image)
        image = sprite_sheet.get_image(153, 6, 17, 28)
        image = pygame.transform.scale(image, (TAILLE_DRESSEUR, TAILLE_DRESSEUR))
        self.walking_frames_UP.append(image)
        image = sprite_sheet.get_image(185, 6, 17, 28)
        image = pygame.transform.scale(image, (TAILLE_DRESSEUR, TAILLE_DRESSEUR))
        self.walking_frames_UP.append(image)

        # Load all the right facing images into a list -- DOWN
        image = sprite_sheet.get_image(121, 39, 17, 28)
        image = pygame.transform.scale(image, (TAILLE_DRESSEUR, TAILLE_DRESSEUR))
        self.walking_frames_DOWN.append(image)
        image = sprite_sheet.get_image(153, 38, 17, 28)
        image = pygame.transform.scale(image, (TAILLE_DRESSEUR, TAILLE_DRESSEUR))
        self.walking_frames_DOWN.append(image)
        image = sprite_sheet.get_image(185, 38, 17, 28)
        image = pygame.transform.scale(image, (TAILLE_DRESSEUR, TAILLE_DRESSEUR))
        self.walking_frames_DOWN.append(image)

        # Load all the right facing images into a list -- RIGHT
        image = sprite_sheet.get_image(121, 103, 14, 28)
        image = pygame.transform.scale(image, (TAILLE_DRESSEUR, TAILLE_DRESSEUR))
        self.walking_frames_RIGHT.append(image)
        image = sprite_sheet.get_image(154, 102, 14, 28)
        image = pygame.transform.scale(image, (TAILLE_DRESSEUR, TAILLE_DRESSEUR))
        self.walking_frames_RIGHT.append(image)
        image = sprite_sheet.get_image(186, 102, 14, 28)
        image = pygame.transform.scale(image, (TAILLE_DRESSEUR, TAILLE_DRESSEUR))
        self.walking_frames_RIGHT.append(image)

        # Load all the right facing images into a list -- LEFT
        image = sprite_sheet.get_image(124, 71, 14, 28)
        image = pygame.transform.scale(image, (TAILLE_DRESSEUR, TAILLE_DRESSEUR))
        self.walking_frames_LEFT.append(image)
        image = sprite_sheet.get_image(155, 70, 14, 28)
        image = pygame.transform.scale(image, (TAILLE_DRESSEUR, TAILLE_DRESSEUR))
        self.walking_frames_LEFT.append(image)
        image = sprite_sheet.get_image(187, 70, 14, 28)
        image = pygame.transform.scale(image, (TAILLE_DRESSEUR, TAILLE_DRESSEUR))
        self.walking_frames_LEFT.append(image)

        self.image = self.walking_frames_UP[0]
        self.rect = self.image.get_rect()

        # self.rect.topright = start  # Update rect with new pos
        self.rect.center = start


    def move(self, walls, roads):

        pressed_keys = pygame.key.get_pressed()
        # Accelerates the player in the direction of the key press
        if pressed_keys[K_q]:
            self.rect.left -= self.vitesse
            hitted_wall = pygame.sprite.spritecollideany(self, walls)
            # hitted_road = pygame.sprite.spritecollideany(self, roads)
            # if hitted_road == None:
            #     self.rect.left += self.vitesse
            # else:
            #     self.rect.top = hitted_road.rect.top
            if hitted_wall != None:
                self.rect.left = hitted_wall.rect.right
            self.direction = "LEFT"
        if pressed_keys[K_d]:
            self.rect.right += self.vitesse
            hitted_wall = pygame.sprite.spritecollideany(self, walls)
            # hitted_road = pygame.sprite.spritecollideany(self, roads)
            # if hitted_road == None:
            #     self.rect.right -= self.vitesse
            # else:
            #     self.rect.top = hitted_road.rect.top
            if hitted_wall != None:
                self.rect.right = hitted_wall.rect.left
            self.direction = "RIGHT"
        if pressed_keys[K_z]:
            self.rect.top -= self.vitesse
            hitted_wall = pygame.sprite.spritecollideany(self, walls)
            # hitted_road = pygame.sprite.spritecollideany(self, roads)
            # if hitted_road == None:
            #     self.rect.top += self.vitesse
            # else:
            #     self.rect.top = hitted_road.rect.top
            if hitted_wall != None:
                self.rect.top = hitted_wall.rect.bottom
            self.direction = "UP"
        if pressed_keys[K_s]:
            self.rect.bottom += self.vitesse
            hitted_wall = pygame.sprite.spritecollideany(self, walls)
            # hitted_road = pygame.sprite.spritecollideany(self, roads)
            # if hitted_road == None:
            #     self.rect.bottom -= self.vitesse
            # else:
            #     self.rect.top = hitted_road.rect.top
            if hitted_wall != None:
                self.rect.bottom = hitted_wall.rect.top
            self.direction = "DOWN"        

        # This causes character warping from one point of the screen to the other
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left< 0:
            self.rect.left = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top< 0:
            self.rect.top = 0

    def teleport(self, coord: tuple) -> None:
        # To move to tuple(x,y)
        self.rect.center = coord

    def update(self):
        # Return to base frame if at end of movement sequence 
        if self.move_frame > 2:
            self.move_frame = 0
            return
        
        tmp = pygame.time.get_ticks()
        if self.direction == "RIGHT":
            self.image = self.walking_frames_RIGHT[self.move_frame]
        elif self.direction == "LEFT":
            self.image = self.walking_frames_LEFT[self.move_frame]
        elif self.direction == "UP":
            self.image = self.walking_frames_UP[self.move_frame]
        elif self.direction == "DOWN":
            self.image = self.walking_frames_DOWN[self.move_frame]
        
        # Pour pas que l'animation soit trop rapide
        if tmp - self.last_tick > 200:
            self.move_frame += 1
            self.last_tick = tmp
        