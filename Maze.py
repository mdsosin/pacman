import pygame

white = (255, 255, 255)
blue = (0, 0, 255)

# This is a list of walls. Each is in the form [x, y, width, height]
walls = [[10, 80, 10, 216],
         [10, 285, 118, 10],
         [492, 285, 118, 10],
         [492, 285, 10, 83],
         [492, 360, 118, 10],
         [10, 487, 10, 257],
         [118, 285, 10, 85],
         [10, 360, 117, 10],
         [10, 80, 600, 10],
         [10, 735, 600, 10],
         [600, 80, 10, 216],
         [600, 487, 10, 257],
         [300, 80, 20, 96],
         [64, 135, 64, 42],
         [172, 135, 84, 42],
         [364, 135, 84, 42],
         [491, 135, 66, 42],
         [64, 221, 64, 20],
         [236, 221, 147, 20],
         [300, 221, 20, 86],
         [492, 221, 66, 20],
         [170, 221, 20, 150],
         [170, 285, 86, 20],
         [428, 221, 20, 150],
         [362, 285, 86, 20],
         [170, 414, 20, 84],
         [236, 478, 147, 20],
         [300, 478, 20, 85],
         [171, 542, 84, 20],
         [365, 542, 84, 20],
         [428, 414, 20, 84],
         [235, 350, 52, 10],
         [333, 350, 52, 10],
         [235, 350, 10, 86],
         [235, 426, 150, 10],
         [375, 350, 10, 86],
         [10, 414, 116, 10],
         [492, 414, 118, 10],
         [116, 414, 10, 83],
         [492, 414, 10, 83],
         [10, 487, 116, 10],
         [106, 544, 20, 83],
         [65, 544, 46, 20],
         [492, 544, 20, 83],
         [492, 544, 66, 20],
         [10, 607, 54, 20],
         [556, 607, 54, 20],
         [492, 487, 118, 10],
         [171, 607, 20, 85],
         [428, 607, 20, 85],
         [236, 607, 147, 20],
         [300, 607, 20, 85],
         [364, 671, 192, 20],
         [65, 671, 192, 20]
         ]


gate_list = [[288, 351, 45, 2]]

gate_rect = pygame.Rect(287, 300, 46, 10)


class Wall(pygame.sprite.Sprite):
    # Constructor function
    def __init__(self, x, y, width, height, color):
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)

        # Make a blue wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.top = y
        self.rect.left = x


# This creates all the walls in room 1
def setupRoomOne(all_sprites_list):
    # Make the walls. (x_pos, y_pos, width, height)
    wall_list = pygame.sprite.RenderPlain()

    # Loop through the list. Create the wall, add it to the list
    for item in walls:
        wall = Wall(item[0], item[1], item[2], item[3], blue)
        wall_list.add(wall)
        all_sprites_list.add(wall)

    # return our new list
    return wall_list


def draw_gate(screen):
    pygame.draw.rect(screen, white, gate_rect)


def setupGate(all_sprites_list):
    gate = pygame.sprite.RenderPlain()
    gate.add(Wall(288, 351, 45, 2, white))
    all_sprites_list.add(gate)
    return gate


def checkWall():
    pass


def isWrite(x, y, direction):
    pass


# This class represents the ball
# It derives from the "Sprite" class in Pygame
class Block(pygame.sprite.Sprite):

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([width, height])
        self.image.fill(white)
        self.image.set_colorkey(white)
        pygame.draw.ellipse(self.image, color, [0, 0, width, height])

        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()
