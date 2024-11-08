import pygame
import math
import random
from random import *
import Maze
import Start_game


def move_all():
    Ghost.list[0].move()
    Ghost.list[1].move()
    Ghost.list[2].move()
    Ghost.list[3].move()


def check_collide_all(pacman):
    for ghost in Ghost.list:
        ghost.collide( pacman, Start_game.width, Start_game.height )


def draw_ghosts(screen):
    Ghost.list[0].draw(screen)
    Ghost.list[1].draw(screen)
    Ghost.list[2].draw(screen)
    Ghost.list[3].draw(screen)


def create_ghosts():
    blinky = RedGhost(250, 400, [16, 2])
    pinky = PinkGhost(280, 400, [2, 2])
    inky = BlueGhost(320, 400, [16, 18])
    clyde = OrangeGhost(350, 400, [2, 18])

    Ghost.list.append(blinky)
    Ghost.list.append(pinky)
    Ghost.list.append(inky)
    Ghost.list.append(clyde)


def blue_mode():
    for ghost in Ghost.list:
        if ghost.mode != "dead":
            ghost.blue = True
            ghost.blue_timer = 0


def end_blue_mode():
    for ghost in Ghost.list:
        ghost.blue = False

def activation(bigseeds, seeds, full_seeds):
    Ghost.list[2].activate(full_seeds, bigseeds, seeds)
    Ghost.list[3].activate(full_seeds, bigseeds, seeds)


class Ghost:
    list = []

    def __init__(self):
        # OBJECTS
        self.state = ['normal', 'vulnerable', 'dead']

        # location
        self.speed = 5
        self.direction_x = self.speed
        self.direction_y = 0
        self.speedxSec = 1

        # move
        self.DIR = {"RIGHT": 0, "DOWN": 1, "LEFT": 2, "UP": 3}
        self.COORD_DIR = {0: [1, 0], 1: [0, 1], 2: [-1, 0], 3: [0, -1]}
        self.look_dir = 3
        self.move_dir = 3

        # vars
        self.mode = "house"
        self.blue = False
        self.respawn_time = 3
        self.multi_kills = 1
        self.out = False

        # const
        self.type = type
        self.scatter_time = 5
        self.chase_time = 20

        # timer
        self.blue_timer = 0
        self.respawn_time = 0
        self.turn_timer = 0

        # image
        # blue mode
        self.blue_mode_up_img = pygame.image.load('img/Ghosts/Ghost_In_Panic/up_28x28.png')
        self.blue_mode_down_img = pygame.image.load('img/Ghosts/Ghost_In_Panic/down_28x28.png')
        self.blue_mode_left_img = pygame.image.load('img/Ghosts/Ghost_In_Panic/left_28x28.png')
        self.blue_mode_right_img = pygame.image.load('img/Ghosts/Ghost_In_Panic/right_28x28.png')
        self.blue_mode_img = pygame.image.load('img/Ghosts/Ghost_In_Panic/scared_1_28x28.png')

    def rmove(self, rect):
        rect.x += self.direction_x
        rect.y += self.direction_y
        cur_rect = rect

        right = False
        left = False
        up = False
        down = False

        rrect = self.blue_mode_img.get_rect(x = rect.x + 10, y = rect.y - self.direction_y)
        lrect = self.blue_mode_img.get_rect(x = rect.x - 10, y = rect.y - self.direction_y)
        urect = self.blue_mode_img.get_rect(x = rect.x - self.direction_x, y = rect.y - 10)
        drect = self.blue_mode_img.get_rect(x = rect.x - self.direction_x, y = rect.y + 10)

        if not rrect.collidelist(Maze.walls) + 1: right = True
        if not lrect.collidelist(Maze.walls) + 1: left = True
        if not urect.collidelist(Maze.walls) + 1: up = True
        if not drect.collidelist(Maze.walls) + 1: down = True

        if self.direction_x > 0:
            cur_rect = rrect
            left = False
        if self.direction_x < 0:
            cur_rect = lrect
            right = False
        if self.direction_y > 0:
            cur_rect = drect
            up = False
        if self.direction_y < 0:
            cur_rect = urect
            down = False

        ability = [right, left, up, down]
        # print(ability)

        if rect.x == 300 and self.out == False:
            self.direction_x = 0
            self.direction_y = -self.speed
            self.out = True

        if cur_rect.collidelist(Maze.walls) + 1:
            afford = []

            for i in range(len(ability)):
                if ability[i] == True:
                    afford.append(i)

            next_direction = afford[randint(0, (len(afford)-1) )]

            if next_direction == 0:
                self.direction_x = self.speed
                self.direction_y = 0
            if next_direction == 1:
                self.direction_x = -self.speed
                self.direction_y = 0
            if next_direction == 2:
                self.direction_x = 0
                self.direction_y = -self.speed
            if next_direction == 3:
                self.direction_x = 0
                self.direction_y = self.speed


    def oper_blue(self, pacman, width, height):
        if self.blue:
            self.mode = "normal"
            self.blue = False
            self.blue_timer = 0
            self.respawn_timer = 0
            pacman.score += 200 * self.multi_kills
            self.multi_kills += 1
        elif not self.blue:
            self.multi_kills = 1
            if pacman.lives > 0:
                # self.main.game_state = "respawn"
                pacman.lives -= 1
                # self.main.temp_counter = 0
                pacman.rect.centerx = width / 2
                pacman.rect.bottom = height - 330
        # house coord (297, 370), tp coord (297, 315)


class RedGhost(Ghost):
    def __init__(self, x, y, return_coords):
        super().__init__()

        self.type = "shadow"
        self.x = x  # координаты от поля
        self.y = y
        self.coords = [x, y]
        self.return_coords = return_coords
        self.out = True
        self.blinky_up_img = pygame.image.load('img/Ghosts/Red/red_up_1_28x28.png')
        self.blinky_down_img = pygame.image.load('img/Ghosts/Red/red_down_1_28x28.png')
        self.blinky_left_img = pygame.image.load('img/Ghosts/Red/red_left_1_28x28.png')
        self.blinky_right_img = pygame.image.load('img/Ghosts/Red/red_right_1_28x28.png')

        self.blinky_rect = self.blinky_up_img.get_rect(x=297, y=315)

    def move(self):
        # print('blinky')
        self.rmove(self.blinky_rect)

    def draw(self, screen):
        if self.blue:
            screen.blit(self.blue_mode_img, self.blinky_rect)
        else:
            if self.direction_y < 0:
                screen.blit(self.blinky_up_img, self.blinky_rect)
            elif self.direction_y > 0:
                screen.blit(self.blinky_down_img, self.blinky_rect)
            elif self.direction_x < 0:
                screen.blit(self.blinky_left_img, self.blinky_rect)
            elif self.direction_x > 0:
                screen.blit(self.blinky_right_img, self.blinky_rect)

    def collide(self, pacman, width, height):
        if self.blinky_rect.colliderect(pacman.rect) and self.mode != "dead":
            Ghost.oper_blue(Ghost.list[0], pacman, width, height)
            self.blinky_rect.x = 297
            self.blinky_rect.y = 370


class OrangeGhost(Ghost):
    def __init__(self, x, y, return_coords):
        super().__init__()

        self.type = "pokey"
        self.x = x  # координаты от поля
        self.y = y
        self.coords = [x, y]
        self.return_coords = return_coords
        self.clyde_up_img = pygame.image.load('img/Ghosts/Orange/orange_up_1_28x28.png')
        self.clyde_down_img = pygame.image.load('img/Ghosts/Orange/orange_down_1_28x28.png')
        self.clyde_left_img = pygame.image.load('img/Ghosts/Orange/orange_left_1_28x28.png')
        self.clyde_right_img = pygame.image.load('img/Ghosts/Orange/orange_right_1_28x28.png')

        self.clyde_rect = self.clyde_up_img.get_rect(x=280, y=370)

    def activate(self):
        self.clyde_rect.x = 455
        self.clyde_rect.y = 186

    def move(self):
        rect = self.clyde_rect
        # print('orange')
        self.rmove(rect)

    def draw(self, screen):
        if self.blue:
            screen.blit(self.blue_mode_img, self.clyde_rect)
        else:
            if self.direction_y < 0:
                screen.blit(self.clyde_up_img, self.clyde_rect)
            elif self.direction_y > 0:
                screen.blit(self.clyde_down_img, self.clyde_rect)
            elif self.direction_x < 0:
                screen.blit(self.clyde_left_img, self.clyde_rect)
            elif self.direction_x > 0:
                screen.blit(self.clyde_right_img, self.clyde_rect)

    def collide(self, pacman, width, height):
        if self.clyde_rect.colliderect(pacman.rect) and self.mode != "dead":
            Ghost.oper_blue(Ghost.list[3], pacman, width, height)
            self.clyde_rect.x = 297
            self.clyde_rect.y = 370



class BlueGhost(Ghost):
    def __init__(self, x, y, return_coords):
        super().__init__()

        self.type = "bashful"
        self.x = x  # координаты от поля
        self.y = y
        self.coords = [x, y]
        self.return_coords = return_coords
        self.inky_up_img = pygame.image.load('img/Ghosts/Blue/blue_up_1_28x28.png')
        self.inky_down_img = pygame.image.load('img/Ghosts/Blue/blue_down_1_28x28.png')
        self.inky_left_img = pygame.image.load('img/Ghosts/Blue/blue_left_1_28x28.png')
        self.inky_right_img = pygame.image.load('img/Ghosts/Blue/blue_right_1_28x28.png')

        self.inky_rect = self.inky_up_img.get_rect(x=340, y=390)
    def activate(self):
        self.inky_rect.x = 137
        self.inky_rect.y = 186

    def move(self):
        rect = self.inky_rect
        # print('blue')
        self.rmove(rect)

    def draw(self, screen):
        if self.blue:
            screen.blit(self.blue_mode_img, self.inky_rect)
        else:
            if self.direction_y < 0:
                screen.blit(self.inky_up_img, self.inky_rect)
            elif self.direction_y > 0:
                screen.blit(self.inky_down_img, self.inky_rect)
            elif self.direction_x < 0:
                screen.blit(self.inky_left_img, self.inky_rect)
            elif self.direction_x > 0:
                screen.blit(self.inky_right_img, self.inky_rect)

    def collide(self, pacman, width, height):
        if self.inky_rect.colliderect(pacman.rect) and self.mode != "dead":
            Ghost.oper_blue(Ghost.list[2], pacman, width, height)
            self.inky_rect.x = 297
            self.inky_rect.y = 370


class PinkGhost(Ghost):
    def __init__(self, x, y, return_coords):
        super().__init__()

        self.type = "speedy"
        self.x = x  # координаты от поля
        self.y = y
        self.coords = [x, y]
        self.return_coords = return_coords
        self.pinky_up_img = pygame.image.load('img/Ghosts/Pink/pink_up_1_28x28.png')
        self.pinky_down_img = pygame.image.load('img/Ghosts/Pink/pink_down_1_28x28.png')
        self.pinky_left_img = pygame.image.load('img/Ghosts/Pink/pink_left_1_28x28.png')
        self.pinky_right_img = pygame.image.load('img/Ghosts/Pink/pink_right_1_28x28.png')

        self.pinky_rect = self.pinky_up_img.get_rect(x=320, y=380)

    def move(self):
        rect = self.pinky_rect
        # print('pink')
        self.rmove(rect)

    def draw(self, screen):
        if self.blue:
            screen.blit(self.blue_mode_img, self.pinky_rect)
        else:
            if self.direction_y < 0:
                screen.blit(self.pinky_up_img, self.pinky_rect)
            elif self.direction_y > 0:
                screen.blit(self.pinky_down_img, self.pinky_rect)
            elif self.direction_x < 0:
                screen.blit(self.pinky_left_img, self.pinky_rect)
            elif self.direction_x > 0:
                screen.blit(self.pinky_right_img, self.pinky_rect)

    def collide(self, pacman, width, height):
        if self.pinky_rect.colliderect(pacman.rect) and self.mode != "dead":
            Ghost.oper_blue(Ghost.list[1], pacman, width, height)
            self.pinky_rect.x = 297
            self.pinky_rect.y = 370
