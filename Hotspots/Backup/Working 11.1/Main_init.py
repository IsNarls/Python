#start of game
# Import Modules
import os
import pygame as pg
import random
import time
import player
import Houses
from multiprocessing import Process, Queue, Lock
from pathlib import Path
import ast 


file_lock = Lock()
First_count = 0 
Previous_y = 0
Player_counter = 0 
counter = 0

#unsure what this does figure out later 
if not pg.font:
    print("Warning, fonts disabled")
if not pg.mixer:
    print("Warning, sound disabled")

screen_width, screen_height = 1280, 900

red = (255, 0 ,0)
blue = (0,0,255)
start_counter = 0
main_dir = r"C:\Users\narwh\OneDrive\Documents\Pythonshit\Hotspots"
data_dir = r"C:\Users\narwh\OneDrive\Documents\Pythonshit\Hotspots\Support Files"

Waypoints = {
    'W1': (255.0, 1300.0),
    'W2': (395.0, 1165.0),
    'W3': (585.0, 975.0),
    'W4': (760.0, 765.0),
    'W5': (935.0, 565.0),
    'W6': (1155.0, 360.0),
    'W7': (1335.0, 180.0),
    'W8': (1465.0, 50.0),
    'W9': (1635.0, 90.0),
    'W10': (1795.0, 230.0),
    'W11': (1975.0, 350.0),
    'H1': (295.0, 1140.0),
    'H2': (490.0, 930.0),
    'H3': (675.0, 715.0),
    'H4': (850.0, 500.0),
    'H5': (1045.0, 315.0),
    'H6': (1235.0, 120.0),
    'H7': (1380.0, 30.0),
    'H8': (1690.0, 60.0),
    'H9': (1805.0, 145.0),
}

neighbors = {
    'W1': ['W2', 'W6'],      # W1 is near W2 and W6
    'W2': ['W1', 'W3', 'W6', 'H1'],  # W2 is near W1, W3, and W6
    'W3': ['W2', 'W4', 'W6', 'H2'],  # W3 is near W2, W4, and W6
    'W4': ['W3', 'W5', 'W6', 'H3'],  # W4 is near W3, W5, and W6
    'W5': ['W4', 'W6', 'W7', 'H4'],  # W5 is near W4, W6, and W7
    'W6': ['W1', 'W2', 'W3', 'W4', 'W5', 'W7', 'H5'],  # W6 connects many points
    'W7': ['W5', 'W6', 'W8', 'H6'],  # W7 is near W5, W6, and W8
    'W8': ['W7', 'W9', 'H7'],      # W8 is near W7 and W9
    'W9': ['W8', 'W10', 'H8'],     # W9 is near W8 and W10
    'W10': ['W9', 'W11', 'H9'],    # W10 is near W9 and W11
    'W11': ['W10'],          # W11 is near W10
    'H1': ['W2'],
    'H2': ['W3'],
    'H3': ['W4'],
    'H4': ['W5'],
    'H5': ['W6'],
    'H6': ['W7'],
    'H7': ['W8'],
    'H8': ['W9'],
    'H9': ['W10'],
}

HouseWaypoints = {
    'H1': (295.0, 1140.0),
    'H2': (490.0, 930.0),
    'H3': (675.0, 715.0),
    'H4': (850.0, 500.0),
    'H5': (1045.0, 315.0),
    'H6': (1235.0, 120.0),
    'H7': (1380.0, 30.0),
    'H8': (1690.0, 60.0),
    'H9': (1805.0, 145.0),
}

NPC_Houses = [
    'H3',
    'H4',
    'H5',
    'H6',
    'H7',
    'H8',
    'H9',
]

house_waypoints = [] 
waaypoints = []
points = Waypoints 
previous_house = None
Game_clock = 0
Minute_timer = 0
Hour_timer = 8
Day_timer = 1 
Calender_counter = 0
Year_counter = 1

# functions to create our resources

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

def pick_house():
        # Pick a random house
        global NPC_Houses
        global previous_house
        selected_house = random.choice(NPC_Houses)
        print(selected_house)
        #Remove the selected house from the dictionary
        return selected_house


def Draw_Points(screen):
        # Draw points
    for point, pos in points.items():
        pg.draw.circle(screen, (0, 0, 0), pos, 5)
        font = pg.font.Font(None, 24)
        text = font.render(point, True, (0, 0, 0))
        screen.blit(text, (pos[0] + 10, pos[1] - 10))
                
def Mark_time():
            global Game_clock
            global Minute_timer
            global Hour_timer
            global Day_timer
            global Calender_counter 
            Game_clock += 1
            # 1 minute = 27 ticks, total ticks = 38880 (1440 minutes in 1 day)
            # start time is 8am, 480 minutes have passed 960 minutes to go.
            if Game_clock == 27:
                #print(Minute_timer)
                Game_clock = 0
                Minute_timer += 1
            if Minute_timer == 60:
                Minute_timer = 0 
                Hour_timer += 1
            if Hour_timer == 24:
                Day_timer += 1
                Hour_timer = 0
            if Day_timer == 7:
                Day_timer = 0
                Calender_counter += 7
            if Calender_counter == 365:
                Calender_counter = 0 
                Year_counter += 1
            time_of_day = ('Hour:', Hour_timer, 'minute:', Minute_timer,'Day:', Day_timer,'Calender:',Calender_counter)
            Write_time_to_file(str(time_of_day))

def Write_time_to_file(Time):
    with file_lock: 
        file_path = rf"C:\Users\narwh\OneDrive\Documents\Pythonshit\Hotspots\Support Files\TIME"
        with open(file_path, "w+") as f:
            f.write(Time) 
            f.close()
                    
def Get_time():
        file_path = rf"C:\Users\narwh\OneDrive\Documents\Pythonshit\Hotspots\Support Files\TIME"
        with open(file_path, "r") as f:
            TIME = f.readlines()# 0 is Current order not open 1 is current buy order open 2 is current sell order open
            str_conversion = TIME
            data_tuple = eval(TIME[0])

            # Partition the tuple into variables
            hour_label, hour, minute_label, minute, day_label, day, calendar_label, calendar = data_tuple

            # Output the results
            #print(f"Hour: {hour}, Minute: {minute}, Day: {day}, Calendar: {calendar}") 
            #print(TIME)   
            return(day,minute,hour,calendar)       
    
def main():
    
    """this function is called when the program starts.
    it initializes everything it needs, then ns in
    a loop until the function returns."""
    # Initialize Everything
    pg.init()
    
    screen = pg.display.set_mode((screen_width, screen_height))
    # Scrolling variables
    scroll_x = 0
    scroll_y = 0 
    # Load the background image
    background_image = pg.image.load(r"C:\Users\narwh\OneDrive\Documents\Pythonshit\Hotspots\Support Files\Background.png").convert()
    background_width, background_height = background_image.get_size()
    print(background_image.get_size())
    pg.display.set_caption("My RPG")
    pg.mouse.set_visible(True)

    # Create The Background
    background = pg.Surface(background_image.get_size())
    background = background.convert()
    background_rect = background_image.get_rect(center=(screen_width // 2, screen_height // 2))  # Center the background

    # Prepare Game Objects
    #whiff_sound = load_sound("whiff.wav")
    #punch_sound = load_sound("punch.wav")
    num_npcs = 75
    player1 = player.player()
    playersprite = pg.sprite.RenderPlain(player1)  # Separate sprite group for player
    clock = pg.time.Clock()
    houses = Houses.Houses()
    person = NPC_Crime.NPC_Crime()
    person2 = NPC_Crime.NPC_Crime()

    allpersons = pg.sprite.RenderPlain(person)
    allpersons2 = pg.sprite.RenderPlain(person2)

    for i in range(num_npcs):
        person = NPC_Crime.NPC_Crime()
        person2 = NPC_Crime.NPC_Crime()
        allpersons.add(person)
        allpersons2.add(person2)
    """for k in range(num_npcs):
        person2 = NPC_Crime.NPC_Crime()
        allpersons2.add(person2)
    for l in range(num_npcs):
        person3 = NPC_Crime.NPC_Crime()
        allpersons3.add(person3)"""



        
    
    # Initialize the additional updateable layer
    updateable_layer = pg.Surface((background_width, background_height), pg.SRCALPHA)
    self = None
    
    # Main Loop
    going = True
    while going:
        clock.tick(120)
        Mark_time()
        #get_time()
    #print(time_of_day)
    #print("The time is:", Day_timer , ":" , Hour_timer , ":" , Minute_timer)
        # Handle Input Events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                going = False
            elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                going = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    #print(f"Player coordinates: ({player.player1_position_x}, {player.player1_position_y})")
                    # Print pixel coordinates relative to the background image
                    #print(f"Pixel Coordinates on Background: {player.player1_position_x}, {player.player1_position_y}")
                    #current_coords = (player.player1_position_x,player.player1_position_y)
                    #waaypoints.append(current_coords)
                    #print("waypoints = ", waaypoints)
                    global Hour_timer
                    Hour_timer += 1
                    #Mark_time()
                if event.key == pg.K_h:
                    # Print pixel coordinates relative to the background image
                    print(f"Pixel Coordinates on Background: {player.player1_position_x}, {player.player1_position_y}")
                    current_coords = (player.player1_position_x,player.player1_position_y)
                    house_waypoints.append(current_coords)
                    print("House_waypoints = ", house_waypoints)

                    # Draw a dot at the marked location
                    pg.draw.circle(background_image, (255, 0, 0), current_coords, 5)  # Red dot with radius 5

         
   
        playersprite.update()
        player1.Draw_Points(background_image)
        viewport_x = max(0, min(player1.rect.centerx - screen_width // 3, background_image.get_width()))
        viewport_y = max(0, min(player1.rect.centery - screen_height // 6.5, background_image.get_height()))
        viewport = pg.Rect(viewport_x, viewport_y, screen_width, screen_height)

        # Clear the updateable layer
        
        updateable_layer.fill((0, 0, 0, 0))  # Transparent fill
        #houses.draw_NPC_locations(updateable_layer)
        #area = pg.Rect(0, 0, 2160, 1620)
        allpersons.update(updateable_layer)
        allpersons2.update(updateable_layer)
        #allpersons1.update(updateable_layer)
        #allpersons2.update(updateable_layer)
        #allpersons3.update(updateable_layer)
        #person.tick(time_of_day)
        
        # Draw Everything
        screen.blit(background_image, (0,0), viewport)
        #allpersons.draw(updateable_layer)
        playersprite.draw(screen)
        houses.draw_squares(background_image)
        # Draw/update things on the updateable layer
        screen.blit(updateable_layer, (0,0), viewport)
        #time.sleep(.5)s
        pg.display.flip()

    pg.quit()

# Game Over
# this calls the 'main' function when this script is executed
if __name__ == "__main__":
    main()


