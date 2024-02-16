import pygame
import random

pygame.init()
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 500
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('First Pygame')
clock = pygame.time.Clock()
running = True


score = 0
lives = 5
speed = 5
playsound = True


dt = 0
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)


title_font = pygame.font.SysFont('impact', 40)
score_font = pygame.font.SysFont('impact', 25)
lives_font = pygame.font.SysFont('impact', 25)
game_over_font = pygame.font.SysFont('impact', 85)
restart_game_font = pygame.font.SysFont('impact', 30)


title_text = title_font.render('Feed Puppy', True, '#3d5f9f', 'silver')
score_text = score_font.render(f'Score: {score}', True, '#3d5f9f', 'silver')
lives_text = lives_font.render(f'Lives: {lives}', True, '#3d5f9f', 'silver')
game_over_text = game_over_font.render('Game Over', True, '#3d5f9f', 'silver')
restart_game_text = restart_game_font.render("Pres 'p' to play again...", True, '#3d5f9f', 'silver')


title_text_rect = title_text.get_rect()
score_text_rect = score_text.get_rect()
lives_text_rect = lives_text.get_rect()
game_over_text_rect = game_over_text.get_rect()
restart_game_text_rect = restart_game_text.get_rect()


title_text_rect.center = (WINDOW_WIDTH / 2, 30)
score_text_rect.topleft = (10, 5)
lives_text_rect.topleft = ((WINDOW_WIDTH - lives_text.get_width() - 10), 5)
game_over_text_rect.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
restart_game_text_rect.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 + 100)

puppy = pygame.image.load('images/aspen2.png')
food = pygame.image.load('images/food2.png')

puppy_rect = puppy.get_rect()
food_rect = food.get_rect()

puppy_rect.center = (60, WINDOW_HEIGHT/2)
food_rect.x = WINDOW_WIDTH - 100
food_rect.y = random.randint(65, (WINDOW_HEIGHT - food.get_height()))


pygame.mixer.music.load('sounds/bg.wav')
pygame.mixer.music.play(-1, 0.0)

hit_sound = pygame.mixer.Sound('sounds/dog.mp3')
miss_sound = pygame.mixer.Sound('sounds/aww.mp3')
game_over_sound = pygame.mixer.Sound('sounds/game_over.mp3')




while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # screen color
    screen.fill('silver')

    screen.blit(title_text, title_text_rect)
    screen.blit(score_text, score_text_rect)
    screen.blit(lives_text, lives_text_rect)

    if lives == 0:
        screen.blit(game_over_text, game_over_text_rect)
        screen.blit(restart_game_text, restart_game_text_rect)
        food_rect.x = WINDOW_WIDTH + 100
        # food_rect.y = 10000

        if playsound:
            pygame.mixer.music.stop()
            game_over_sound.play()
            playsound = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_p]:
            speed = 5
            score = 0
            lives = 5
            score_text = score_font.render(f'Score: {score}', True, '#3d5f9f', 'silver')
            lives_text = lives_font.render(f'Lives: {lives}', True, '#3d5f9f', 'silver')
            playsound = True
            pygame.mixer.music.play(-1, 0.0)


    screen.blit(puppy, puppy_rect)
    screen.blit(food, food_rect)

    pygame.draw.line(screen, '#3d5f9f', (0, 60), (WINDOW_WIDTH, 60), 2)

    keys = pygame.key.get_pressed()

    if (keys[pygame.K_UP] or keys[pygame.K_w]) and puppy_rect.y > 70:
        puppy_rect.y -= 300 * dt

    if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and puppy_rect.y < WINDOW_HEIGHT - puppy.get_height() - 5:
        puppy_rect.y += 300 * dt

    if food_rect.x < 0:
        miss_sound.play()
        lives -= 1
        lives_text = lives_font.render(f'Lives: {lives}', True, '#3d5f9f', 'silver')
        food_rect.x = WINDOW_WIDTH + 100
        food_rect.y = random.randint(65, (WINDOW_HEIGHT - food.get_height()))

    else:
        food_rect.x -= speed


    if puppy_rect.colliderect(food_rect):
        hit_sound.play()
        score += 1
        speed += 1
        score_text = score_font.render(f'Score: {score}', True, '#3d5f9f', 'silver')
        food_rect.x = WINDOW_WIDTH + 100
        food_rect.y = random.randint(65, (WINDOW_HEIGHT - food.get_height()))

    # display
    pygame.display.flip()

    dt = clock.tick(60) / 1000









pygame.quit()
