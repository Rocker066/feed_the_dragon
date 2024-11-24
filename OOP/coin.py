import pygame
import random

class Coin:
    """Coin class"""

    def __init__(self, fd_game):
        """Initialize the coin and its starting position."""
        self.screen = fd_game.display_surface
        self.settings = fd_game.settings

        # Load the dragon image and set its rect attribute.
        self.coin_image = pygame.image.load('assets/coin.png')
        self.coin_image_rect = self.coin_image.get_rect()
        self.coin_image_rect.x = self.settings.WIDTH + self.settings.BUFFER_DISTANCE
        self.coin_image_rect.y = random.randint(64, self.settings.HEIGHT - 32)

        # Set coin sound assets
        self.coin_sound = pygame.mixer.Sound('assets/coin_sound.wav')
        self.miss_sound = pygame.mixer.Sound('assets/miss_sound.wav')


    def reset(self):
        self.coin_image_rect.x = self.settings.WIDTH + self.settings.BUFFER_DISTANCE
        self.coin_image_rect.y = random.randint(64, self.settings.HEIGHT - 32)


    def move(self):
            self.coin_image_rect.x -= self.settings.coin_velocity


    def play_coin_sound(self):
        self.coin_sound.set_volume(.1)
        self.coin_sound.play()


    def stop_coin_sound(self):
        self.coin_sound.stop()


    def play_miss_sound(self):
        self.miss_sound.set_volume(.1)
        self.miss_sound.play()


    def stop_miss_sound(self):
        self.miss_sound.play()


    def blit_me(self):
        self.screen.blit(self.coin_image, self.coin_image_rect)
