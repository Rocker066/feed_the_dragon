import pygame
import random


# Initialize pygame
pygame.init()

# Set display surface
WIDTH = 1000
HEIGHT = 400
display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Feed the Dragon')

# Set framerate
FPS = 60
clock = pygame.time.Clock()

# Set game values
PLAYER_STARTING_LIVES = 2
PLAYER_VELOCITY = 5
COIN_STARTING_VELOCITY = 5
COIN_ACCELERATION = .5
BUFFER_DISTANCE = 100

score = 0
player_lives = PLAYER_STARTING_LIVES
coin_velocity = COIN_STARTING_VELOCITY

# Set colors
GREEN = (0, 255, 0)
DARKGREEN = (10, 50, 10)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set fonts
font = pygame.font.Font('assets/AttackGraffiti.ttf', 32)
# persian_font = pygame.font.Font('assets/BJALAL.TTF', 32)

# # Persian text
# persian_text = "به اژدها غذا بده"
# reshaped_text = arabic_reshaper.reshape(persian_text)  # Reshape the text
# bidi_text = get_display(reshaped_text)  # Get the display string for right-to-left rendering

# Set text
score_text = font.render('Score : ' + str(score), True, GREEN)
score_text_rect = score_text.get_rect()
score_text_rect.topleft = (10, 10)

title_text = font.render('<< Feed the Dragon >>', True, WHITE)
title_text_rect = title_text.get_rect()
title_text_rect.centerx = WIDTH // 2
title_text_rect.y = 10

lives_text = font.render('Lives : ' + str(player_lives), True, GREEN)
lives_text_rect = lives_text.get_rect()
lives_text_rect.topright = (WIDTH - 10, 10)

game_over_text = font.render('Game Over', True, GREEN, DARKGREEN)
game_over_text_rect = game_over_text.get_rect()
game_over_text_rect.center = (WIDTH // 2, HEIGHT // 2)

continue_text = font.render('Press any key to play again', True, GREEN, DARKGREEN)
continue_text_rect = continue_text.get_rect()
continue_text_rect.center = (WIDTH // 2, HEIGHT // 2 + 64)

# Set sounds and music
coin_sound = pygame.mixer.Sound('assets/coin_sound.wav')
miss_sound = pygame.mixer.Sound('assets/miss_sound.wav')
miss_sound.set_volume(.1)
pygame.mixer.music.load('assets/ftd_background_music.wav')

# Set images
player_image = pygame.image.load('assets/dragon_right.png')
player_image_rect = player_image.get_rect()
player_image_rect.left = 32
player_image_rect.centery = HEIGHT // 2

coin_image = pygame.image.load('assets/coin.png')
coin_image_rect = coin_image.get_rect()
coin_image_rect.x = WIDTH + BUFFER_DISTANCE
coin_image_rect.y = random.randint(64, HEIGHT - 32)

# Main game loop
pygame.mixer.music.set_volume(.1)
pygame.mixer.music.play(-1, 0.0)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Check if the player wants to move
    keys = pygame.key.get_pressed()
    if (keys[pygame.K_UP] or keys[pygame.K_w]) and player_image_rect.top > 64:
        player_image_rect.y -= PLAYER_VELOCITY
    if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and player_image_rect.bottom < HEIGHT:
        player_image_rect.y += PLAYER_VELOCITY

    # Move the coin
    if coin_image_rect.x < 0:
        # Player missed the coin
        player_lives -= 1
        miss_sound.play()
        coin_image_rect.x = WIDTH + BUFFER_DISTANCE
        coin_image_rect.y = random.randint(64, HEIGHT -32)
    else:
        # Move the coin
        coin_image_rect.x -= coin_velocity

    # Check for collisions
    if player_image_rect.colliderect(coin_image_rect):

        score += 1
        coin_sound.play()
        coin_velocity += COIN_ACCELERATION
        coin_image_rect.x = WIDTH + BUFFER_DISTANCE
        coin_image_rect.y = random.randint(64, HEIGHT - 32)

    # Update the HUD
    score_text = font.render('Score : ' + str(score), True, GREEN)
    lives_text = font.render('Lives : ' + str(player_lives), True, GREEN)

    # Check for game over
    if player_lives == 0:
        display_surface.blit(game_over_text, game_over_text_rect)
        display_surface.blit(continue_text, continue_text_rect)
        pygame.display.update()


        pygame.mixer.music.stop()
        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                # Player wants to play again
                if event.type == pygame.KEYDOWN:
                    player_lives = PLAYER_STARTING_LIVES
                    score = 0
                    player_image_rect.y = HEIGHT // 2
                    coin_velocity = COIN_STARTING_VELOCITY
                    pygame.mixer.music.play(-1, 0.0)
                    # Pause the game until player pressed a key, then reset the game                    is_paused = False

                # Player want to quit
                if event.type == pygame.QUIT:
                    is_paused = False
                    running = False

    # Fill the screen
    display_surface.fill(BLACK)

    # Blit HUD to the screen
    display_surface.blit(score_text, score_text_rect)
    display_surface.blit(title_text, title_text_rect)
    display_surface.blit(lives_text, lives_text_rect)
    pygame.draw.line(display_surface, WHITE, (0, 64), (WIDTH, 64), 2)

    # Blit assets to the screen
    display_surface.blit(player_image, player_image_rect)
    display_surface.blit(coin_image, coin_image_rect)

    # Update screen
    pygame.display.flip()

    # Tick the clock
    clock.tick(FPS)

# End game
pygame.quit()