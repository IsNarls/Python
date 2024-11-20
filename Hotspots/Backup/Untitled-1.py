
from pathlib import Path
import ast 




def Read_location_to_file():
                Temp_data_list = []
                file_path = rf"C:\Users\narwh\Documents\Pythonshit\Hotspots\Support Files\Location"
                with open(file_path, "r") as f:
                    lol = f.readlines()
                    Temp_data_list.append(lol)
                    print(Temp_data_list)
                    f.close()   

Read_location_to_file()