#write location file
import pygame
import random
from collections import deque 




def Write_time_to_file(Location):
        file_path = rf"C:\Users\narwh\OneDrive\Documents\Pythonshit\Hotspots\Support Files\Location"
        with open(file_path, "a") as f:
            f.write(Location) 
            f.close()



def draw_circles():
    for _ in range(1500):
        radius = random.randint(5, 20)  # Random radius between 5 and 20
        color_value_1 = random.randint(0, 255)
        color_value_2 = random.randint(0, 255)
        color_value_3 = random.randint(0, 255)
        x = random.randint(0, 1200)
        y = random.randint(0, 800)
        location = str(rf'{color_value_1}, {color_value_2}, {color_value_3}, {x, y}, {radius}')
        Write_time_to_file(location)
