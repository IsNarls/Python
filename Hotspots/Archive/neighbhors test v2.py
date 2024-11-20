import os 

NPC_NAME = '416735'
self.all_neighbhor_list = []
self.true_neighbhor_list = []
self.npc_neighbors_dict = {}  # Dictionary to store NPC locations and their corresponding neighbors

def read_files(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    return [line.strip() for line in lines]  # Strip newlines and any extra whitespace

def Look_around():
    folder_path = rf"C:\Users\narwh\Documents\Pythonshit\Hotspots\Support Files\self.NPC_Location"
    file_list = sorted(os.listdir(folder_path))
    
    self.NPC_location = None  # We'll store the NPC location here
    for file_name in file_list:
        npc_name = file_name.split('.')[0]
        
        # If it's the target NPC, get their location and store it
        if int(npc_name) == int(NPC_NAME):
            file_path = os.path.join(folder_path, file_name)
            self.NPC_location = read_files(file_path)  # Get the location for NPC_NAME
            #print(f"NPC Location ({NPC_NAME}): {self.NPC_location}")  # Debugging line
        else:
            file_path = os.path.join(folder_path, file_name)
            lines = read_files(file_path)
            new_str = lines + [file_name]  # Add the file name to the location list
            self.all_neighbhor_list.append(new_str)  # Store all neighbor locations and names
    
    # Debugging: Check what's in self.all_neighbhor_list
    #print(f"All Neighbor Locations (with file names): {self.all_neighbhor_list}")
    
    # Compare NPC's location with each neighbor's location
    for location in self.all_neighbhor_list:
        # If the location matches the NPC's location, add the file name to the dictionary
        if location[:-1] == self.NPC_location:  # Exclude the file_name for comparison
            file_name = location[-1]  # Get the last item (file name)
            # Use the first element in the location as the key (the actual location)
            if self.NPC_location[0] not in self.npc_neighbors_dict:  # Ensure the location is used as the key
                self.npc_neighbors_dict[self.NPC_location[0]] = []  # Initialize with an empty list
            self.npc_neighbors_dict[self.NPC_location[0]].append(file_name)  # Add the file name to the location's list of neighbors
    
    # Print the dictionary of neighbors for the NPC
    print(f"NPC Neighbors Dictionary: {self.npc_neighbors_dict}")

# Run the function
Look_around()
