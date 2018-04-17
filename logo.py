# ICS3U
# Assignment 2: Logo
# Jazmin M

# adapted from http://www.101computing.net/getting-started-with-pygame/

# Import the pygame library and initialise the game engine
import pygame
pygame.init()

# Define some colours
# Colours are defined using RGB values
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (93, 175, 252)
PINK = (247, 133, 218)

# Set the screen size (please don't change this)
SCREENWIDTH = 400
SCREENHEIGHT = 400

# Open a new window
# The window is defined as (width, height), measured in pixels
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Logo")

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
    
    # --- Draw code goes here

    # Clear the screen to white
    screen.fill(WHITE)

    # Queue different shapes and lines to be drawn
    pygame.draw.polygon(screen, BLACK, [[200,0],[0,200],[200,400],[400,200]])
    #^this is the diamond which everything else wil be drawn onto^
    pygame.draw.line(screen, WHITE,[50,0], [275,200], 30)
    #^line connecting 1st and 2nd elipse^
    pygame.draw.ellipse(screen, WHITE, [173,110,60,60],0)
    #^1st ellipse^
    pygame.draw.line(screen, WHITE, [202,125], [202,300], 25)
    #^line connecting 1st ellipse and 3rd ellipse^
    pygame.draw.ellipse(screen,WHITE, [255,182,60,60],0)
    #^2nd ellipse^
    pygame.draw.ellipse(screen, WHITE,[173,260,60,60],0)
    #^3rd ellipse^
    

    # Update the screen with queued shapes
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Once the main program loop is exited, stop the game engine
pygame.quit()
