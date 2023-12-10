"""! @brief Reversi Documentation."""
##
# @mainpage Reversi
#
# @section description_main Description

# Reversi is a classic two-player board game that has been around for decades.
#
# @section notes_main Functions
#1. Game menu
# - Start button - opens a new window with game settings:
# - Choose the number of rounds or a quick game (1 round)
# - Game option selection: regular reversi, NxN reversi, anti-reversi, black hole reversi
# - choosing the color of the chips that the user is playing for
# - The "Start game" button
# - Settings button - opens a new window with settings:
# - selecting the player's name
# - choosing the design of the board and chips
# - The "Save" button saves the settings and goes to the previous menu
# - Exit button - displays the dialog box "Do you want to exit the game?" with options for exiting the game or returning to the game.
#2. Gameplay
# - drawing the board and pieces on the screen, highlighting the figure (frames around the figure) after clicking on it, selecting available cells for making a move (implementing one of the rules of the game), placing chips on the cells available for the move
# - changing the color of a number of chips after a successful move by the opponent (implementing one of the rules of the game)
# - implementing the algorithm behavior of the opponent bot (computer)
# - implementation of the algorithm for determining the end of the game
# - request statistics and its visualization
# - the ability to pause the game with the display of a dialog box:
# - Resume game button
# - Exit the game button - return to the main menu of the program
# - Restart button - restart the game with the same parameters
# - the visual part:
# - Game time display
# - displaying the score of the round (for example, the ratio of chips)
# - Displaying the score of the game (if it is a multi-round game)
# - Displaying the round counter (if it is a multi-round game)
# - Displaying the player's name
# - at the end of the game, the dialog box is displayed:
# - name of the winner
# - The score of the game if it is a multi-round game
# - Exit or Restart buttons
#
# Copyright (c) 2020 Sanya Workshop.  All rights reserved.
##
# @file menu.py
import pygame
import pygame_widgets
from pygame_widgets.button import Button
from pygame_widgets.textbox import TextBox
from pygame.locals import *
import sys
import main
from pygame_widgets.dropdown import Dropdown

# Initialize pygame
pygame.init()

# Constants
WIDTH = 800
HEIGHT = 800
BACKGROUND_COLOR = (0, 0, 0)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Reversi Menu")
screen.blit(pygame.image.load("./img/menu3.png"), (0, 0))

# Set the font
font = pygame.font.SysFont("Unispace", 70)

btn1 = Button(
    screen,  # Surface to place button on
    WIDTH // 2 - 75,  # X-coordinate of top left corner
    HEIGHT // 2 - 150,  # Y-coordinate of top left corner
    150,  # Width
    100,  # Height
    text='Start Game',  # Text to display
    fontSize=30,  # Size of font
    margin=20,  # Minimum distance between text/image and edge of button
    inactiveColour=(144, 77, 48),  # Colour of button when not being interacted with
    pressedColour=(140, 71, 67),  # Colour of button when being clicked
    radius=20,  # Radius of border corners (leave empty for not curved)
    onClick=lambda: start(),  # Function to call when clicked on
    font=pygame.font.SysFont("Unispace", 30)
)

btn2 = Button(
    screen,  # Surface to place button on
    WIDTH // 2 - 75,  # X-coordinate of top left corner
    HEIGHT // 2 + 175,  # Y-coordinate of top left corner
    150,  # Width
    100,  # Height
    text='Quit',  # Text to display
    fontSize=30,  # Size of font
    margin=20,  # Minimum distance between text/image and edge of button
    inactiveColour=(144, 77, 48),  # Colour of button when not being interacted with
    pressedColour=(140, 71, 67),  # Colour of button when being clicked
    radius=20,  # Radius of border corners (leave empty for not curved)
    onClick=lambda: sys.exit(),  # Function to call when clicked on
    font=pygame.font.SysFont("Unispace", 30)
)

dropdown1 = Dropdown(
    screen,  # Surface to place dropdown on
    WIDTH // 2 - 250,  # X-coordinate of top left corner
    HEIGHT // 2 - 150,  # Y-coordinate of top left corner
    150,  # Width
    100,  # Height
    name='Select mode',  # Dropdown name
    choices=['Reversi', 'Antireversi'],  # Dropdown choices
    borderRadius=20,  # Radius of border corners (leave empty for not curved)
    colour=pygame.Color((144, 77, 48)),  # Colour of dropdown
    values=[True, False],  # Dropdown values
    direction='down',  # Dropdown direction
    textHAlign='centre',  # Text alignment
    fontSize=30,  # Size of font
    font=pygame.font.SysFont("Unispace", 30)
)

# Repeat the same pattern for dropdown2, dropdown3, dropdown4, and dropdown5

dropdown2 = Dropdown(
    screen,  # Surface to place dropdown on
    WIDTH // 2 + 100,  # X-coordinate of top left corner
    HEIGHT // 2 - 150,  # Y-coordinate of top left corner
    150,  # Width
    100,  # Height
    name='Select color',  # Dropdown name
    choices=['Black', 'White'],  # Dropdown choices
    borderRadius=20,  # Radius of border corners (leave empty for not curved)
    colour=pygame.Color((144, 77, 48)),  # Colour of dropdown
    values=[True, False],  # Dropdown values
    direction='down',  # Dropdown direction
    textHAlign='centre',  # Text alignment
    fontSize=30,  # Size of font
    font=pygame.font.SysFont("Unispace", 30)
)

# Repeat the same pattern for dropdown3, dropdown4, and dropdown5

dropdown3 = Dropdown(
    screen,  # Surface to place dropdown on
    WIDTH // 2 - 75,  # X-coordinate of top left corner
    HEIGHT // 2,  # Y-coordinate of top left corner
    150,  # Width
    50,  # Height
    name='Choose board',  # Dropdown name
    choices=['8', '10'],  # Dropdown choices
    borderRadius=20,  # Radius of border corners (leave empty for not curved)
    colour=pygame.Color((144, 77, 48)),  # Colour of dropdown
    values=[True, False],  # Dropdown values
    direction='down',  # Dropdown direction
    textHAlign='centre',  # Text alignment
    fontSize=30,  # Size of font
    font=pygame.font.SysFont("Unispace", 25)
)

# Repeat the same pattern for dropdown4 and dropdown5

dropdown4 = Dropdown(
    screen,  # Surface to place dropdown on
    WIDTH // 2 + 100,  # X-coordinate of top left corner
    HEIGHT // 2,  # Y-coordinate of top left corner
    150,  # Width
    50,  # Height
    name='Choose players',  # Dropdown name
    choices=['1', '2'],  # Dropdown choices
    borderRadius=20,  # Radius of border corners (leave empty for not curved)
    colour=pygame.Color((144, 77, 48)),  # Colour of dropdown
    values=[False, True],  # Dropdown values
    direction='down',  # Dropdown direction
    textHAlign='centre',  # Text alignment
    fontSize=30)

dropdown5 = Dropdown(
    screen,  # Surface to place dropdown on
    WIDTH // 2 - 250,  # X-coordinate of top left corner
    HEIGHT // 2,  # Y-coordinate of top left corner
    150,  # Width
    50,  # Height
    name='Black holes',  # Dropdown name
    choices=['Yes', 'No'],  # Dropdown choices
    borderRadius=20,  # Radius of border corners (leave empty for not curved)
    colour=pygame.Color((144, 77, 48)),  # Colour of dropdown
    values=[True, False],  # Dropdown values
    direction='down',  # Dropdown direction
    textHAlign='centre',  # Text alignment
    fontSize=30,  # Size of font
    font=pygame.font.SysFont("Unispace", 25)
)
textbox_name1 = TextBox(
    screen,  # Surface to place textbox on
    WIDTH // 2 - 250,  # X-coordinate of top left corner
    HEIGHT // 2 + 100,  # Y-coordinate of top left corner
    150,  # Width
    50,  # Height
    fontSize=30,  # Size of font
    borderColour=(144, 77, 48),  # Colour of border
    textColour=(0, 0, 0),  # Colour of text
    radius=20,  # Radius of border corners
    borderThickness=5  # Thickness of border
)

textbox_name2 = TextBox(
    screen,  # Surface to place textbox on
    WIDTH // 2 + 100,  # X-coordinate of top left corner
    HEIGHT // 2 + 100,  # Y-coordinate of top left corner
    150,  # Width
    50,  # Height
    fontSize=30,  # Size of font
    borderColour=(144, 77, 48),  # Colour of border
    textColour=(0, 0, 0),  # Colour of text
    radius=20,  # Radius of border corners
    borderThickness=5  # Thickness of border
)


def start():
    """
    This function starts the program by getting selected values from dropdowns and text from textboxes.
    It then calls the main function with the selected values and text inputs, and performs further actions
    based on the return value of the main function.
    """

    # Get selected values from dropdowns
    a = dropdown1.getSelected()
    b = dropdown2.getSelected()
    c = dropdown3.getSelected()
    d = dropdown4.getSelected()
    e = dropdown5.getSelected()

    # Get text from textboxes
    name1 = textbox_name1.getText()
    name2 = textbox_name2.getText()

    # Call the main function with the selected values and text inputs
    rest = main.main(a, b, c, d, e, name1, name2)

    # Check the return value of the main function
    if rest == 1:
        # If return value is 1, draw the menu
        draw_menu()
    else:
        # If return value is not 1, exit the program
        sys.exit()
def draw_menu():
    """
    This function draws a menu on the screen.
    It handles events, clears the screen, loads and displays an image, updates the state of the pygame widgets, and updates the display.
    """
    run = True
    while run:
        # Get all the events
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
                sys.exit()

        # Clear the screen and fill it with black color
        screen.fill((0, 0, 0), pygame.Rect(0, 400, 800, 800))

        # Load and display the menu image
        screen.blit(pygame.image.load("./img/menu2.png"), (0, 0))

        # Update the state of the pygame widgets
        pygame_widgets.update(events)

        # Update the display
        pygame.display.update()
        pygame.display.flip()

draw_menu()