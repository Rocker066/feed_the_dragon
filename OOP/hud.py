import pygame


class HUD:
    """A class to show the score and lives and the game title"""

    def __init__(self, fd_game):
        """Initialize the hud attributes"""
        self.screen = fd_game.display_surface
        self.settings = fd_game.settings

        # Render score text
        self.score_text = self.settings.font.render(
                'Score : ' + str(self.settings.score),
                 True, self.settings.GREEN, self.settings.DARKGREEN)
        self.score_text_rect = self.score_text.get_rect()
        self.score_text_rect.topleft = (10, 10)

        # Render title text
        self.title_text = self.settings.font.render(
            '<< Feed the Dragon >>', True, self.settings.WHITE)
        self.title_text_rect = self.title_text.get_rect()
        self.title_text_rect.centerx = self.settings.WIDTH // 2
        self.title_text_rect.y = 10

        # Render lives text
        self.lives_text = self.settings.font.render(
            'Lives : ' + str(self.settings.player_lives),
            True, self.settings.GREEN, self.settings.DARKGREEN)
        self.lives_text_rect = self.lives_text.get_rect()
        self.lives_text_rect.topright = (self.settings.WIDTH - 10, 10)

        # Render created_by text
        self.created_by_text = self.settings.font2.render('Created by: MAHYAR', True, self.settings.WHITE)
        self.created_by_text_rect = self.created_by_text.get_rect()
        self.created_by_text_rect.center = (self.settings.WIDTH // 2, self.settings.HEIGHT - 20)


    def render_score(self):
        self.score_text_rect.topleft = (10, 10)
        self.score_text = self.settings.font.render(
            'Score : ' + str(self.settings.score),
            True, self.settings.GREEN, self.settings.DARKGREEN)


    def render_lives(self):
        self.lives_text = self.settings.font.render(
            'Lives : ' + str(self.settings.player_lives),
            True, self.settings.GREEN, self.settings.DARKGREEN)


    def render_game_over(self):
        self.score_text_rect.centerx = (self.settings.WIDTH // 2)
        self.score_text_rect.y = 44
        self.screen.blit(self.score_text, self.score_text_rect)
        game_over_text = self.settings.font.render(
            'Game Over', True, self.settings.RED)
        game_over_text_rect = game_over_text.get_rect()
        game_over_text_rect.center = (self.settings.WIDTH // 2 ,self.settings.HEIGHT // 2 )

        continue_text = self.settings.font.render(
            'Press ENTER to play again', True, self.settings.WHITE)
        continue_text_rect = continue_text.get_rect()
        continue_text_rect.center = (self.settings.WIDTH // 2, self.settings.HEIGHT // 2 + 84)

        self.screen.blit(game_over_text, game_over_text_rect)
        self.screen.blit(continue_text, continue_text_rect)


    def render_paused_screen(self):
        paused_text = self.settings.font.render(
            'PAUSED', True, self.settings.GREEN
        )
        paused_text_rect = paused_text.get_rect()
        paused_text_rect.center = (self.settings.WIDTH // 2, self.settings.HEIGHT // 2)
        self.screen.blit(paused_text, paused_text_rect)


    def render_start_screen(self):
        start_title = self.settings.font.render(
            '<> Feed the Dragon <>', True, self.settings.WHITE
        )
        start_title_rect = start_title.get_rect()
        start_title_rect.center = (self.settings.WIDTH // 2, self.settings.HEIGHT // 2 + 50)

        start_text = self.settings.font.render(
            'Press ENTER to start', True, self.settings.GREEN
        )
        start_text_rect = start_text.get_rect()
        start_text_rect.center = (self.settings.WIDTH // 2, self.settings.HEIGHT // 2 - 50)

        self.screen.blit(start_title, start_title_rect)
        self.screen.blit(start_text, start_text_rect)


    def blit_me(self):
        self.screen.blit(self.score_text, self.score_text_rect)
        self.screen.blit(self.title_text, self.title_text_rect)
        self.screen.blit(self.lives_text, self.lives_text_rect)
        pygame.draw.line(self.screen, self.settings.WHITE,
                         (0, 64), (self.settings.WIDTH, 64), 2)
        self.screen.blit(self.created_by_text, self.created_by_text_rect)