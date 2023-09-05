import pygame
from components.load_sprites import load_sprite_sheets
from os.path import join
from Classes.object import Object

# Class to represent points
class Point(Object):
    ANIMATION_DELAY = 3  # Adjust the delay as needed

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "points")
        self.animation_count = 0
        self.points = load_sprite_sheets("Items", "Fruits", width, height)

        self.image = self.points["Strawberry"][0]

        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_name = "Strawberry"

        

    def loop(self):
        sprites = self.points[self.animation_name]
        sprite_index = (self.animation_count //
                        self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1

        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0






