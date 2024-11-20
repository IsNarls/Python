import pygame as pg
import sys

# Initialize Pygame
pg.init()



waypoints = []
house_waypoints = []

# Screen dimensions
SCREEN_WIDTH = 1280     
SCREEN_HEIGHT = 900

# Create the screen
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption("Sprite Movement Around Background")

# Load the background image
background_image = pg.image.load(r"C:\Users\narwh\Documents\Pythonshit\Hotspots\Support Files\dots.png").convert()

# Get the size of the background image
bg_width, bg_height = background_image.get_size()

# Define the sprite
sprite_color = (255, 0, 0)  # Red color for the sprite
sprite_size = 20
sprite_pos = pg.Vector2(bg_width // 2, bg_height // 2)  # Start in the center of the background

# Speed of the sprite
sprite_speed = 5

def Write_location_to_file_DEATH(location):
                    file_path = rf"C:\Users\narwh\Documents\Pythonshit\Hotspots\Support Files\Coordinate_points"
                    with open(file_path, "w+") as f:
                        f.write(str(location))
                        f.close() 
index = 95
w = None
# Main loop
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
            str_1_to_write = str("waypoints = ", waypoints)
            #print("House_waypoints = ", house_waypoints)
            Write_location_to_file_DEATH(self,str_1_to_write)
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                # Print pixel coordinates relative to the background image
                print(f"Pixel Coordinates on Background: {sprite_pos.x}, {sprite_pos.y}")
                current_coords = (sprite_pos.x,sprite_pos.y)
                waypoint_name = "S" + str(index)
                #waypoints.append("W")
                waypoints.append(str(waypoint_name))
                waypoints.append(current_coords)
                new_waypoint = index
                index += 1
                print("waypoints = ", waypoints)
                Write_location_to_file_DEATH(waypoints)
            if event.key == pg.K_h:
                # Print pixel coordinates relative to the background image
                print(f"Pixel Coordinates on Background: {sprite_pos.x}, {sprite_pos.y}")
                current_coords = (sprite_pos.x,sprite_pos.y)
                house_waypoints.append(current_coords)
                print("House_waypoints = ", house_waypoints)
                
                

    # Get pressed keys
    keys = pg.key.get_pressed()
    if keys[pg.K_a]:
        sprite_pos.x -= sprite_speed
    if keys[pg.K_d]:
        sprite_pos.x += sprite_speed
    if keys[pg.K_w]:
        sprite_pos.y -= sprite_speed
    if keys[pg.K_s]:
        sprite_pos.y += sprite_speed

    # Keep the sprite within the bounds of the background image
    sprite_pos.x = max(sprite_size // 2, min(bg_width - sprite_size // 2, sprite_pos.x))
    sprite_pos.y = max(sprite_size // 2, min(bg_height - sprite_size // 2, sprite_pos.y))

    # Calculate camera offset based on sprite position
    camera_offset_x = sprite_pos.x - SCREEN_WIDTH // 2
    camera_offset_y = sprite_pos.y - SCREEN_HEIGHT // 2

  
    # Clear the screen and draw the background
    screen.blit(background_image, (-camera_offset_x, -camera_offset_y))

    # Draw the sprite at the center of the screen
    pg.draw.rect(screen, sprite_color, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, sprite_size, sprite_size))

    # Update the display
    pg.display.flip()
    pg.time.Clock().tick(60)  # Limit to 60 FPS
