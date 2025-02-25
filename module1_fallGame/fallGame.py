import pygame
import random

# Initialize game -tells computer that the following
# code should be interpretted as a game.
pygame.init()

# Step 1. Set up the display
height = 1000
width = 1200

# this is reusable code that represents our game screen
screen = pygame.display.set_mode((width, height)) 

# this will allow us to show the title of the game when a 
# user opens our game
pygame.display.set_caption("Avoid the Falling Objects") 

# Set frame rate
clock = pygame.time.Clock() 
FPS = 60  

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


pygame.quit()

#. Step 2. Create player object
# Object - a data type that allows us to 
# pass in unique data, including
# functions and other objects.
