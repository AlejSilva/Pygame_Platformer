#Game reset if dead
def reset_game(self):
    self.rect.x = 100
    self.rect.y = 100
    self.is_alive = True