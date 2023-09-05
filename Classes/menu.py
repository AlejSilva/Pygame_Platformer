import pygame

WIDTH, HEIGHT = 1000, 800


#Menu for pausing, restarting resuming the game 
class Menu:
    def __init__(self):
        self.options = ["Resume", "Restart", "Quit"]
        self.selected_option = 0
        self.font = pygame.font.Font(None, 36)
        self.menu_active = False

    def toggle_menu(self):
        self.menu_active = not self.menu_active
        self.selected_option = 0

    def draw(self, screen):
        if self.menu_active:
            for i, option in enumerate(self.options):
                text = self.font.render(option, True, (255, 255, 255))
                text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + i * 40))
                if i == self.selected_option:
                    pygame.draw.rect(screen, (255, 0, 0), text_rect, 2)
                screen.blit(text, text_rect)

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.selected_option = (self.selected_option - 1) % len(self.options)
        if keys[pygame.K_DOWN]:
            self.selected_option = (self.selected_option + 1) % len(self.options)
        if keys[pygame.K_RETURN]:
            if self.options[self.selected_option] == "Resume":
                self.toggle_menu()
            elif self.options[self.selected_option] == "Restart":
                # Implement game restart logic here
                pass
            elif self.options[self.selected_option] == "Quit":
                pygame.quit()
                quit()