import pygame
from Classes.object import Object
from os.path import join
from components.load_sprites import load_sprite_sheets


# Class to represent fire traps in the game
class Fire(Object):
    ANIMATION_DELAY = 3

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "fire")
        self.fire = load_sprite_sheets("Traps", "Fire", width, height)
        self.image = self.fire["off"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.animation_name = "off"

    def on(self):
        self.animation_name = "on"

    def off(self):
        self.animation_name = "off"

    def loop(self):
        sprites = self.fire[self.animation_name]
        sprite_index = (self.animation_count //
                        self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1

        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0


def load_single_spike_image(width, height):
    path = join("assets", "Traps", "Spikes", "Idle.png")
    image = pygame.image.load(path).convert_alpha()
    return pygame.transform.scale(image, (width, height))

# Class to represent spikes traps in the game
class Spikes(Object):

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "spikes")
        self.image = load_single_spike_image(width, height)
        self.mask = pygame.mask.from_surface(self.image)
