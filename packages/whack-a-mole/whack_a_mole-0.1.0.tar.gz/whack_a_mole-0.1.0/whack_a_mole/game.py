import pygame
import random
import sys
import os

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Whack-a-Mole")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Load mole image
mole_image_path = os.path.join(os.path.dirname(__file__), 'assets', 'mole.png')
mole_image = pygame.image.load(mole_image_path)
mole_rect = mole_image.get_rect()

# Game variables
mole_position = (random.randint(0, WIDTH - mole_rect.width), random.randint(0, HEIGHT - mole_rect.height))
score = 0
font = pygame.font.Font(None, 74)
clock = pygame.time.Clock()
mole_display_time = 1000  # Time in milliseconds the mole is displayed
last_mole_time = pygame.time.get_ticks()

def run_game():
    global mole_position, score, last_mole_time

    running = True
    while running:
        screen.fill(WHITE)
        
        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if mole_rect.collidepoint(event.pos):
                    score += 1
                    mole_position = (random.randint(0, WIDTH - mole_rect.width), random.randint(0, HEIGHT - mole_rect.height))
                    last_mole_time = pygame.time.get_ticks()
        
        # Update mole position after a certain time
        if pygame.time.get_ticks() - last_mole_time > mole_display_time:
            mole_position = (random.randint(0, WIDTH - mole_rect.width), random.randint(0, HEIGHT - mole_rect.height))
            last_mole_time = pygame.time.get_ticks()
        
        mole_rect.topleft = mole_position
        screen.blit(mole_image, mole_position)
        
        # Display score
        score_text = font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (10, 10))
        
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
    sys.exit()
