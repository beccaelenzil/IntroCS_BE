import math
# Import a library of functions called 'pygame'
import pygame
# Initialize the game engine
pygame.init()

# Define some colors
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)
PI = math.pi

#Opening and setting the window size
size = (700, 500)
screen = pygame.display.set_mode(size)

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Starting position of the rectangle
rect_x = 50
rect_y = 50

# Speed and direction of rectangle
rect_change_x = 5
rect_change_y = 5

# -------- Main Program Loop -----------
while done == False:
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop

    # Set the screen background
    screen.fill(BLACK)

    # Draw the rectangle
    pygame.draw.rect(screen, WHITE, [rect_x, rect_y, 50, 50])

    # Move the rectangle starting point
    rect_x += rect_change_x
    rect_y += rect_change_y

    if rect_change_x > 0:
        rect_change_x += 0.1
    else:
        rect_change_x -= 0.1


    # Bounce the rectangle if needed
    if rect_y > 450 or rect_y < 0:
        rect_change_y = rect_change_y * -1
    if rect_x > 650 or rect_x < 0:
        rect_change_x = rect_change_x * -1


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)
