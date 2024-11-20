import pygame
import os

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((1400, 900))  # Adjust the size as needed
clock = pygame.time.Clock()

# Folder containing your files
folder_path = r"C:\Users\narwh\Documents\Pythonshit\Hotspots\Support Files\NPC_Data"  # Update this path
class generate_dots():
    def __init__(self):
        self.coordinate_list = []
        self.coordinates = (0,0)
        self.npc_lists = {}

    # Function to read coordinates from a file
    def read_coordinates_from_file(self, file_path):
        with open(file_path, 'r') as f:
            lines = f.readlines()
            #new_list = []
            #new_list.append(lines)
            final_list = [eval(item) for item in lines]
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
        for key in circles.npc_lists.keys():
             file_path = os.path.join(folder_path, key)
             self.npc_lists[f'{key}'] = self.read_coordinates_from_file(file_path)
        return(self.npc_lists)


circles = generate_dots()
circles.read_files()
index = 0 
delay_counter = 0
previous_list_x = 0
previous_list_y = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # Clear the screen
    #screen.fill((0, 0, 0))  # Fill with black before drawing
    #if delay_counter == 5:
    screen.fill((0, 0, 0))
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
        
            pygame.draw.circle(screen, (255, 0, 0), (x, y), 10)  # Draw red dots
    circles.existing_file_coordinates()
            #index = 0
     #   delay_counter = 0
   # else:
       # delay_counter += 1
            
            #try:
                #circles.read_files()
            #except:
                #pass
           # index = 0
        

    # Update the display
    pygame.display.flip()
    clock.tick(120)  # Limit to 60 FPS

pygame.quit()
