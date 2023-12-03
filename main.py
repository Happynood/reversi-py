import pygame
import sys
import random
import copy

SQUARE_SIZE = 100
# Define constants
BOARD_SIZE = 8
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
def draw_board(board,p2,p3):
    if p3==1:
        SQUARE_SIZE = 100
        # Define constants
        BOARD_SIZE = 8
    else:
        SQUARE_SIZE = 80
        # Define constants
        BOARD_SIZE = 10
    screen.blit(pygame.image.load("./img/game.png"), (0, 0))
    for x in range(BOARD_SIZE):
        for y in range(BOARD_SIZE):
            rect = pygame.Rect(x * SQUARE_SIZE, y * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
            s = str()
            pr_x = int()
            pr_y = int()
            if p3==1:
                s = '10'
                pr_x, pr_y = 50, 50

            else:
                s = '8'
                pr_x, pr_y = 40, 40
            if board[x][y] == 1:
                if p2==1:
                    wh = pygame.image.load("./img/black"+s+".png")
                    screen.blit(wh,(rect.center[0]-pr_x,rect.center[1]-pr_y))
                else:
                    wh = pygame.image.load("./img/white"+s+".png")
                    screen.blit(wh, (rect.center[0] - pr_x, rect.center[1] - pr_y))
            elif board[x][y] == 2:
                if p2==1:
                    wh = pygame.image.load("./img/white"+s+".png")
                    screen.blit(wh, (rect.center[0] - pr_x, rect.center[1] - pr_y))
                else:
                    wh = pygame.image.load("./img/black"+s+".png")
                    screen.blit(wh, (rect.center[0] - pr_x, rect.center[1] - pr_y))


def get_valid_moves(board, player,p3):
    if p3==1:
        SQUARE_SIZE = 100
        # Define constants
        BOARD_SIZE = 8
    else:
        SQUARE_SIZE = 80
        # Define constants
        BOARD_SIZE = 10
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

def ai_move(board, player,p3):
    valid_moves = get_valid_moves(board, player,p3)
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
def main(p1,p2,p3):
    if p3==1:
        SQUARE_SIZE = 100
        # Define constants
        BOARD_SIZE = 8
    else:
        SQUARE_SIZE = 80
        # Define constants
        BOARD_SIZE = 10
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
    # Initialize game state
    board = [[0] * BOARD_SIZE for _ in range(BOARD_SIZE)]
    board[len(board)//2-1][len(board)//2-1] = board[len(board)//2][len(board)//2] = 1
    board[len(board)//2-1][len(board)//2] = board[len(board)//2][len(board)//2-1] = 2
    player = 1
    game_over = False

    cor_x = int()
    cor_y = int()

    # Game loop
    while not game_over:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and player == 1:
                x, y = event.pos[0] // SQUARE_SIZE, event.pos[1] // SQUARE_SIZE
                if (x, y) in get_valid_moves(board, player,p3):
                    make_move(board, player, (x, y))
                    player = 3 - player
            if player == 2:
                move = ai_move(board, player,p3)
                if move is not None:
                    make_move(board, player, move)
                    player = 3 - player

        # Draw board
        draw_board(board,p2,p3)
        check_x = int()
        check_y = int()

        # Draw valid moves
        for move in get_valid_moves(board, player,p3):
            rect = pygame.Rect(move[0] * SQUARE_SIZE, move[1] * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
            pygame.draw.rect(screen, BLUE, rect, 3)

        # Draw scores
        black_score, white_score = get_score(board)
        font = pygame.font.SysFont(None, 30)
        if p2==1:
            black_text = font.render("Black: {}".format(black_score), True, WHITE)
            white_text = font.render("White: {}".format(white_score), True, WHITE)
        else:
            black_text = font.render("White: {}".format(black_score), True, WHITE)
            white_text = font.render("Black: {}".format(white_score), True, WHITE)
        screen.blit(black_text, (10, BOARD_SIZE * SQUARE_SIZE - 40))
        screen.blit(white_text, (BOARD_SIZE * SQUARE_SIZE - 110, BOARD_SIZE * SQUARE_SIZE - 40))

        # Update screen
        pygame.display.flip()

        # Check for game over
        if not get_valid_moves(board, player,p3):
            player = 3 - player
            if not get_valid_moves(board, player,p3):
                game_over = True

    # Draw game over screen
    draw_board(board,p2,p3)
    font = pygame.font.SysFont(None, 50)
    if black_score > white_score and p1==1:
        text = font.render("Black wins!", True, BLACK)
    elif black_score < white_score and p1==1:
        text = font.render("White wins!", True, BLACK)
    if black_score < white_score and p1==0:
        text = font.render("Black wins!", True, BLACK)
    elif black_score > white_score and p1==0:
        text = font.render("White wins!", True, BLACK)
    else:
        text = font.render("Tie game!", True, BLACK)
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