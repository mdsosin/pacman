import pygame

class Grain:

    def __init__(self, x, y):
        self.pic = pygame.image.load('img/Seeds/Big_seed_8x8.png')
        self.rect = self.pic.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, screen):
        screen.blit(self.pic, self.rect) # Рисует зерно


def generateSeeds(walls):
    seeds = []

    # seeds.append(Grain(574, 105))
    for y in range(29):
        for x in range(26):
            xcoord = 40 + 21.3 * x
            ycoord = 110 + 21.5 * y
            tmp = Grain(xcoord, ycoord)
            if not tmp.rect.collidelist(walls) + 1:
                if not (0 < xcoord < 130 and 270 < ycoord < 500) and \
                        not (480 < xcoord < 580 and 270 < ycoord < 500) and \
                        not (160 < xcoord < 450 and 270 < ycoord < 500) and \
                        not (290 < xcoord < 320 and 580 < ycoord < 590):
                    seeds.append(tmp)

    return seeds


class bigSeed:

    def __init__(self, x, y):
        self.pic = pygame.image.load('img/Seeds/Big_seed_16x16.png')
        self.rect = self.pic.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, screen):
        screen.blit(self.pic, self.rect)  # Рисует большое зерно


def generateBigSeed():
    bigSeeds = []

    bigSeeds.append(bigSeed(36, 150))
    bigSeeds.append(bigSeed(36, 685))
    bigSeeds.append(bigSeed(568, 150))
    bigSeeds.append(bigSeed(568, 685))

    return bigSeeds
