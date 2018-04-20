# ICS3U
# Assignment 2: Action
# Jazmin M

# adapted from http://www.101computing.net/getting-started-with-pygame/

# Import the pygame library and initialise the game engine
# Don't forget to import your class
import pygame
import random
from bat import Bat
pygame.init()

# Define some colours
# Colours are defined using RGB values
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GREY = (155,149,150)
# Set the screen size
SCREENWIDTH = 400
SCREENHEIGHT = 400

background = pygame.image.load("The_Cave_artwork.jpg")

speed=25
# Open a new window
# The window is defined as (width, height), measured in pixels
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Animation")
screen.blit(background, (0,0))

all_sprites_list = pygame.sprite.Group()
    
Bat1 = Bat(GREY, 20,30)
Bat1.rect.x = 200
Bat1.rect.y = 300

Bat2 = Bat(GREY, 20,30)
Bat2.rect.x = 100
Bat2.rect.y = 300

all_sprites_list.add(Bat1)
all_sprites_list.add(Bat2)

all_bats = pygame.sprite.Group()
all_bats.add(Bat1)
all_bats.add(Bat2)





# This loop will continue until the user exits the game
carryOn = True

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

#---------Main Program Loop----------
while carryOn:
    # --- Main event loop ---
    for event in pygame.event.get(): # Player did something
        if event.type == pygame.QUIT: # Player clicked close button
            carryOn = False

    # --- Game logic goes here
    # There should be none for a static image
    
    for bat in all_bats:
        bat.moveForward(speed)
        if bat.rect.y > SCREENHEIGHT:
            bat.changeSpeed(random.randint(50,100))
            #car.repaint(random.choice(colorList))
            bat.rect.y = -200


    
    
    # --- Draw code goes here
    

    # Clear the screen to white
    #screen.fill(WHITE)
    screen.blit(background, (0,0))
    all_sprites_list.update()
    all_sprites_list.draw(screen)

    # Queue different shapes and lines to be drawn
    # pygame.draw.rect(screen, RED, [55, 200, 100, 70], 0)
    # pygame.draw.line(screen, GREEN, [0, 0], [100, 100], 5)
    # pygame.draw.ellipse(screen, BLACK, [20, 20, 250, 100], 2)

    # Update the screen with queued shapes
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Once the main program loop is exited, stop the game engine
pygame.quit()
