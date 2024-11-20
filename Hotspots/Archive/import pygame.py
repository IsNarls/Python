import pygame
import os

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((1280, 900))  # Adjust the size as needed
clock = pygame.time.Clock()

# Folder containing your files
folder_path = r"C:\Users\narwh\Documents\Pythonshit\Hotspots\Support Files\NPC_Data"  # Update this path

# Function to read coordinates from a file
def read_coordinates_from_file(file_path):
    #coordinates = []
    with open(file_path, 'r') as f:
        lines = f.readlines()
        #print(lines)
        for line in lines:
            test = line.partition(')')
            test2 = test[0].partition("(")
            test3 = test2[2].partition(',')
            x , y = (int(test3[0]), int(test3[2]))
            #print(x,y)
            coordinates = (x,y)
            # Remove unwanted characters and split by comma
            #line = line.strip()#.partition(',')
            #print(line) # Remove parentheses if present
            #if line:  # Check if the line is not empty
                #try:
                    #print(line[1])
                    #x, y = map(int,line)#map(int, line.split(','))  # Split by comma and convert to integers
        #coordinates.append(lines)
                #except ValueError:
                    #print(f"Invalid line skipped: {line}")  # Handle parsing errors
    return coordinates

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((0, 0, 0))  # Fill with black before drawing

    # Iterate over files in the directory
    for file_name in sorted(os.listdir(folder_path)):
        #if file_name.endswith('.txt'):  # Assuming your files are text files
            file_path = os.path.join(folder_path, file_name)
            #print(f"Reading from file: {file_path}")  # Debugging line
            coordinates = read_coordinates_from_file(file_path)
            x, y = coordinates
            #print(x, y)
            # Draw the dots for each coordinate in the file
            #for x, y in coordinates:
            pygame.draw.circle(screen, (255, 0, 0), (x, y), 10)  # Draw red dots

    # Update the display
    pygame.display.flip()
    clock.tick(60)  # Limit to 60 FPS

pygame.quit()
