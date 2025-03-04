import pygame
import random

# Initialize game -tells computer that the following
# code should be interpretted as a game.
pygame.init()

# Step 1. Set up the display
height = 1000
width = 1200

WHITE = (255, 255, 255)

# this is reusable code that represents our game screen
screen = pygame.display.set_mode((width, height)) 

# this will allow us to show the title of the game when a 
# user opens our game
pygame.display.set_caption("Avoid the Falling Objects") 

# Set frame rate
clock = pygame.time.Clock() 
FPS = 60  

#. Step 2. Create player object
# Object - a data type that allows us to 
# pass in unique data, including
# functions and other objects.
class Player:
    def __init__(self):
        self.x = width // 2  # Start in the middle
        self.y = height - 60  # Near the bottom
        self.playerWidth = 50
        self.playerHeight = 50
        self.playerSpeed = 5  # How fast the player moves

    def move(self, keys): 
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.playerSpeed
        if keys[pygame.K_RIGHT] and self.x < width - self.playerWidth:
            self.x += self.playerSpeed

    def draw(self):
        pygame.draw.rect(screen, (0, 0, 255),  
        (self.x, self.y, self.playerWidth, self.playerHeight))
  
class FallingObject:
    def __init__(self):
        self.x = random.randint(0, width - 50)
        self.y = -50
        self.width = 50
        self.height = 50
        self.speed = random.randint(3, 7)

    def move(self):
        self.y += self.speed

    def draw(self):
        pygame.draw.rect(screen,  
        (255, 0, 0), (self.x, self.y, self.width, self.height))

    def off_screen(self):
        return self.y > height

player = Player()
falling_objects = []
score = 0
lives = 3
    
running = True

while running:
    clock.tick(FPS)
    screen.fill('WHITE')  # Clear screen

    # Player movement
    keys = pygame.key.get_pressed()
    player.move(keys)
    player.draw()



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


pygame.quit()