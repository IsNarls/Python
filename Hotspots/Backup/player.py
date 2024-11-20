#start of game
# Import Modules
import os
import pygame as pg
import random
import time
import Main_init

class player(pg.sprite.Sprite):
    """moves a sprite on the screen, following the keyboard WASD"""

    def __init__(self):
        pg.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.image, self.rect = Main_init.load_image(r"C:\Users\narwh\OneDrive\Documents\Pythonshit\Hotspots\Support Files\chimp.png", -1)
        # Set initial position for the player
        self.rect.center = (0, 0)
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
        

    # Boundary checking
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > Main_init.screen_width-2:
            self.rect.right = Main_init.screen_width-2
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom  > Main_init.screen_height-2:
            self.rect.bottom = Main_init.screen_height-2
            #print(self.rect.bottom)

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

