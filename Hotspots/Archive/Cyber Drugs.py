import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Draw Circles")

#color_value_1 = random.randint(0, 255)
#color_value_2 = random.randint(0, 255)
#color_value_3 = random.randint(0, 255)

# Function to draw circles
def draw_circles():
    for _ in range(1500):
        color_value_1 = random.randint(0, 255)
        color_value_2 = random.randint(0, 255)
        color_value_3 = random.randint(0, 255)
        x = random.randint(0, 1200)
        y = random.randint(0, 800)
        radius = random.randint(5, 20)  # Random radius between 5 and 20
        pygame.draw.circle(screen, (color_value_1, color_value_2, color_value_3), (x, y), radius)

# Main loop
running = True
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
pygame.quit()