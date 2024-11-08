import pygame
import Start_game
yellow = (255, 255, 0)


class Pacman:
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/Pacman/pacman_28x28_facing_right.png')
        self.rect = self.image.get_rect()
        # self.rect.centerx = Run.width / 2
        # self.rect.bottom = Run.height - 330
        self.rect.x = 296
        self.rect.y = 571
        self.speedx = 0
        self.speedy = 0
        self.speed = 3
        self.score = 0
        self.lives = 4

    def update(self, walls, gate_list):
        # self.speedx = 0
        keystate = pygame.key.get_pressed()

        # Checking keys on x
        if keystate[pygame.K_a]:
            self.speedx = -self.speed
            self.speedy = 0
            self.image = pygame.image.load('img/Pacman/pacman_28x28_facing_left.png')
        if keystate[pygame.K_d]:
            self.speedx = self.speed
            self.speedy = 0
            self.image = pygame.image.load('img/Pacman/pacman_28x28_facing_right.png')

        # Checking keys on y
        if keystate[pygame.K_w]:
            self.speedy = -self.speed
            self.speedx = 0
            self.image = pygame.image.load('img/Pacman/pacman_28x28_facing_top.png')
        if keystate[pygame.K_s]:
            self.speedy = self.speed
            self.speedx = 0
            self.image = pygame.image.load('img/Pacman/pacman_28x28_facing_bottom.png')

        # Moving on y
        self.rect.y += self.speedy
        if self.rect.collidelist(walls) + 1 or self.rect.collidelist(gate_list) + 1:
            self.rect.y -= self.speedy

        # Moving on x
        self.rect.x += self.speedx
        if self.rect.collidelist(walls) + 1 or self.rect.collidelist(gate_list) + 1:
            self.rect.x -= self.speedx

        # Teleport
        if self.rect.right < 0:
            self.rect.left = Start_game.width
        if self.rect.left > Start_game.width:
            self.rect.right = 0

    def draw(self, screen):
        screen.blit(self.image, self.rect)
