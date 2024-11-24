import pygame.font


class Settings:
    """A class for  feed the dragon  settings"""
    def __init__(self):
        """Set display surface"""
        self.WIDTH = 1000
        self.HEIGHT = 400

        # Set framerate
        self.FPS = 60

        # Set game values
        self.PLAYER_STARTING_LIVES = 3
        self.PLAYER_VELOCITY = 5
        self.COIN_STARTING_VELOCITY = 5
        self.COIN_ACCELERATION = .5
        self.BUFFER_DISTANCE = 100

        self.score = 0
        self.player_lives = self.PLAYER_STARTING_LIVES
        self.coin_velocity = self.COIN_STARTING_VELOCITY

        # Set colors
        self.GREEN = (0, 255, 0)
        self.DARKGREEN = (10, 50, 10)
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0 ,0)

        # Set font
        self.font = pygame.font.Font('assets/AttackGraffiti.ttf', 32)


    def reset(self):
        self.player_lives = self.PLAYER_STARTING_LIVES
        self.score = 0
        self.coin_velocity = self.COIN_STARTING_VELOCITY

