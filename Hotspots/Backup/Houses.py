#start of game
# Import Modules
import os
import pygame as pg
import random
import time
import Main_init



class Houses:
    def __init__(self):
        self.red = (255, 0, 0)
        self.blue = (0,0,255)
        self.houses = [
            pg.Rect(0, 0, 0, 0),
            pg.Rect(300, 1140, 30, 30),
            pg.Rect(486, 935, 30, 30),
            pg.Rect(680, 743, 30, 30),
            pg.Rect(1042, 730, 30, 30),
            pg.Rect(678, 1148, 30, 30),
            pg.Rect(850, 500, 30, 30)
        ]

        self.waypointss = [
            pg.Rect(0, 0, 0, 0),
            pg.Rect(255, 1300, 30, 30),
            pg.Rect(395, 1165, 30, 30),
            pg.Rect(585, 975, 30, 30),
            pg.Rect(760, 765, 30, 30),
            pg.Rect(935, 565, 30, 30)
        ]
        
    def draw_squares(self, screen):
        for house in self.houses:
            pg.draw.rect(screen, self.red, house)
        for waypoint in self.waypointss:
            pg.draw.rect(screen, self.blue, waypoint)


    def add_house(self, x, y, width=30, height=30):
        self.houses.append(pg.Rect(x, y, width, height))
   


    def draw_random_squares(self, screen):
        x = 1000 #random.randint(0,1280)
        y = 300 #random.randint(0,900)
        Random_square_1 = pg.Rect(x, y, 30, 30)
        pg.draw.rect(screen, Main_init.load_image.red, Random_square_1)  # Draw the moved square