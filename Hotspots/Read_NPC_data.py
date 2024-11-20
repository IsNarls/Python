from pathlib import Path
import ast 
import time

class NPC_DATA_FILES():
    
    def __init__(self):
        self.counter=0
        self.Master_list = []


    def Read_NPC_Data_files(self):
            NPC_data_dir = r"C:\Users\narwh\Documents\Pythonshit\Hotspots\Support Files\NPC_DATA"
            data_dir = Path(NPC_data_dir)
            global coordinates
            coordinates = []
            for file in data_dir.iterdir():
                if file.is_file():  # Check if it is a file
                    with open(file, 'r') as temp_npc_data:
                        for line in temp_npc_data:
                            coord = ast.literal_eval(line.strip())
                            x,y = coord
                            coordinates.append(coord)
            return(coordinates)

    def Write_location_to_file(self):
                file_path = rf"C:\Users\narwh\Documents\Pythonshit\Hotspots\Support Files\Location"
                with open(file_path, "a") as f:
                    f.write(str(self.Master_list))

    def Read_NPC_Data_files(self):
            location_data_dir = rf"C:\Users\narwh\Documents\Pythonshit\Hotspots\Support Files\Location"
            for file in location_data_dir.iterdir():
                if file.is_file():  # Check if it is a file
                    with open(file, 'r') as temp_npc_data:
                        for line in temp_npc_data:
                            coord = ast.literal_eval(line.strip())
                            x,y = coord
                            coordinates.append(coord)
            return(coordinates)
      

    def Store_coordinates(self):
       while True:
        self.Read_NPC_Data_files()
        self.List1 = coordinates
        self.Master_list = (self.List1)
        self.Write_location_to_file()

Main_class = NPC_DATA_FILES()
print_list = Main_class.Store_coordinates()
print_list

#print(print_list)
