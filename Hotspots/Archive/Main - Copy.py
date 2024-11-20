#start of game
# Import Modules
import os
import pygame as pg
import random
import time
First_count = 0 
Previous_y = 0
Player_counter = 0 
player1_position_x = 1
player1_position_y = 1
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
waypoints =  [(255.0, 1300.0), (395.0, 1165.0), (585.0, 975.0), (760.0, 765.0), (935.0, 565.0), (1155.0, 360.0), (1335.0, 180.0), (1465.0, 50.0), (1635.0, 90.0), (1795.0, 230.0), (1975.0, 350.0)]
all_waypoints = House_waypoints + waypoints
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

class player(pg.sprite.Sprite):
    """moves a sprite on the screen, following the keyboard WASD"""

    def __init__(self):
        pg.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.image, self.rect = load_image(r"C:\Users\narwh\OneDrive\Documents\Pythonshit\Hotspots\Support Files\chimp.png", -1)
        #self.fist_offset = (-235, -80)
        # Set initial position for the player
        self.rect.center = (0, 0)
        self.punching = False 
        self.speed = 5  # Speed of movement
        

    def update(self):

        keys = pg.key.get_pressed()
        
        # Store the current position before potential updates
        old_x, old_y = self.rect.x, self.rect.y


        """move the fist based on the keyboard input"""
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.rect.y -= self.speed
        if keys[pg.K_s]:
            self.rect.y += self.speed
        if keys[pg.K_a]:
            self.rect.x -= self.speed
        if keys[pg.K_d]:
            self.rect.x += self.speed
        if self.punching:
            self.rect.move_ip(15, 25)

    # Boundary checking
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > screen_width:
            self.rect.right = screen_width
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom  > screen_height:
            self.rect.bottom = screen_height
            print(self.rect.bottom)

        # Check if the player has actually moved
        if old_x != self.rect.x or old_y != self.rect.y:
            self.update_position()  # Optional: Update position variables if needed



    def update_position(self):
        """Update any position variables you're tracking externally"""
        global player1_position_x
        global player1_position_y
        player1_position_x = self.rect.x
        player1_position_y = self.rect.y
        # Print the current coordinates
        #print(f"Player coordinates: ({self.rect.x}, {self.rect.y})")

    def Collide(self):
        """prints success if the players hitbox equal the NPC hitbox"""
        global player1_position_x
        global player1_position_y
        global NPC1_position_x
        global NPC1_position_y
        if player1_position_x <= NPC1_position_x and player1_position_y <= NPC1_position_y :
           #print("success")
           pass

class Houses:
    

    def __init__(self):
        self.red = (255, 0, 0)
        self.houses = [
            pg.Rect(0, 0, 0, 0),
            pg.Rect(300, 1140, 30, 30),
            pg.Rect(486, 935, 30, 30),
            pg.Rect(680, 743, 30, 30),
            pg.Rect(1042, 730, 30, 30),
            pg.Rect(678, 1148, 30, 30)
        ]
        

    def draw_squares(self, screen):
        for house in self.houses:
            pg.draw.rect(screen, self.red, house)


    def add_house(self, x, y, width=30, height=30):
        self.houses.append(pg.Rect(x, y, width, height))
   


    def draw_random_squares(self, screen):
        x = 1000 #random.randint(0,1280)
        y = 300 #random.randint(0,900)
        Random_square_1 = pg.Rect(x, y, 30, 30)
        pg.draw.rect(screen, red, Random_square_1)  # Draw the moved square

class NPC_Crime(pg.sprite.Sprite):
    """generate and NPC on screen and print its position"""

    def __init__(self, houses):
        self.Old_House_location_update = houses.houses[0]
        self.counter_lock = 0
        self.current_house = houses.houses[0]
        self.NPC_Position_x = None
        self.NPC_Position_y = None
        self.original_location = None
        self.current_house = None
        self.Trigger_var = 0
        self.interacting = False
        self.house_x = houses.houses[0].centerx
        self.house_y = houses.houses[0].centery
        self.counter = 0
        x = random.randint(280, 300)
        y = random.randint(1220, 1240)
        pg.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.image, self.rect = load_image(r"C:\Users\narwh\OneDrive\Documents\Pythonshit\Hotspots\Support Files\PersonDot.png", -1, 1)
        screen = pg.display.get_surface()
        self.area = screen.get_rect()
        #self.rect.topleft = x, y
        self.move_x = 5
        self.move_y = -5
        self.npc_pos = pg.Vector2(280, 1301)
        self.start_point = pg.Vector2(280, 1301)          
        self.end_point = pg.Vector2(1480,79)
        #pg.draw.line(screen, (0, 0, 0), self.start_point, self.end_point, 2)
        self.speed = 2
        self.current_waypoint_index = 0
        self.sprite_color = (255, 0, 0)  # Red color for the sprite
        self.sprite_size = 20
        self.sprite_pos = pg.Vector2(all_waypoints[0])
        
        
        
    # Waypoint index
 
    
    """def _walk(self):
        if not self.interacting:
        # Calculate the direction to the end point
            direction = self.end_point - self.start_point 
            if self.npc_pos.distance_to(self.end_point) > self.speed:
                self.npc_pos += direction.normalize() * self.speed
            else:
                self.npc_pos = self.end_point
            
            # Update the rectangle position based on the new npc_pos
            self.rect.topleft = (self.npc_pos.x, self.npc_pos.y)
            print(self.rect.topleft)
            # Optional: Check boundaries if necessary
            if self.rect.left < 280 or self.rect.right > 300 or self.rect.top < 1220 or self.rect.bottom > 1240:
                self.move_x = -self.move_x  # Change direction on x-axis
                self.move_y = -self.move_y  # Change direction on y-axis"""


    def _walk(self):
        if not self.interacting:
        # Calculate the direction to the current waypoint
            if self.current_waypoint_index < len(all_waypoints):
                #print(len(all_waypoints))
                target = pg.Vector2(all_waypoints[self.current_waypoint_index])
                direction = target - self.sprite_pos
                # Move the sprite towards the waypoint
                if direction.length() > self.speed:
                    print(self.current_waypoint_index)
                    direction.normalize_ip()  # Normalize the direction vector
                    self.sprite_pos += direction * self.speed
                else:
                    # Reached the waypoint, move to the next one
                    self.current_waypoint_index += 1

                # Update the rectangle's position based on sprite_pos
                self.rect.center = (self.sprite_pos.x, self.sprite_pos.y)
    
    def _walk_to_house(self):
        location = (self.current_house.x, self.current_house.y)
        player = (self.rect.x, self.rect.y)
        #move the red dot across the screen, and turn at the ends
        loc_x , loc_y = location
        play_x, play_y = player
        playerlocation_differential_x = int(loc_x) - int(play_x) 
        playerlocation_differential_y = int(loc_y) - int(play_y)
        #if playerlocation_differential_x != 0 and playerlocation_differential_y != 0:
        if int(playerlocation_differential_x) == 0 and int(playerlocation_differential_y) == 0:
            self.Trigger_var = 2 
            #self.update_position()
        if  playerlocation_differential_x != 0:
            if playerlocation_differential_x < 0:
                newpos = self.rect.move((-1,0))
            if playerlocation_differential_x > 0:
                newpos = self.rect.move((1,0))
            self.rect = newpos
        if  playerlocation_differential_y != 0:
            if playerlocation_differential_y < 0:
                newpos = self.rect.move((0,-1))
            if playerlocation_differential_y > 0:
                newpos = self.rect.move((0,1))
            self.rect = newpos
        #print(playerlocation_differential_x,playerlocation_differential_y)


    def _walk_back(self):
        current_position = (self.rect.x, self.rect.y)
        old_position = (self.NPC_Position_x, self.NPC_Position_y)
        loc_x , loc_y = old_position
        play_x, play_y = current_position
        playerlocation_differential_x = int(loc_x) - int(play_x) 
        playerlocation_differential_y = int(loc_y) - int(play_y)
        if int(playerlocation_differential_x) == 0 and int(playerlocation_differential_y) == 0:
            self.interacting = False
            self.Trigger_var = 0
            #self.update_position()
        if  playerlocation_differential_x != 0:
            if playerlocation_differential_x < 0:
                newpos = self.rect.move((-1,0))
            if playerlocation_differential_x > 0:
                newpos = self.rect.move((1,0))
            self.rect = newpos
        if  playerlocation_differential_y != 0:
            if playerlocation_differential_y < 0:
                newpos = self.rect.move((0,-1))
            if playerlocation_differential_y > 0:
                newpos = self.rect.move((0,1))
            self.rect = newpos
      

    def interact_with_building(self, houses):
        for house in houses.houses:
            if house.top <= self.rect.centery-10 <= house.bottom: # Y axis 
                #print("Self", self.rect)
                #self.current_house = house.x
            #if house.left <= self.rect.centerx <= house.right: # X Axis
                if int(house.x) != int(self.Old_House_location_update.x):
                    print(house.x, self.Old_House_location_update.x )
                    self.Trigger_var = 1 
                    self.current_house = house
                    print(house)
                    if self.counter_lock == 0:
                        self.update_house_position()
                        self.update_position()
                        self.counter_lock = 1
                        #print("NEAR A HOUSE")
                        #print(house.x)
                    #time.sleep(.1)
                else:
                    #print(house.x, self.Old_House_location_update.x)
                    pass
        

    def update_position(self):
        """Update any position variables you're tracking externally"""
        self.NPC_Position_x = self.rect.x 
        self.NPC_Position_y = self.rect.y
        
    def update_house_position(self):
        self.Old_House_location_update = self.current_house
        print(self.Old_House_location_update)
    
       
        
    def update(self,houses):
        if self.counter == 1:
            if self.Trigger_var == 1:
                self.interacting = True
                self._walk_to_house()
            elif self.Trigger_var == 2:
                self.interacting = True
                self._walk_back()
            else:
                self.interacting = False
                self._walk()
                #self.interact_with_building(houses)
                #print(self.Trigger_var)
            self.counter = 0
        else:
            self.counter = self.counter + 1
                
          
def main():
    
    """this function is called when the program starts.
    it initializes everything it needs, then ns in
    a loop until the function returns."""
    # Initialize Everything
    pg.init()
    
    screen_width, screen_height = 1280, 900
    screen = pg.display.set_mode((screen_width, screen_height))

    # Load the background image
    background_image = pg.image.load(r"C:\Users\narwh\OneDrive\Documents\Pythonshit\Hotspots\Support Files\Background.png").convert()
    background_width, background_height = background_image.get_size()
    print(background_image.get_size())
    pg.display.set_caption("My RPG")
    pg.mouse.set_visible(True)
    

    # Create The Background
    background = pg.Surface(screen.get_size())
    background = background.convert()

    # Prepare Game Objects
    #whiff_sound = load_sound("whiff.wav")
    #punch_sound = load_sound("punch.wav")
    
    player1 = player()
    playersprite = pg.sprite.RenderPlain(player1)  # Separate sprite group for player
    clock = pg.time.Clock()
    houses = Houses()
    person = NPC_Crime(houses)
    allpersons = pg.sprite.RenderPlain(person)
    
    #person = Person(background_image)
    # Initialize the additional updateable layer
    updateable_layer = pg.Surface((background_width, background_height), pg.SRCALPHA)
    #updateable_layer = pg.Surface(screen.get_size(), pg.SRCALPHA)  # Use SRCALPHA for transparency





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
                 print(f"Player coordinates: ({player1_position_x}, {player1_position_y})")
       





        #person.interact_with_building(houses)    
        playersprite.update()
        allpersons.update(houses)
    
         # Adjust the viewport to follow the player
        viewport = pg.Rect(player1.rect.x, player1.rect.y, screen_width, screen_height)

        # Clear the updateable layer
        updateable_layer.fill((0, 0, 0, 0))  # Transparent fill


        # Draw Everything
        screen.blit(background_image, (0, 0), viewport)
        allpersons.draw(updateable_layer)
        playersprite.draw(screen)
        houses.draw_squares(background_image)
        # Draw/update things on the updateable layer
        screen.blit(updateable_layer, (0, 0), viewport) # Draw the updateable layer on top
        #time.sleep(.5)
        pg.display.flip()

    pg.quit()


# Game Over
# this calls the 'main' function when this script is executed
if __name__ == "__main__":
    main()


