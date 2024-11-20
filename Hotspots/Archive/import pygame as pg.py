import pygame as pg
from pathlib import Path
import ast
import threading
import time

# Shared data structure for NPC coordinates
npc_coordinates = []

# Function to load NPC locations in a separate thread
def load_NPC_locations():
    NPC_data_dir = r"C:\Users\narwh\Documents\Pythonshit\Hotspots\Support Files\NPC_DATA"
    data_dir = Path(NPC_data_dir)
    while running:  # Keep running while the main loop is active
        global npc_coordinates
        npc_coordinates.clear()  # Clear previous coordinates
        for file in data_dir.iterdir():
            if file.is_file():
                with open(file, 'r') as temp_npc_data:
                    for line in temp_npc_data:
                        try:
                            coord = ast.literal_eval(line.strip())
                            npc_coordinates.append(coord)
                        except Exception as e:
                            print(f"Error parsing line: {line.strip()} - {e}")
        print(f"Loaded coordinates: {npc_coordinates}")  # Debugging statement
        time.sleep(1)  # Control the loading rate

# Initialize Pygame
pg.init()
screen = pg.display.set_mode((800, 600))

# Flag to control the main loop
running = True

# Start thread to load NPC locations
load_thread = threading.Thread(target=load_NPC_locations)
load_thread.start()

# Main loop
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # Clear the screen
    screen.fill((255, 255, 255))  # Fill with white

    # Draw NPC locations
    for x, y in npc_coordinates:
        pg.draw.circle(screen, (255, 0, 0), (x, y), 20)

    # Draw other elements (example)
    pg.draw.rect(screen, (0, 255, 0), (100, 100, 50, 50))

    # Update the display
    pg.display.flip()

# Clean up
load_thread.join()
pg.quit()
