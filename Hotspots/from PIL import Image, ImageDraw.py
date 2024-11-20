import os
import time
from PIL import Image, ImageDraw
import random



class Drawingframes():

    def __init__(self):
        # Paths configuration
        self.image_path = r'C:\Users\narwh\Documents\Pythonshit\Hotspots\Support Files\Background4.png'
        self.output_path = r"C:\Users\narwh\Documents\Pythonshit\Hotspots\Support Files\Frames\output_image.png"
        self.coords_folder = r'C:\Users\narwh\Documents\Pythonshit\Hotspots\Support Files\NPC_DATA'
        self.counter = 0
        # Open the base image
        self.img = Image.open(self.image_path)
        self.draw = ImageDraw.Draw(self.img)

    def draw_dots_on_image(self):
     while True:
        # Iterate over each file in the NPC_DATA folder
        for filename in os.listdir(self.coords_folder):
            # Only process files that seem to be data files 
                file_path = os.path.join(self.coords_folder, filename)
                with open(file_path, 'r') as file:
                    for line in file:
                        # Parse the coordinates by stripping parentheses and splittings
                        line = line.strip().strip('()')
                        x = line.partition(',')  # Remove parentheses
                        #print(x)
                        self.draw.ellipse((int(x[0]) - 5, (int(x[2]))  - 5, (int(x[0]))  + 5, (int(x[2]))  + 5), fill='red')
                        output_name = self.counter = self.counter + 1
                        str_conversion = str(output_name)
                        output_path = rf"C:\Users\narwh\Documents\Pythonshit\Hotspots\Support Files\Frames\output_image{str_conversion}.png"

        # Save the modified image
        self.img.save(output_path)
        print(f'Dots drawn and saved to {output_path}')

start = Drawingframes()
start.draw_dots_on_image()

    




