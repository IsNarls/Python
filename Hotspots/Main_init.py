#start of game
# Import Modules
import os
import pygame as pg
import random
import time
import player
from multiprocessing import Process, Queue, Lock
from pathlib import Path
import ast 
import multiprocessing as mp
from itertools import chain
import Mark_Time
import os
from concurrent.futures import ThreadPoolExecutor
import cProfile
from pathlib import Path
from typing import List, Tuple, Union

file_lock = Lock()
First_count = 0 
Previous_y = 0
Player_counter = 0 
counter = 0
test_counter = 0


#unsure what this does figure out later 
if not pg.font:
    print("Warning, fonts disabled")
if not pg.mixer:
    print("Warning, sound disabled")

screen_width, screen_height = 1920, 1080#1280, 900


#previous_list_x = 0
#previous_list_y = 0
start_counter = 0
folder_path = r"C:\Users\narwh\Documents\Pythonshit\Hotspots\Support Files\NPC_Data"
main_dir = r"C:\Users\narwh\Documents\Pythonshit\Hotspots"
data_dir = r"C:\Users\narwh\Documents\Pythonshit\Hotspots\Support Files"

class NPC_DATA_FILES:
    
    def __init__(self, queue):
        self.counter = 0
        self.Master_list = []
        self.queue = queue


    def Read_NPC_Data_files(self):
        NPC_data_dir = r"C:\Users\narwh\Documents\Pythonshit\Hotspots\Support Files\NPC_DATA"
        data_dir = Path(NPC_data_dir)
        coordinates_batches = []  # To store batches of coordinate lists
        current_batch = []

        # Iterate through files in the directory
        for file in data_dir.iterdir():
            if file.is_file():
                with open(file, 'r') as temp_npc_data:
                    for line in temp_npc_data:
                        coord = ast.literal_eval(line.strip())
                        current_batch.append(coord)
                        # Check if the current batch has reached a specific size
                        if len(current_batch) >= 120:  # Adjust the batch size as needed
                            coordinates_batches.append(current_batch)
                            current_batch = []  # Reset for the next batch

        # Append any remaining coordinates in the current batch
        if current_batch:
            coordinates_batches.append(current_batch)

        return coordinates_batches    

    #"""def Read_NPC_Data_files(self):
    #    NPC_data_dir = r"C:\Users\narwh\Documents\Pythonshit\Hotspots\Support Files\NPC_DATA"
     #   data_dir = Path(NPC_data_dir)
     #   coordinates = []
      #  for file in data_dir.iterdir():
     #       if file.is_file():
     #           with open(file, 'r') as temp_npc_data:
      #              for line in temp_npc_data:
     #                   coord = ast.literal_eval(line.strip())
     #                   coordinates.append(coord)
     #   return coordinates"""

    def Write_location_to_file(self, Master_list):
        file_path = rf"C:\Users\narwh\Documents\Pythonshit\Hotspots\Support Files\Location"
        with open(file_path, "a") as f:
            f.write(str(Master_list)) 

    def Store_coordinates(self):
        while True:
            #time.sleep(1)
            coordinates = self.Read_NPC_Data_files()
            self.Master_list.append(coordinates)
            self.queue.put(self.Master_list)


class Spritesheet:
    def __init__(self, filepath: Path, sprite_size: Tuple[int, int], spacing: Tuple[int, int] = (0, 0), scale: Tuple[int, int] = None) -> None:
        """Initialize the spritesheet.

        Args:
            filepath (Path): Path to the spritesheet image file.
            sprite_size (Tuple[int, int]): Width and height of each sprite in the sheet.
            spacing (Tuple[int, int], optional): Spacing between each sprite (row spacing, column spacing). Defaults to (0, 0).
            scale (Tuple[int, int], optional): Rescale each sprite to the given size. Defaults to None.
        """
        self._sheet = pg.image.load(filepath).convert_alpha()
        self._sprite_size = sprite_size
        self._spacing = spacing
        self._scale = scale

    def get_sprite(self, loc: Tuple[int, int], colorkey: Union[pg.Color, int, None] = None) -> pg.Surface:
        """Load a specific sprite from the spritesheet.

        Args:
            loc (Tuple[int, int]): Location of the sprite in the sheet (row, column).
            colorkey (Union[pg.Color, int, None], optional): Color to be treated as transparent. Defaults to None.

        Returns:
            pg.Surface: The sprite image.
        """
        x = loc[1] * (self._sprite_size[0] + self._spacing[0])
        y = loc[0] * (self._sprite_size[1] + self._spacing[1])

        rect = pg.Rect(x, y, *self._sprite_size)
        image = pg.Surface(self._sprite_size, pg.SRCALPHA).convert_alpha()
        image.blit(self._sheet, (0, 0), rect)

        if colorkey is not None:
            if colorkey == -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey, pg.RLEACCEL)

        if self._scale:
            image = pg.transform.scale(image, self._scale)
        
        return image

    def get_sprites(self, locs: List[Tuple[int, int]], colorkey: Union[pg.Color, int, None] = None) -> List[pg.Surface]:
        """Load multiple sprites from the spritesheet.

        Args:
            locs (List[Tuple[int, int]]): List of locations of the sprites in the sheet (row, column).
            colorkey (Union[pg.Color, int, None], optional): Color to be treated as transparent. Defaults to None.

        Returns:
            List[pg.Surface]: List of sprite images.
        """
        return [self.get_sprite(loc, colorkey) for loc in locs]

def load_image(name, colorkey=None, scale=1):
    fullname = os.path.join(data_dir, name)
    image = pg.image.load(fullname)
    image = image.convert()
    size = image.get_size()
    size = (size[0] * scale, size[1] * scale)
    image = pg.transform.scale(image, size)

    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, pg.RLEACCEL)
    return image, image.get_rect()    

def Read_location_to_file():
                Temp_data_list = []
                file_path = rf"C:\Users\narwh\Documents\Pythonshit\Hotspots\Support Files\Location"
                with open(file_path, "r") as f:
                    lol = f.readlines()
                    Temp_data_list.append(lol)
                    print(Temp_data_list)
                    f.close()   

def npc_process(queue):
    npc_data = NPC_DATA_FILES(queue)
    npc_data.Store_coordinates()

def load_image_sequence(directory):
    """Load all image files from the specified directory."""
    image_files = [f for f in os.listdir(directory)]
    image_files.sort()  # Sort the files to ensure a consistent order
    return image_files


class generate_dots():
    def __init__(self):
        self.coordinate_list = []
        self.coordinates = (0,0)
        self.npc_lists = {}
        self.previous_list_x = 0
        self.previous_list_y = 0

    # Function to read coordinates from a file
    def read_coordinates_from_file(self, file_path):
        with open(file_path, 'r') as f:
            lines = f.readlines()
            #new_list = []
            #new_list.append(lines)
            try:
                final_list = [eval(item) for item in lines]
            except:
                final_list = []
            #print(final_list)
            

        return final_list


    def read_files(self):
        file_list = sorted(os.listdir(folder_path))
        for file_name in file_list:
                npc_name = file_name.split('.')[0]
                file_path = os.path.join(folder_path, file_name)
                # Create a new list dynamically in the dictionary
                self.npc_lists[f'{npc_name}'] = self.read_coordinates_from_file(file_path)
        return(self.npc_lists)

    def existing_file_coordinates(self):
        def read_file(key):
            file_path = os.path.join(folder_path, key)
            return key, self.read_coordinates_from_file(file_path)
        
        with ThreadPoolExecutor() as executor:
            # This will run `read_file` concurrently for each NPC
            results = executor.map(read_file, circles.npc_lists.keys())
        
        # Store the results in npc_lists dictionary
        for key, coordinates in results:
            self.npc_lists[key] = coordinates

        return self.npc_lists

    #def existing_file_coordinates(self):
        #for key in circles.npc_lists.keys():
            # file_path = os.path.join(folder_path, key)
           #  self.npc_lists[f'{key}'] = self.read_coordinates_from_file(file_path)
       # return(self.npc_lists)
    

    def get_circle_coordinates(self,key):
        #for key in self.npc_lists.keys():
            my_list = self.npc_lists[key]
            if my_list == []:
                #print(my_list)
                x = self.previous_list_x
                y = self.previous_list_y
            else:
                x = my_list[0][0]
                y = my_list[0][1]
                self.previous_list_x = x
                self.previous_list_y = y
            return(x,y)
    



circles = generate_dots()
circles.read_files()

#Read_location_to_file()                 
def main():
    """this function is called when the program starts.
    it initializes everything it needs, then ns in
    a loop until the function returns."""
    # Initialize Everything
    pg.init()

    #background_dir = r"C:\Users\narwh\Documents\Pythonshit\Hotspots\Support Files\Frames"
    #image_files = load_image_sequence(background_dir)

    #queue = mp.Queue()
    #npc_process_instance = mp.Process(target=npc_process, args=(queue,))
    #npc_process_instance.start()
    #screen = pg.display.set_mode((screen_width, screen_height))
    screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
    # Load the background image
    #current_image_index = 0
    #background_image = pg.image.load(os.path.join(background_dir, image_files[0])).convert()
    #background_width, background_height = (2160,1620)
    background_image = pg.image.load(rf"C:\Users\narwh\Documents\Pythonshit\Hotspots\Support Files\IMG_0582.png").convert()
    background_width, background_height = background_image.get_size()
    #print(background_image.get_size())
    pg.display.set_caption("My RPG")
    pg.mouse.set_visible(True)
    previous_list_x = 0
    previous_list_y = 0
    # Create The Background
    background = pg.Surface(background_image.get_size())
    background = background.convert()
    #previous_coord = (0,0)

    # Prepare Game Objects
    #whiff_sound = load_sound("whiff.wav")
    #punch_sound = load_sound("punch.wav")
    
    spritesheet = Spritesheet(r"C:\Users\narwh\Documents\Pythonshit\Hotspots\Support Files\MySprite.png",(75, 150))

    sprite_1 = spritesheet.get_sprite((0, 0)) # Gets sprite in location of (1, 1) from top left corner
    sprite_2 = spritesheet.get_sprite((5, 3)) # Gets sprite in location of (5, 3) considering that the starting number is (0, 0)
    player1 = player.player()
    playersprite = pg.sprite.RenderPlain(player1)  # Separate sprite group for player
    clock = pg.time.Clock()
    draw_markers = Mark_Time.choose_points()
    # Initialize the additional updateable layer
    updateable_layer = pg.Surface((background_width, background_height), pg.SRCALPHA)
    font = pg.font.SysFont('Arial', 30)
    small_image = pg.image.load(r"C:\Users\narwh\Documents\Pythonshit\Hotspots\Support Files\PersonDot4.png").convert_alpha()
    small_image2 = pg.image.load(r"C:\Users\narwh\Documents\Pythonshit\Hotspots\Support Files\PersonDot2.png").convert_alpha()
    small_image3 = pg.image.load(r"C:\Users\narwh\Documents\Pythonshit\Hotspots\Support Files\PersonDot3.png").convert_alpha()
    scaled_image_1 = pg.transform.scale(small_image, (16, 16))
    scaled_image_2 = pg.transform.scale(small_image2, (16, 16))
    scaled_image_3 = pg.transform.scale(small_image3, (16, 16))
    sprite_11 = pg.transform.scale(sprite_1, (25, 25))

    # Main Loop
    going = True
    while going:
        circles.existing_file_coordinates()
        clock.tick(240)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                going = False
            elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                going = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_h:
                    # Print pixel coordinates relative to the background image
                    print(f"Pixel Coordinates on Background: {player.player1_position_x}, {player.player1_position_y}")
                    current_coords = (player.player1_position_x,player.player1_position_y)
                    # Draw a dot at the marked location
                    pg.draw.circle(background_image, (255, 0, 0), current_coords, 5)  # Red dot with radius 5
            # Cycle through images
        #background_image = pg.image.load(os.path.join(background_dir, image_files[1])).convert()
            
        playersprite.update()
        # Zoom factor: smaller values mean a "zoomed-in" effect
        #zoom_factor = 2  # 2 means half the original size (zoomed in)

        # Set the new screen width and height based on the zoom factor
        #zoomed_screen_width = screen_width // zoom_factor
        #zoomed_screen_height = screen_height // zoom_factor

        # Now create the viewport using the new zoomed dimensions
        #viewport_x = max(0, min(player1.rect.centerx - zoomed_screen_width // 2, background_image.get_width()))
        #viewport_y = max(0, min(player1.rect.centery - zoomed_screen_height // 2, background_image.get_height()))
        viewport_x = max(0, min(player1.rect.centerx - screen_width // 1000, background_image.get_width()))
        viewport_y = max(0, min(player1.rect.centery - screen_height // 2000, background_image.get_height()))
        #print(viewport_x,viewport_y)
        #viewport = pg.Rect(viewport_x, viewport_y, zoomed_screen_width, zoomed_screen_height)
        viewport = pg.Rect(viewport_x, viewport_y, screen_width, screen_height)
        # Clear the updateable layer
        updateable_layer.fill((0, 0, 0, 0))  # Transparent fill
       
        # Get the current FPS
        fps = clock.get_fps()

        # Create a text surface with the FPS value
        fps_text = font.render(f"FPS: {fps:.2f}", True, (0, 0, 0))

        



        # Draw Everything
        for key in circles.npc_lists.keys():
            my_list = circles.npc_lists[key]
            if my_list == []:
                #print(my_list)
                x = previous_list_x
                y = previous_list_y
            else:
                x = my_list[0][0]
                y = my_list[0][1]
                previous_list_x = x
                previous_list_y = y
        #for key in circles.npc_lists.keys():
            #x,y = circles.get_circle_coordinates(key)
        #if (viewport_x <= x <= viewport_x + screen_width) and (viewport_y <= y <= viewport_y + screen_height):
            if x > 10000 and x < 20000:
                x -= 10000
                updateable_layer.blit(scaled_image_2, (x, y))
                #pg.draw.circle(updateable_layer, (0, 255, 0), (x, y), 8)  # Draw red dots
            elif x > 20000:
                x -= 20000
                updateable_layer.blit(sprite_11, (x, y))
                #pg.draw.circle(updateable_layer, (0, 0, 255), (x, y), 8)  # Draw red dots
            else:
                updateable_layer.blit(scaled_image_3, (x, y))
                #pg.draw.circle(updateable_layer, (255, 0, 0), (x, y), 8)  # Draw red dots
        #draw_markers.Draw_Points(updateable_layer)
        screen.blit(background_image, (0,0), viewport)
        #Draw_Points(self, screen)
        playersprite.draw(screen)
        # Draw the text on the screen (position it at the top-left corner)
        screen.blit(fps_text, (10, 10))
        screen.blit(updateable_layer, (0,0), viewport)
        #circles.existing_file_coordinates()
        pg.display.flip()

        

    #npc_process_instance.terminate()
    pg.quit()

# Game Over
# this calls the 'main' function when this script is executed
if __name__ == "__main__":
    main()



