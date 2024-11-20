import os 


NPC_NAME = '416735'
all_neighbhor_list = []
true_neighbhor_list = []

def read_files(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
        #print(lines)
    return lines

def Look_around():
    folder_path = rf"C:\Users\narwh\Documents\Pythonshit\Hotspots\Support Files\NPC_Location"
    file_list = sorted(os.listdir(folder_path))
    for file_name in file_list:
            npc_name = file_name.split('.')[0]
            if int(npc_name) == int(NPC_NAME):
                file_path = os.path.join(folder_path, file_name)
                NPC_location = read_files(file_path)
                #print(NPC_location)
            else:
                #print(npc_name)
                file_path = os.path.join(folder_path, file_name)
                # Create a new list dynamically in the dictionary
                lines = read_files(file_path)
                new_str = lines + file_name
                all_neighbhor_list.append(new_str)
    print(all_neighbhor_list)
    for location in all_neighbhor_list:
        if location == NPC_location:
            true_neighbhor_list.append(file_name)
    print(true_neighbhor_list)
    

Look_around()