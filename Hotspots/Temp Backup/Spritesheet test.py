import pygame

# Initialize Pygame
pygame.init()

# Load the sprite sheet
sprite_sheet_image = pygame.image.load('spritesheet.png').convert_alpha()

# Function to extract a sprite
def get_sprite(sheet, x, y, width, height):
    sprite = pygame.Surface((width, height), pygame.SRCALPHA)
    sprite.blit(sheet, (0, 0), (x, y, width, height))
    return sprite

# Example of extracting sprites
sprite1 = get_sprite(sprite_sheet_image, 0, 0, 32, 32)  # Top-left sprite
sprite2 = get_sprite(sprite_sheet_image, 32, 0, 32, 32)  # Next sprite over

# Set up the game window
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))  # Clear the screen
    screen.blit(sprite1, (100, 100))  # Draw sprite 1
    screen.blit(sprite2, (150, 100))  # Draw sprite 2
    pygame.display.flip()  # Update the display
    clock.tick(60)  # Limit the frame rate

pygame.quit()