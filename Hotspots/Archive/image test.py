import pygame as pg

# Initialize Pygame
pg.init()

# Set up your display
screen_width, screen_height = 1280, 900
screen = pg.display.set_mode((screen_width, screen_height))

# Load your large image
large_image = pg.image.load(r"C:\Users\narwh\OneDrive\Documents\Pythonshit\Hotspots\Support Files\Background.png")  # Replace with your image path
large_image_rect = large_image.get_rect()

# Scrolling position
scroll_x, scroll_y = 0, 0
scroll_speed = 10  # Speed of scrolling

# Game loop
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    keys = pg.key.get_pressed()
    # Scroll based on key presses
    if keys[pg.K_LEFT]:
        scroll_x -= scroll_speed
    if keys[pg.K_RIGHT]:
        scroll_x += scroll_speed
    if keys[pg.K_UP]:
        scroll_y -= scroll_speed
    if keys[pg.K_DOWN]:
        scroll_y += scroll_speed

    # Ensure the scrolling stays within the bounds of the large image
    scroll_x = max(0, min(scroll_x, large_image_rect.width - screen_width))
    scroll_y = max(0, min(scroll_y, large_image_rect.height - screen_height))

    # Draw everything
    screen.fill((0, 0, 0))  # Clear the screen
    # Draw the portion of the large image based on scroll position
    screen.blit(large_image, (-scroll_x, -scroll_y))

    # Update the display
    pg.display.flip()

pg.quit()