import pygame
import random
from settings import Settings


class FeedDragon:
    """The main class of feed the dragon game"""

    def __init__(self):
        """The game attributes"""
        # Initialize pygame
        pygame.init()

        # Initialize settings
        self.settings = Settings()

        # Set the display surface
        self.display_surface = pygame.display.set_mode((self.settings.WIDTH, self.settings.HEIGHT))
        pygame.display.set_caption('Feed the Dragon')

        self.clock = pygame.time.Clock()

        self.running = True


    def run_game(self):
        while self.running:

            self._check_events()

            self._update_screen()


    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False


    def _update_screen(self):
        self.display_surface.fill(self.settings.BLACK)

        pygame.display.flip()



if __name__ == '__main__':
    fd = FeedDragon()
    fd.run_game()

