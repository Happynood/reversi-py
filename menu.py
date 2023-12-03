import pygame
import pygame_widgets
from pygame_widgets.button import Button
from pygame.locals import *
import sys
import main
from pygame_widgets.dropdown import Dropdown

WIDTH = 800
HEIGHT = 800
BACKGROUND_COLOR = (0, 0, 0)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Reversi Menu")
screen.blit(pygame.image.load("./img/menu3.png"), (0, 0))
font = pygame.font.SysFont("Unispace", 70)
btn1 = Button(
    # Mandatory Parameters
    screen,  # Surface to place button on
    WIDTH // 2 - 75,  # X-coordinate of top left corner
    HEIGHT // 2 - 150,  # Y-coordinate of top left corner
    150,  # Width
    100,  # Text to display
    fontSize=30,  # Size of font
    margin=20,  # Minimum distance between text/image and edge of button
    inactiveColour=(144, 77, 48),  # Colour of button when not being interacted with
    text='Start Game',
    pressedColour=(140, 71, 67),  # Colour of button when being clicked
    radius=20,  # Radius of border corners (leave empty for not curved)
    onClick=lambda: start(),  # Function to call when clicked on
font = pygame.font.SysFont("Unispace", 30)
)

btn2= Button(
    # Mandatory Parameters
    screen,  # Surface to place button on
    WIDTH // 2 - 75,  # X-coordinate of top left corner
    HEIGHT // 2 + 175,  # Y-coordinate of top left corner
    150,  # Width
    100,  # Text to display
    fontSize=30,  # Size of font
    margin=20,  # Minimum distance between text/image and edge of button
    inactiveColour=(144, 77, 48),  # Colour of button when not being interacted with
    text='Quit',
    pressedColour=(140, 71, 67),  # Colour of button when being clicked
    radius=20,  # Radius of border corners (leave empty for not curved)
    onClick=lambda: sys.exit(),  # Function to call when clicked on
font = pygame.font.SysFont("Unispace", 30)
)

dropdown1 = Dropdown(
    screen, WIDTH // 2 -250, HEIGHT // 2 , 150, 100, name='Select mode',
    choices=[
        'Reversi',
        'Antireversi'
    ],
    borderRadius=20,
    colour=pygame.Color((144, 77, 48)),
    values=[True,False],
    direction='down',
    textHAlign='centre',
    fontSize=30,
    font = pygame.font.SysFont("Unispace", 30)
)

dropdown2 = Dropdown(
    screen, WIDTH // 2 +100, HEIGHT // 2 , 150, 100, name='Select color',
    choices=[
        'Black',
        'White'
    ],
    borderRadius=20,
    colour=pygame.Color((144, 77, 48)),
    values=[True,False],
    direction='down',
    textHAlign='centre',
    fontSize=30,
    font = pygame.font.SysFont("Unispace", 30)
)

dropdown3 = Dropdown(
    screen, WIDTH // 2 +-75, HEIGHT // 2 , 150, 50, name='Choose board',
    choices=[
        '8',
        '10'
    ],
    borderRadius=20,
    colour=pygame.Color((144, 77, 48)),
    values=[True,False],
    direction='down',
    textHAlign='centre',
    fontSize=30,
    font = pygame.font.SysFont("Unispace", 25)
)

def start():
    a = dropdown1.getSelected()
    b = dropdown2.getSelected()
    c = dropdown3.getSelected()
    main.main(a,b,c)

title_text = font.render("Reversi Menu", True, (255, 255, 255))
screen.blit(title_text, (WIDTH / 2 - title_text.get_width() / 2, HEIGHT / 4-100))


def draw_menu():
    run = True
    while run:

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
                quit()

        screen.fill((0, 0, 0), pygame.Rect(0, 400, 800, 800))
        screen.blit(pygame.image.load("./img/menu2.png"), (0, 0))
        pygame_widgets.update(events)
        pygame.display.update()

draw_menu()