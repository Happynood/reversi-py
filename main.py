import pygame
import sys
import random
import copy

# Define constants
BOARD_SIZE = 8
SQUARE_SIZE = 100
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
screen.blit(pygame.image.load("./img/game1.png"), (0, 0))

# Define helper functions
def draw_board(board):
    screen.blit(pygame.image.load("./img/game.png"), (0, 0))
    for x in range(BOARD_SIZE):
        for y in range(BOARD_SIZE):
            rect = pygame.Rect(x * SQUARE_SIZE, y * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)

            #pygame.draw.rect(screen, GREEN, rect)
            if board[x][y] == 1:
                wh = pygame.image.load("./img/black.png")
                screen.blit(wh,(rect.center[0]-50,rect.center[1]-50))

            elif board[x][y] == 2:
                wh = pygame.image.load("./img/white.png")
                screen.blit(wh, (rect.center[0] - 50, rect.center[1] - 50))


def get_valid_moves(board, player):
    valid_moves = []
    for x in range(BOARD_SIZE):
        for y in range(BOARD_SIZE):
            if board[x][y] == 0:
                for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]:
                    nx, ny = x + dx, y + dy
                    if nx < 0 or nx >= BOARD_SIZE or ny < 0 or ny >= BOARD_SIZE or board[nx][ny] == player:
                        continue
                    while board[nx][ny] != 0:
                        nx += dx
                        ny += dy
                        if nx < 0 or nx >= BOARD_SIZE or ny < 0 or ny >= BOARD_SIZE:
                            break
                        if board[nx][ny] == player:
                            valid_moves.append((x, y))
                            break
    return valid_moves

def make_move(board, player, move):
    x, y = move
    board[x][y] = player
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= BOARD_SIZE or ny < 0 or ny >= BOARD_SIZE or board[nx][ny] == player:
            continue
        while board[nx][ny] != 0:
            nx += dx
            ny += dy
            if nx < 0 or nx >= BOARD_SIZE or ny < 0 or ny >= BOARD_SIZE:
                break
            if board[nx][ny] == player:
                while True:
                    nx -= dx
                    ny -= dy
                    if nx == x and ny == y:
                        break
                    board[nx][ny] = player
                break

def get_score(board):
    black_score = 0
    white_score = 0
    for x in range(BOARD_SIZE):
        for y in range(BOARD_SIZE):
            if board[x][y] == 1:
                black_score += 1
            elif board[x][y] == 2:
                white_score += 1
    return black_score, white_score

def ai_move(board, player):
    valid_moves = get_valid_moves(board, player)
    if not valid_moves:
        return None
    best_move = None
    best_score = -1
    for move in valid_moves:
        new_board = copy.deepcopy(board)
        make_move(new_board, player, move)
        score = get_score(new_board)[player - 1]
        if score > best_score:
            best_move = move
            best_score = score
    return best_move

# Define main function
def main():

    # Initialize game state
    board = [[0] * BOARD_SIZE for _ in range(BOARD_SIZE)]
    board[3][3] = board[4][4] = 1
    board[3][4] = board[4][3] = 2
    player = 1
    game_over = False

    # Game loop
    while not game_over:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and player == 1:
                x, y = event.pos[0] // SQUARE_SIZE, event.pos[1] // SQUARE_SIZE
                if (x, y) in get_valid_moves(board, player):
                    make_move(board, player, (x, y))
                    player = 3 - player
            if player == 2:
                move = ai_move(board, player)
                if move is not None:
                    make_move(board, player, move)
                    player = 3 - player

        # Draw board
        draw_board(board)

        # Draw valid moves
        for move in get_valid_moves(board, player):
            rect = pygame.Rect(move[0] * SQUARE_SIZE, move[1] * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
            pygame.draw.rect(screen, BLUE, rect, 3)

        # Draw scores
        black_score, white_score = get_score(board)
        font = pygame.font.SysFont(None, 30)
        black_text = font.render("Black: {}".format(black_score), True, BLACK)
        white_text = font.render("White: {}".format(white_score), True, WHITE)
        screen.blit(black_text, (10, BOARD_SIZE * SQUARE_SIZE - 40))
        screen.blit(white_text, (BOARD_SIZE * SQUARE_SIZE - 110, BOARD_SIZE * SQUARE_SIZE - 40))

        # Update screen
        pygame.display.flip()

        # Check for game over
        if not get_valid_moves(board, player):
            player = 3 - player
            if not get_valid_moves(board, player):
                game_over = True

    # Draw game over screen
    draw_board(board)
    font = pygame.font.SysFont(None, 50)
    if black_score > white_score:
        text = font.render("Black wins!", True, BLACK)
    elif white_score > black_score:
        text = font.render("White wins!", True, WHITE)
    else:
        text = font.render("Tie game!", True, YELLOW)
    screen.blit(text, (WINDOW_SIZE[0] // 2 - text.get_width() // 2, WINDOW_SIZE[1] // 2 - text.get_height() // 2))
    pygame.display.flip()

    # Wait for user to close window
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

# Run main function
if __name__ == "__main__":
    main()