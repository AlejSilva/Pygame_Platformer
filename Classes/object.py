import pygame
from os.path import join

from components.get_block import get_block, get_wood_block, get_scale_block, get_grass_block, get_orange_grass_block, get_pink_grass_block
from components.load_sprites import load_sprite_sheets

# Class to represent objects in the game
class Object(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, name=None):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.width = width
        self.height = height
        self.name = name

    def draw(self, win, offset_x):
        win.blit(self.image, (self.rect.x - offset_x, self.rect.y))


# Class to represent stone blocks in the game
class Block(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)
        block = get_block(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)


# Class to represent wood blocks in the game
class WoodBlock(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)
        block = get_wood_block(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)

# Class to represent scale/moss blocks in the game
class ScaleBlock(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)
        block = get_scale_block(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)
    
# Class to represent GREEN grass blocks in the game
class GrassBlock(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)
        block = get_grass_block(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)

# Class to represent ORANGE grass blocks in the game
class OrangeBlock(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)
        block = get_orange_grass_block(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)

# Class to represent PINK grass blocks in the game
class PinkBlock(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)
        block = get_pink_grass_block(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)





