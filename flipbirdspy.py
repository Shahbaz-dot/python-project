import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Clock
clock = pygame.time.Clock()
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLUE = (135, 206, 235)
GREEN = (0, 200, 0)

# Fonts
font = pygame.font.SysFont(None, 40)

# Game Variables
gravity = 0.5
bird_movement = 0
game_active = True
score = 0

# Bird
bird_surface = pygame.Surface((30, 30))
bird_surface.fill((255, 255, 0))
bird_rect = bird_surface.get_rect(center=(100, HEIGHT // 2))

# Pipes
pipe_width = 60
pipe_height = 400
pipe_gap = 150
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200)

def create_pipe():
    height = random.randint(150, 450)
    bottom_pipe = pygame.Rect(WIDTH, height, pipe_width, HEIGHT - height)
    top_pipe = pygame.Rect(WIDTH, height - pipe_gap - pipe_height, pipe_width, pipe_height)
    return top_pipe, bottom_pipe

def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 3
    return [pipe for pipe in pipes if pipe.right > 0]

def draw_pipes(pipes):
    for pipe in pipes:
        pygame.draw.rect(screen, GREEN, pipe)

def check_collision(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            return False
    if bird_rect.top <= 0 or bird_rect.bottom >= HEIGHT:
        return False
    return True

def display_score(score):
    score_surface = font.render(f'Score: {score}', True, (0, 0, 0))
    screen.blit(score_surface, (10, 10))

# Game loop
while True:
    screen.fill(BLUE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                bird_movement = -8
            if event.key == pygame.K_SPACE and not game_active:
                game_active = True
                pipe_list.clear()
                bird_rect.center = (100, HEIGHT // 2)
                bird_movement = 0
                score = 0

        if event.type == SPAWNPIPE and game_active:
            pipe_list.extend(create_pipe())

    if game_active:
        # Bird
        bird_movement += gravity
        bird_rect.centery += int(bird_movement)
        screen.blit(bird_surface, bird_rect)

        # Pipes
        pipe_list = move_pipes(pipe_list)
        draw_pipes(pipe_list)

        # Collision
        game_active = check_collision(pipe_list)

        # Scoring
        for pipe in pipe_list:
            if pipe.centerx == bird_rect.centerx:
                score += 0.5  # top and bottom pipe both count once
        display_score(int(score))
    else:
        game_over_surface = font.render("Game Over - Press Space", True, (255, 0, 0))
        screen.blit(game_over_surface, (40, HEIGHT // 2 - 50))

    pygame.display.update()
    clock.tick(FPS)

