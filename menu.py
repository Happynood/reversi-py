import pygame
import pygame_widgets
from pygame_widgets.button import Button
from pygame.locals import *
import main
WIDTH = 800
HEIGHT = 800
BACKGROUND_COLOR = (0, 0, 0)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Reversi Menu")

font = pygame.font.SysFont("Arial", 70)

button = Button(
            # Mandatory Parameters
            screen,  # Surface to place button on
            WIDTH //2 -75,  # X-coordinate of top left corner
            HEIGHT//2-75,  # Y-coordinate of top left corner
            150,  # Width
            100,  # Text to display
            fontSize=30,  # Size of font
            margin=20,  # Minimum distance between text/image and edge of button
            inactiveColour=(255, 255, 255),  # Colour of button when not being interacted with
            text = 'Start Game',
            pressedColour=(100, 100, 100),  # Colour of button when being clicked
            radius=20,  # Radius of border corners (leave empty for not curved)
            onClick=lambda: main.main()  # Function to call when clicked on
        )

title_text = font.render("Reversi Menu", True, (255, 255, 255))
screen.blit(title_text, (WIDTH / 2 - title_text.get_width() / 2, HEIGHT / 4))
def draw_menu():
    running = True
    while running:
        # Handle Events
        events = pygame.event.get()
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        # Fill Background
        pygame_widgets.update(events)  # Call once every loop to allow widgets to render and listen
        pygame.display.update()


draw_menu()