import pygame
import random
from collections import deque 

# Initialize Pygame
#pygame.init()

# Set up the display
#screen = pygame.display.set_mode((1200, 800))
#pygame.display.set_caption("Draw Circles")


def Read_location_file():
            file_path = rf"C:\Users\narwh\OneDrive\Documents\Pythonshit\Hotspots\Support Files\Location"
            with open(file_path, "r") as f:
                content =  f.readlines()
                print(content)
                f.close()


def draw_from_file():
    Read_location_file()
    #pygame.draw.circle(screen, (color_value_1, color_value_2, color_value_3), (x, y), radius)

# Main loop
"""running = True
while running:
    # Fill the screen with a background color
    screen.fill((255, 255, 255))

    # Draw the circles
    draw_circles()

    # Update the display
    pygame.display.flip()

    # Event loop to check for quitting
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit Pygame
pygame.quit()"""

draw_circles()
draw_from_file()