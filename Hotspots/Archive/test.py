import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("NPC Path with Vectors")

# Define colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# NPC properties
npc_pos = pygame.Vector2(700, 500)
speed = 1

# Path defined by start and end points
start_point = pygame.Vector2(700, 500)          
end_point = pygame.Vector2(100,100)

# Calculate direction and normalize
direction = end_point - start_point
if direction.length() != 0:
    direction.normalize_ip()  # Normalize in place

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update NPC position along the path
    if npc_pos.distance_to(end_point) > speed:
        npc_pos += direction * speed
    else:
        npc_pos = end_point  # Stop at the endpoint

    # Fill the screen with white
    screen.fill(WHITE)

    # Draw the NPC (as a blue circle)
    pygame.draw.circle(screen, BLUE, (int(npc_pos.x), int(npc_pos.y)), 10)

    # Draw the path line
    pygame.draw.line(screen, (0, 0, 0), start_point, end_point, 2)

    # Update the display
    pygame.display.flip()