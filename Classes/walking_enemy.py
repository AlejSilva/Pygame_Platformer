import pygame
from components.load_sprites import load_sprite_sheets


class WalkingEnemy(pygame.sprite.Sprite):
    COLOR = (0, 0, 255)
    GRAVITY = 1
    ANIMATION_DELAY = 3
    SPRITES = load_sprite_sheets("Traps", "SpikeHead", 32, 32, True)


    def __init__(self, x, y, width, height):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.x_vel = 0
        self.animation_count = 0
        self.direction = "left"
        self.timer = 0
        self.name = "enemy"

    def move(self, dx):
        self.rect.x += dx

    def loop(self):
        # Increment the timer
        self.timer += 1  

        # Check if it's time to change the movement direction
        if self.timer >= 150: #Since game is running at 30 FPS, when timer is at 90 it means 3 seconds
            if self.direction == "left":
                self.direction = "right"  
            else:
                self.direction = "left" 
            self.timer = 0  # Reset the timer

        if self.direction == "left":
            self.y_vel = -self.GRAVITY
        else:
            self.y_vel = self.GRAVITY

        self.move(self.y_vel)
        self.update_sprite()

    def update_sprite(self):
        sprite_sheet = "idle"
         
        sprite_sheet_name = sprite_sheet + "_" + self.direction
        sprites = self.SPRITES[sprite_sheet_name]

        sprite_index = (self.animation_count //
                        self.ANIMATION_DELAY) % len(sprites)
        self.sprite = sprites[sprite_index]
        self.animation_count += 1
        self.update()

    def update(self):
        self.rect = self.sprite.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.sprite)

    def draw(self, win, offset_x):
        win.blit(self.sprite, (self.rect.x - offset_x, self.rect.y))
