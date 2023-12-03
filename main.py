import pygame
import sys
import random
import copy
from pygame_widgets.button import Button
import pygame_widgets
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
            elif board[x][y] == 3:
                if p3==1:
                    wh = pygame.image.load("./img/bh8.png")
                    screen.blit(wh, (rect.center[0]-45, rect.center[1]-45))
                else:
                    wh = pygame.image.load("./img/bh"+s+".png")
                    screen.blit(wh, (rect.center[0] -45, rect.center[1] -45))



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
                    if nx < 0 or nx >= BOARD_SIZE or ny < 0 or ny >= BOARD_SIZE or board[nx][ny] == player or board[nx][ny] == 3:
                        continue
                    while board[nx][ny] != 0:
                        nx += dx
                        ny += dy
                        if nx < 0 or nx >= BOARD_SIZE or ny < 0 or ny >= BOARD_SIZE or board[nx][ny] == 3:
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
        if nx < 0 or nx >= BOARD_SIZE or ny < 0 or ny >= BOARD_SIZE or board[nx][ny] == player or board[nx][ny] == 3:
            continue
        while board[nx][ny] != 0 and board[nx][ny] != 3:
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

def get_score(board,p2):
    black_score = 0
    white_score = 0
    for x in range(BOARD_SIZE):
        for y in range(BOARD_SIZE):
            if board[x][y] == 1:
                black_score += 1
            elif board[x][y] == 2:
                white_score += 1
    if p2==1:
        return black_score, white_score
    return white_score, black_score


def ai_move(board, player,p1,p2,p3):
    valid_moves = get_valid_moves(board, player,p3)
    if not valid_moves:
        return None
    best_move = None

    if p1==1:
        best_score = -1
        for move in valid_moves:
            new_board = copy.deepcopy(board)
            make_move(new_board, player, move)
            score = get_score(new_board)[player - 1]
            if score > best_score:
                best_move = move
                best_score = score
    else:
        best_score = 100
        for move in valid_moves:
            new_board = copy.deepcopy(board)
            make_move(new_board, player, move)
            score = get_score(new_board,p2)[player - 1]
            if score < best_score:
                best_move = move
                best_score = score
    return best_move

# Define main function
def main(p1,p2,p3,p4,p5,name1,name2):
    if p3==1:
        SQUARE_SIZE = 100
        # Define constants
        BOARD_SIZE = 8
    else:
        SQUARE_SIZE = 80
        # Define constants
        BOARD_SIZE = 10

    black_holes_coord = []
    if p5==1:
        for x in range(random.randint(1,BOARD_SIZE//2)):
            black_holes_coord.append((random.randint(0,BOARD_SIZE//2-2),random.randint(0,BOARD_SIZE//2-1)))
        for x in range(random.randint(1,BOARD_SIZE//2)):
            black_holes_coord.append((random.randint(BOARD_SIZE//2+1,BOARD_SIZE-1),random.randint(0,BOARD_SIZE-1)))
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
    for x in range(len(black_holes_coord)):
        board[black_holes_coord[x][0]][black_holes_coord[x][1]] = 3
    player = 1
    game_over = False

    cor_x = int()
    cor_y = int()

    # Game loop
    if p4==0 or p4==None:
        while not game_over:

            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return 1
                if event.type == pygame.MOUSEBUTTONDOWN and player == 1:
                    x, y = event.pos[0] // SQUARE_SIZE, event.pos[1] // SQUARE_SIZE
                    if (x, y) in get_valid_moves(board, player,p3):
                        make_move(board, player, (x, y))
                        player = 3 - player
                if player == 2:
                    move = ai_move(board, player,p1,p2,p3)
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
            black_score, white_score = get_score(board,p2)
            font = pygame.font.SysFont(None, 30)
            if p2==1:
                black_text = font.render("Black: {}".format(black_score), True, WHITE)
                white_text = font.render("White: {}".format(white_score), True, WHITE)
            else:
                black_text = font.render("Black: {}".format(black_score), True, WHITE)
                white_text = font.render("White: {}".format(white_score), True, WHITE)

            screen.blit(black_text, (10, BOARD_SIZE * SQUARE_SIZE - 40))
            screen.blit(white_text, (BOARD_SIZE * SQUARE_SIZE - 110, BOARD_SIZE * SQUARE_SIZE - 40))

            clock = pygame.time.Clock()

            ticks = pygame.time.get_ticks()
            millis = ticks % 1000
            seconds = int(ticks / 1000 % 60)
            minutes = int(ticks / 60000 % 24)

            out = '{minutes:02d}:{seconds:02d}:{millis}'.format(minutes=minutes, millis=millis, seconds=seconds)
            timer = font.render("Time: "+out, True, WHITE)
            screen.blit(timer, (10, 10))

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
        if black_score < white_score and (p2==1 or p2==None):
            text = font.render("Black wins!", True, BLACK)
        if black_score > white_score and (p2==1 or p2==None):
            text = font.render("White wins!", True, BLACK)
        if black_score > white_score and p2==0:
            text = font.render("Black wins!", True, BLACK)
        if black_score < white_score and p2==0:
            text = font.render("White wins!", True, BLACK)
        if(black_score==white_score):
            text = font.render("Tie game!", True, BLACK)

        screen.blit(text, (WINDOW_SIZE[0] // 2 - text.get_width() // 2, WINDOW_SIZE[1] // 2 - text.get_height() // 2))
        pygame.display.flip()

        while True:
            text1 = font.render("Turn to menu by 5 seconds", True, BLACK)
            screen.blit(text1,(WINDOW_SIZE[0] // 2 - text.get_width() // 2-130, WINDOW_SIZE[1] // 2 - text.get_height() // 2-200))
            pygame.display.flip()
            pygame.time.delay(5000)
            return True
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

    if p4==1:
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

                if event.type == pygame.MOUSEBUTTONDOWN and player == 2:
                    x, y = event.pos[0] // SQUARE_SIZE, event.pos[1] // SQUARE_SIZE
                    if (x, y) in get_valid_moves(board, player,p3):
                        make_move(board, player, (x, y))
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
            black_score, white_score = get_score(board,p2)
            font = pygame.font.SysFont(None, 30)
            if p2==1:
                black_text = font.render("Black: {}".format(black_score), True, WHITE)
                white_text = font.render("White: {}".format(white_score), True, WHITE)
            else:
                black_text = font.render("White: {}".format(black_score), True, WHITE)
                white_text = font.render("Black: {}".format(white_score), True, WHITE)

            screen.blit(black_text, (10, BOARD_SIZE * SQUARE_SIZE - 40))
            screen.blit(white_text, (BOARD_SIZE * SQUARE_SIZE - 110, BOARD_SIZE * SQUARE_SIZE - 40))

            clock = pygame.time.Clock()

            ticks = pygame.time.get_ticks()
            millis = ticks % 1000
            seconds = int(ticks / 1000 % 60)
            minutes = int(ticks / 60000 % 24)

            out = '{minutes:02d}:{seconds:02d}:{millis}'.format(minutes=minutes, millis=millis, seconds=seconds)
            timer = font.render("Time: " + out, True, WHITE)
            screen.blit(timer, (10, 10))
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
        if black_score > white_score and (p2==1 or p2==None):
            text = font.render("Black wins!", True, BLACK)
        if black_score < white_score and (p2==1 or p2==None):
            text = font.render("White wins!", True, BLACK)
        if black_score < white_score and p2==0:
            text = font.render("Black wins!", True, BLACK)
        if black_score > white_score and p2==0:
            text = font.render("White wins!", True, BLACK)
        if(black_score==white_score):
            text = font.render("Tie game!", True, BLACK)

        screen.blit(text, (WINDOW_SIZE[0] // 2 - text.get_width() // 2, WINDOW_SIZE[1] // 2 - text.get_height() // 2))
        pygame.display.flip()

        # Wait for user to close window
        while True:
            text1 = font.render("Turn to menu by 5 seconds", True, BLACK)
            screen.blit(text1, (
            WINDOW_SIZE[0] // 2 - text.get_width() // 2 - 130, WINDOW_SIZE[1] // 2 - text.get_height() // 2 - 200))
            pygame.display.flip()
            pygame.time.delay(1000)
            return True
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
# Run main function
if __name__ == "__main__":
    main()