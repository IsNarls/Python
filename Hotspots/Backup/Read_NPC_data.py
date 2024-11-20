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

    def Write_location_to_file(self,Master_list):
                file_path = rf"C:\Users\narwh\Documents\Pythonshit\Hotspots\Support Files\Location"
                with open(file_path, "a") as f:
                    f.write(str(Master_list)) 
      

    def Store_coordinates(self):
       while True:
        time.sleep(1) 
        while self.counter == 0:
            self.Read_NPC_Data_files()
            self.List1 = coordinates
            self.counter = 1
        while self.counter == 1:
            self.Read_NPC_Data_files()
            self.List2 = coordinates
            self.counter = 2 
        while self.counter == 2:
            self.Read_NPC_Data_files()
            self.List3 = coordinates
            self.counter = 3
        while self.counter == 3:
            self.Read_NPC_Data_files()
            self.List4 = coordinates
            self.counter = 4
        while self.counter == 4:
            self.Read_NPC_Data_files()
            self.List5 = coordinates
            self.counter = 5
        while self.counter == 5:
            self.Read_NPC_Data_files()
            self.List6 = coordinates
            self.counter = 6
        self.Master_list = (self.List1,self.List2,self.List3,self.List4,self.List5,self.List6)
        self.Write_location_to_file(self.Master_list)

Main_class = NPC_DATA_FILES()
print_list = Main_class.Store_coordinates()
print_list

#print(print_list)
