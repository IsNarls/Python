#start of game
# Import Modules
import os
import pygame as pg
import random
import time
import player
import Houses
import NPC_Crime

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

"""
houses_neighbors = {
    'H1': {'neighbors': ['W1']},
    'H2': {'neighbors': ['W2']},
    'H3': {'neighbors': ['W3']},
    'H4': {'neighbors': ['W4']},
    'H5': {'neighbors': ['W5']},
    'H6': {'neighbors': ['W6']},
    'H7': {'neighbors': ['W7']},
    'H8': {'neighbors': ['W8']},
    'H9': {'neighbors': ['W9']},
}"""


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


house_waypoints = [] 
waaypoints = []
points = Waypoints 

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
    
    player1 = player.player()
    playersprite = pg.sprite.RenderPlain(player1)  # Separate sprite group for player
    clock = pg.time.Clock()
    houses = Houses.Houses()
    person = NPC_Crime.NPC_Crime()
    allpersons = pg.sprite.RenderPlain(person)
    
    # Initialize the additional updateable layer
    updateable_layer = pg.Surface((background_width, background_height), pg.SRCALPHA)
    


    # Main Loop
    going = True
    while going:
        clock.tick(120)
       

        # Handle Input Events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                going = False
            elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                going = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    print(f"Player coordinates: ({player.player1_position_x}, {player.player1_position_y})")
                    # Print pixel coordinates relative to the background image
                    print(f"Pixel Coordinates on Background: {player.player1_position_x}, {player.player1_position_y}")
                    current_coords = (player.player1_position_x,player.player1_position_y)
                    waaypoints.append(current_coords)
                    print("waypoints = ", waaypoints)
                if event.key == pg.K_h:
                    # Print pixel coordinates relative to the background image
                    print(f"Pixel Coordinates on Background: {player.player1_position_x}, {player.player1_position_y}")
                    current_coords = (player.player1_position_x,player.player1_position_y)
                    house_waypoints.append(current_coords)
                    print("House_waypoints = ", house_waypoints)

                    # Draw a dot at the marked location
                    pg.draw.circle(background_image, (255, 0, 0), current_coords, 5)  # Red dot with radius 5

         
   
        playersprite.update()
        viewport_x = max(0, min(player1.rect.centerx - screen_width // 3, background_image.get_width()))
        viewport_y = max(0, min(player1.rect.centery - screen_height // 6.5, background_image.get_height()))
        viewport = pg.Rect(viewport_x, viewport_y, screen_width, screen_height)

        # Clear the updateable layer
        updateable_layer.fill((0, 0, 0, 0))  # Transparent fill
        #area = pg.Rect(0, 0, 2160, 1620)

        allpersons.update(updateable_layer)


        # Draw Everything
        screen.blit(background_image, (0,0), viewport)
        allpersons.draw(updateable_layer)
        playersprite.draw(screen)
        houses.draw_squares(background_image)
        # Draw/update things on the updateable layer
        screen.blit(updateable_layer, (0,0), viewport)
        #time.sleep(.5)
        pg.display.flip()

    pg.quit()


# Game Over
# this calls the 'main' function when this script is executed
if __name__ == "__main__":
    main()


