import pygame


class Dragon:
    """Dragon class"""
    def __init__(self, fd_game):
        """Initialize the dragon and its starting position."""
        self.screen = fd_game.display_surface
        self.settings = fd_game.settings

        # Load the dragon image and set its rect attribute.
        self.image = pygame.image.load('assets/dragon_right.png')
        self.image_rect = self.image.get_rect()
        self.image_rect.left = 32
        self.image_rect.centery = self.settings.HEIGHT // 2 + 32


    def move_up(self):
        self.image_rect.y -= self.settings.PLAYER_VELOCITY


    def move_down(self):
        self.image_rect.y += self.settings.PLAYER_VELOCITY


    def reset(self):
        self.image_rect.left = 32
        self.image_rect.centery = self.settings.HEIGHT // 2 + 32


    def blit_me(self):
        self.screen.blit(self.image, self.image_rect)