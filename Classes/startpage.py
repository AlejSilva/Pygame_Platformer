import os
import pygame
from os.path import join

twoBitFont = os.path.join(os.path.dirname(__file__), "fonts", "PressStart2P-Regular.ttf")

WIDTH, HEIGHT = 1000, 800
window = pygame.display.set_mode((WIDTH, HEIGHT))

# Load the background image
background_image = pygame.image.load("assets/Background/startBackground.jpg")

class StartPage:
    def __init__(self, screen_width, screen_height):
        self.screen_width = WIDTH
        self.screen_height = HEIGHT
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Leap of Legends")
        self.font = pygame.font.Font(twoBitFont, 22)

        #Start Button
        self.start_button = pygame.Rect(400, 400, 200, 50)
        self.start_text = self.font.render("START", True, (255, 255, 255))
        self.start_text_rect = self.start_text.get_rect(center=self.start_button.center)

        #Exit Button
        self.exit_button = pygame.Rect(400, 470, 200, 50)
        self.exit_text = self.font.render("EXIT", True, (255, 255, 255))
        self.exit_text_rect = self.exit_text.get_rect(center=self.exit_button.center)

        # Track if the mouse is hovering over the buttons
        self.start_hovered = False
        self.exit_hovered = False

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.start_button.collidepoint(event.pos):
                    return "main_game"
                elif self.exit_button.collidepoint(event.pos):
                    pygame.quit()
                    quit()

        # Check if the mouse is hovering over the buttons
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.start_hovered = self.start_button.collidepoint(mouse_x, mouse_y)
        self.exit_hovered = self.exit_button.collidepoint(mouse_x, mouse_y)

        return None

    def draw(self):
        #Background, 
        self.screen.blit(background_image, (0, 0))

        # Draw buttons with different colors based on hover state
        start_color = (100, 100, 100) if self.start_hovered else (50, 50, 50)
        exit_color = (100, 100, 100) if self.exit_hovered else (50, 50, 50)

        #Start button
        pygame.draw.rect(self.screen, start_color, self.start_button)
        self.screen.blit(self.start_text, self.start_text_rect)

        #Exit Button
        pygame.draw.rect(self.screen, exit_color, self.exit_button)
        self.screen.blit(self.exit_text, self.exit_text_rect)

        # Draw the game title on the window
        font = pygame.font.Font(twoBitFont, 56)
        fontSmall = pygame.font.Font(twoBitFont, 32)
        gameTitleTop = font.render("LEAP", True, (255, 255, 255))
        gameTitleMiddle = fontSmall.render("OF", True, (255, 255, 255))
        gameTitleBottom = font.render("LEGENDS", True, (255, 255, 255))

        window.blit(gameTitleTop, (385, 150))  # Adjust the position as needed
        window.blit(gameTitleMiddle, (465, 220))
        window.blit(gameTitleBottom, (310, 270))

        pygame.display.flip()