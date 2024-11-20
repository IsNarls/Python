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
House_waypoints =  [(295.0, 1140.0), (490.0, 930.0), (675.0, 715.0), (850.0, 500.0), (1045.0, 315.0), (1235.0, 120.0), (1380.0, 30.0), (1690.0, 60.0), (1805.0, 145.0)]
waypoints =  [(255.0, 1300.0), (395.0, 1165.0), (585.0, 975.0), (760.0, 765.0), (935.0, 565.0)] #(1155.0, 360.0), (1335.0, 180.0), (1465.0, 50.0), (1635.0, 90.0), (1795.0, 230.0), (1975.0, 350.0)]

house_waypoints = []
waaypoints = []

all_waypoints = waypoints 
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
    #pg.image.load

    # Create The Background
    background = pg.Surface(background_image.get_size())
    #background = pg.Surface(screen.get_size())
    background = background.convert()
    #background_rect = background_image.get_rect()
    background_rect = background_image.get_rect(center=(screen_width // 2, screen_height // 2))  # Center the background

    # Prepare Game Objects
    #whiff_sound = load_sound("whiff.wav")
    #punch_sound = load_sound("punch.wav")
    
    player1 = player.player()
    playersprite = pg.sprite.RenderPlain(player1)  # Separate sprite group for player
    clock = pg.time.Clock()
    houses = Houses.Houses()
    person = NPC_Crime.NPC_Crime(houses)
    allpersons = pg.sprite.RenderPlain(person)
    
    #person = Person(background_image)
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

         




        #person.interact_with_building(houses)    
        playersprite.update()
        allpersons.update(houses)
    
         # Adjust the viewport to follow the player
        #viewport_x = max(0, min(player1.rect.x - screen_width // 2, background_width - screen_width))
        #viewport_y = max(0, min(player1.rect.y - screen_height // 2, background_height - screen_height))
        viewport_x = max(0, min(player1.rect.centerx - screen_width // 3, background_image.get_width()))
        viewport_y = max(0, min(player1.rect.centery - screen_height // 6.5, background_image.get_height()))
        #viewport = pg.Rect(player1.rect.x, player1.rect.y, screen_width, screen_height)
        viewport = pg.Rect(viewport_x, viewport_y, screen_width, screen_height)
        #print(viewport)

        #area = pg.Rect(0, 0, 2160, 1620)
        # Clear the updateable layer
        updateable_layer.fill((0, 0, 0, 0))  # Transparent fill
        #area = pg.Rect(0, 0, 2160, 1620)

       


        # Draw Everything
        #screen.blit(background_image, (0,0))
        #screen.blit(updateable_layer, (0,0))
        screen.blit(background_image, (0,0), viewport)
        allpersons.draw(updateable_layer)
        playersprite.draw(screen)
        houses.draw_squares(background_image)
        # Draw/update things on the updateable layer
        #screen.blit(updateable_layer, (0, 0), viewport) # Draw the updateable layer on top
        #background_image.blit(updateable_layer, (0, 0), area) 
        screen.blit(updateable_layer, (0,0), viewport)
        #time.sleep(.5)
        pg.display.flip()

    pg.quit()


# Game Over
# this calls the 'main' function when this script is executed
if __name__ == "__main__":
    main()


