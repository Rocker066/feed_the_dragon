import pygame

from settings import Settings
from dragon import Dragon
from coin import Coin
from hud import HUD


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
        pygame.display.set_caption('Feed the Dragon OOP')

        # Make an instance of the HUD
        self.hud = HUD(self)

        # Make an instance of a dragon
        self.dragon = Dragon(self)

        # Make an instance of a coin
        self.coin = Coin(self)

        # Create a clock
        self.clock = pygame.time.Clock()

        # Set the state of the game loop to running
        self.running = True
        self.game_started = False
        self.paused = False

        # Play background music
        pygame.mixer.music.load('assets/ftd_background_music.wav')
        pygame.mixer.music.set_volume(.1)
        pygame.mixer.music.play(-1, 0.0)


    def run_game(self):
        # Show the start menu for the first run of the game
        if not self.game_started:
            self._start_menu()

        while self.running:
            # check for key pressed
            self._check_events()

            # Run if the game is not paused by pressing escape
            if not self.paused:
                # Update the screen
                self._update_screen()

                # Moving coins
                self.coin.move()

                # Check for key held down
                self._key_held_down()

                # Detect collision
                self._collision()

                # Detect miss
                self._detect_miss()

                # Detect game over
                self._detect_game_over()

                # Hide the mouse cursor.
                pygame.mouse.set_visible(False)

                # Set framerate
                self.clock.tick(self.settings.FPS)
            else:
                self.display_surface.fill(self.settings.BLACK)
                self.hud.render_paused_screen()
                pygame.display.update()


    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    self.running = False

                if event.key == pygame.K_ESCAPE:
                    self.paused = not self.paused
                    print(self.paused)


    def _start_menu(self):
        while not self.game_started:
            self.display_surface.fill(self.settings.BLACK)
            self.hud.render_start_screen()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    # Start game on Enter key press
                    if event.key == pygame.K_RETURN:
                        # Exit the start screen loop
                        self.game_started = True


    def _key_held_down(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.dragon.image_rect.top > 64:
            self.dragon.move_up()

        if keys[pygame.K_DOWN] and self.dragon.image_rect.bottom < self.settings.HEIGHT:
            self.dragon.move_down()


    def _collision(self):
        if self.dragon.image_rect.colliderect(self.coin.image_rect):
            self.coin.play_coin_sound()
            self.settings.score += 1
            self.settings.coin_velocity += self.settings.COIN_ACCELERATION
            self.hud.render_score()
            self.coin.reset()


    def _detect_miss(self):
        if self.coin.image_rect.x < 0:
            self.coin.play_miss_sound()
            self.settings.player_lives -= 1
            self.hud.render_lives()
            self.coin.reset()


    def _detect_game_over(self):
        if self.settings.player_lives == 0:
            self.display_surface.fill(self.settings.BLACK)
            self.hud.render_game_over()
            pygame.display.update()

            # Pause the game until player presses a key, then reset the game
            pygame.mixer.music.stop()
            is_paused = True
            while is_paused:
                # Player wants to play again
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        pygame.mixer.music.play()
                        self.settings.reset()
                        self.dragon.reset()
                        self.hud.render_lives()
                        self.hud.render_score()
                        is_paused = False

                    # Player wants to quit
                    if event.type == pygame.QUIT:
                        is_paused = False
                        self.running = False


    def _update_screen(self):
        self.display_surface.fill(self.settings.BLACK)

        # Draw HUD
        self.hud.blit_me()

        # Draw the dragon
        self.dragon.blit_me()

        # Draw the coin
        self.coin.blit_me()

        # Flip the display
        pygame.display.flip()



if __name__ == '__main__':
    fd = FeedDragon()
    fd.run_game()

