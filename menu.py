import pygame
from pygame.locals import *
WIDTH = 800
HEIGHT = 600
BACKGROUND_COLOR = (0, 0, 0)
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Reversi Menu")
font = pygame.font.SysFont("Arial", 50)
running = True
while running:
# Handle Events
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
    # Fill Background
    screen.fill(BACKGROUND_COLOR)

    # Render Menu
    title_text = font.render("Reversi Menu", True, (255, 255, 255))
    screen.blit(title_text, (WIDTH/2 - title_text.get_width()/2, HEIGHT/4))

    option1_text = font.render("1. Start Game", True, (255, 255, 255))
    screen.blit(option1_text, (WIDTH/2 - option1_text.get_width()/2, HEIGHT/2))

    option2_text = font.render("2. Instructions", True, (255, 255, 255))
    screen.blit(option2_text, (WIDTH/2 - option2_text.get_width()/2, HEIGHT/2 + 60))

    option3_text = font.render("3. Quit", True, (255, 255, 255))
    screen.blit(option3_text, (WIDTH/2 - option3_text.get_width()/2, HEIGHT/2 + 120))

    pygame.display.flip()
pygame.quit()