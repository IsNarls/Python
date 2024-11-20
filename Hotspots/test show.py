import pygame
import os
import time

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((1280, 900))  # Adjust the size as needed
clock = pygame.time.Clock()

# Folder containing your images
folder_path = r"C:\Users\narwh\Documents\Pythonshit\Hotspots\Support Files\NPC_Data"  # Update this path
images = [os.path.join(folder_path, img) for img in sorted(os.listdir(folder_path)) if img.endswith('.png')]
original_image = pygame.image.load(images)
resized_image = pygame.transform.scale(images, (1280, 900))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for img_path in images:
        image = pygame.image.load(img_path)
        pygame.draw.circle(screen, (255, 0, 0), Location, 10)
        pygame.display.flip()
        #time.sleep(0.1)  # Display each image for 0.1 seconds (adjust as needed)

pygame.quit()
