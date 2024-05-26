# breakout_game/game.py

import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)

# Ball properties
ball_speed = [4, 4]
ball_radius = 10

# Paddle properties
paddle_width = 100
paddle_height = 10
paddle_speed = 6

# Block properties
block_rows = 5
block_cols = 8
block_width = 75
block_height = 20
block_margin = 5

# Setup screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Breakout Game')

# Ball setup
ball = pygame.Rect(screen_width // 2, screen_height // 2, ball_radius * 2, ball_radius * 2)

# Paddle setup
paddle = pygame.Rect(screen_width // 2 - paddle_width // 2, screen_height - paddle_height - 30, paddle_width, paddle_height)

# Blocks setup
blocks = []
for row in range(block_rows):
    for col in range(block_cols):
        block = pygame.Rect(col * (block_width + block_margin) + block_margin, row * (block_height + block_margin) + block_margin, block_width, block_height)
        blocks.append(block)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move paddle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.move_ip(-paddle_speed, 0)
    if keys[pygame.K_RIGHT] and paddle.right < screen_width:
        paddle.move_ip(paddle_speed, 0)

    # Move ball
    ball.x += ball_speed[0]
    ball.y += ball_speed[1]

    # Ball collision with walls
    if ball.left <= 0 or ball.right >= screen_width:
        ball_speed[0] = -ball_speed[0]
    if ball.top <= 0:
        ball_speed[1] = -ball_speed[1]
    if ball.bottom >= screen_height:
        pygame.quit()
        sys.exit()

    # Ball collision with paddle
    if ball.colliderect(paddle):
        ball_speed[1] = -ball_speed[1]

    # Ball collision with blocks
    hit_index = ball.collidelist(blocks)
    if hit_index != -1:
        hit_block = blocks.pop(hit_index)
        ball_speed[1] = -ball_speed[1]

    # Clear screen
    screen.fill(black)

    # Draw ball
    pygame.draw.ellipse(screen, white, ball)

    # Draw paddle
    pygame.draw.rect(screen, blue, paddle)

    # Draw blocks
    for block in blocks:
        pygame.draw.rect(screen, red, block)

    # Update display
    pygame.display.flip()
    clock.tick(60)
