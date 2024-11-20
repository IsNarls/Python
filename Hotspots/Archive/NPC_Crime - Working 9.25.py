#start of game
# Import Modules
import os
import pygame as pg
import random
import time
import Main_init

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
        self.image, self.rect = Main_init.load_image(r"C:\Users\narwh\OneDrive\Documents\Pythonshit\Hotspots\Support Files\PersonDot.png", -1, 1)
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
        self.sprite_pos = pg.Vector2(Main_init.all_waypoints[0])
        self.reverse_counter = 0
        
        
        
    # Waypoint index
 

    def _walk(self):
        if not self.interacting:
        # Calculate the direction to the current waypoint
            if self.reverse_counter == 0:
                if self.current_waypoint_index < len(Main_init.all_waypoints):
                    #print(len(all_waypoints))
                    target = pg.Vector2(Main_init.all_waypoints[self.current_waypoint_index])
                    #print(target)
                    direction = target - self.sprite_pos
                    # Move the sprite towards the waypoint
                    if direction.length() > self.speed:
                        #print(self.current_waypoint_index)
                        direction.normalize_ip()  # Normalize the direction vector
                        self.sprite_pos += direction * self.speed
                    else:
                        # Reached the waypoint, move to the next one
                        self.current_waypoint_index += 1
                else:
                    self.reverse_counter = 1
            else:
                if self.current_waypoint_index > 0:
                    target = pg.Vector2(Main_init.all_waypoints[self.current_waypoint_index-1])
                    print(target)
                    direction = target - self.sprite_pos
                    if direction.length() > self.speed:
                        #print(self.current_waypoint_index)
                        direction.normalize_ip()  # Normalize the direction vector
                        self.sprite_pos += direction * self.speed
                    else:
                        # Reached the waypoint, move to the next one
                        self.current_waypoint_index = self.current_waypoint_index - 1
                #print(self.rect.center)
                else:
                    self.reverse_counter = 0
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
                
      