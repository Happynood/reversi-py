import pygame
import sys
import random
import copy

# Define constants
BOARD_SIZE = 8
SQUARE_SIZE = 50
WINDOW_SIZE = (BOARD_SIZE * SQUARE_SIZE, BOARD_SIZE * SQUARE_SIZE)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
BLUE = (0, 0, 200)
RED = (200, 0, 0)
YELLOW = (255, 255, 0)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Reversi")

# Define helper functions
def draw_board(board):
    for x in range(BOARD_SIZE):
        for y in range(BOARD_SIZE):
            rect = pygame.Rect(x * SQUARE_SIZE, y * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
            pygame.draw.rect(screen, GREEN, rect)
            if board[x][y] == 1:
                pygame.draw.circle(screen, BLACK, rect.center, SQUARE_SIZE // 2 - 5)
            elif board[x][y] == 2:
                pygame.draw.circle(screen, WHITE, rect.center, SQUARE_SIZE // 2 - 5)