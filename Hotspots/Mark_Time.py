import pygame as pg
import ast  # To safely evaluate the string representation of tuples
from pathlib import Path
import player
from multiprocessing import Lock
import random
import time

main_counter = 0
house_waypoints = [] 
waaypoints = []
previous_house = None
Game_clock = 0
Minute_timer = 0
Hour_timer = 8
Day_timer = 1 
Calender_counter = 0
Year_counter = 1
file_lock = Lock()

class Drawing_NPCS():

    def __init__(self):
        self.data_dir = Path(r"C:\Users\narwh\Documents\Pythonshit\Hotspots\Support Files\NPC_data")
        self.coordinates = []
        pass

    def draw_NPC_locations(self):
        for file in self.data_dir.iterdir():
            if file.is_file():  # Check if it is a file
                with open(file, 'r') as temp_npc_data:
                    for line in temp_npc_data:
                        coord = ast.literal_eval(line.strip())
                        #x,y = coord
                        #pg.draw.circle(screen, (255, 0, 0), (x,y), 20)
                        print(coord)
        
class Waypoints_class():
    def __init__(self):
        self.define_waypoints()
    
    def define_waypoints(self):
        self.Waypoints = {'W1': (3220.0, 2080.0), 'W2': (2935.0, 1910.0), 'W3': (2580.0, 1720.0), 'W4': (2390.0, 1605.0), 'W5': (1710.0, 1220.0), 'W6': (1680.0, 1180.0), 'W7': (1805.0, 1155.0), 'W8': (1845.0, 1195.0), 'W9': (2055.0, 1070.0), 'W10': (2090.0, 1045.0), 'W11': (2205.0, 1110.0), 'W12': (2405.0, 1225.0), 'W13': (2625.0, 1350.0), 'W14': (2730.0, 1420.0), 'W15': (2790.0, 1440.0), 'W16': (2835.0, 1440.0), 'W17': (2885.0, 1410.0), 'W18': (2945.0, 1370.0), 'W19': (2995.0, 1340.0), 'W20': (3035.0, 1365.0), 'W21': (2980.0, 1405.0), 'W22': (2915.0, 1440.0), 'W23': (2845.0, 1475.0), 'W24': (2795.0, 1475.0), 'W25': (2735.0, 1470.0), 'W26': (2560.0, 1375.0), 'W27': (2335.0, 1245.0), 'W28': (2145.0, 1120.0), 'W29': (1915.0, 1095.0), 'W30': (2105.0, 980.0), 'W31': (2215.0, 925.0), 'W32': (2275.0, 880.0), 'W33': (2405.0, 810.0), 'W34': (2590.0, 700.0), 'W35': (2710.0, 625.0), 'W36': (2245.0, 350.0), 'W37': (2030.0, 470.0), 'W38': (2125.0, 535.0), 'W39': (2080.0, 560.0), 'W40': (2170.0, 515.0), 'W41': (2205.0, 595.0), 'W42': (2310.0, 645.0), 'W43': (2310.0, 700.0), 'W44': (2395.0, 650.0), 'W45': (2740.0, 615.0), 'W46': (2800.0, 635.0), 'W47': (2770.0, 640.0), 'W48': (2580.0, 760.0), 'W49': (2490.0, 825.0), 'W50': (2405.0, 865.0), 'W51': (2325.0, 920.0), 'W52': (2425.0, 975.0), 'W53': (2510.0, 1035.0), 'W54': (2590.0, 1075.0), 'W55': (2650.0, 1120.0), 'W56': (2725.0, 1150.0), 'W57': (2825.0, 1210.0), 'W58': (3010.0, 1305.0), 'W59': (3200.0, 1425.0), 'W60': (3225.0, 1255.0), 'W61': (3050.0, 1150.0), 'W62': (2860.0, 1045.0), 'W63': (2795.0, 995.0), 'W64': (2940.0, 910.0), 'W65': (2840.0, 835.0), 'W66': (2950.0, 760.0), 'W67': (2980.0, 795.0), 'W68': (2910.0, 840.0), 'W69': (3035.0, 905.0), 'W70': (3035.0, 905.0), 'W71': (2970.0, 1030.0), 'W72': (3155.0, 1150.0), 'W73': (3225.0, 1205.0), 'W74': (3215.0, 925.0), 'W75': (3215.0, 880.0), 'W76': (3015.0, 760.0), 'W77': (3110.0, 685.0), 'W78': (3220.0, 605.0), 'W79': (3220.0, 575.0), 'W80': (3035.0, 660.0), 'W81': (2985.0, 530.0), 'W82': (3225.0, 385.0), 'W83': (3225.0, 335.0), 'W84': (3105.0, 410.0), 'W85': (2910.0, 520.0)
                          ,'W86': (1610.0, 1045.0), 'W87': (1460.0, 960.0), 'W88': (1335.0, 880.0), 'W89': (1440.0, 815.0), 'W90': (1540.0, 755.0), 'W91': (2155.0, 1735.0), 'W92': (2055.0, 1805.0), 'W93': (2025.0, 1850.0), 'W94': (1960.0, 1810.0), 'W95': (1780.0, 1700.0)
    ,'H1': (1685.0, 1755.0), 'H2': (1905.0, 1875.0), 'H3': (1585.0, 935.0), 'H4': (1510.0, 875.0),
    'H5': (1620.0, 795.0), 'H6': (1725.0, 740.0), 'H7': (1830.0, 780.0), 'H8': (1740.0, 875.0),
    'H9': (2015.0, 610.0), 'H10': (2245.0, 455.0), 'H11': (2470.0, 605.0), 'H12': (2235.0, 745.0),
    'H13': (2065.0, 1140.0), 'H14': (2105.0, 1175.0), 'H15': (2240.0, 1270.0), 'H16': (2315.0, 1300.0),
    'H17': (2475.0, 1420.0), 'H18': (2545.0, 1450.0), 'H19': (2695.0, 1535.0), 'H20': (2785.0, 1590.0),
    'H21': (2760.0, 1330.0), 'H22': (2710.0, 1270.0), 'H23': (2525.0, 1210.0), 'H24': (2445.0, 1135.0),
    'H25': (2330.0, 1080.0), 'H26': (2225.0, 1020.0), 'H27': (2765.0, 1045.0), 'H28': (2825.0, 1090.0),
    'H29': (2980.0, 1180.0), 'H30': (3065.0, 1220.0), 'H31': (3210.0, 1300.0), 'H32': (3190.0, 1075.0),
    'H33': (3040.0, 1000.0), 'H34': (3145.0, 745.0), 'H35': (3210.0, 720.0), 'H36': (2950.0, 640.0),
    'H37': (3015.0, 595.0),

    'O86': (1260.0, 630.0), 'O87': (1400.0, 535.0), 'O88': (1655.0, 370.0), 'O89': (1705.0, 320.0), 'O90': (2185.0, 245.0), 'O91': (2400.0, 110.0),
    'W96': (2560.0, 880.0), 'S96': (2660.0, 930.0), 'S97': (2760.0, 745.0), 'S98': (1980.0, 1560.0), 'S99': (2400.0, 1755.0), 'S100': (2800.0, 2010.0)
}

        self.points = self.Waypoints 

      #  self.neighbors = {
      #      'W1': ['W2'],#, 'W6'],      # W1 is near W2 and W6
      #      'W2': ['W1', 'W3', 'W6', 'H1'],  # W2 is near W1, W3, and W6
      #      'W3': ['W2', 'W4', 'W6', 'H2'],  # W3 is near W2, W4, and W6
      #     'W4': ['W3', 'W5', 'W6', 'H3'],  # W4 is near W3, W5, and W6
      #      'W5': ['W4', 'W6', 'W7', 'H4'],  # W5 is near W4, W6, and W7
      #      'W6': ['W1', 'W2', 'W3', 'W4', 'W5', 'W7', 'H5'],  # W6 connects many points
      #      'W7': ['W5', 'W6', 'W8', 'H6'],  # W7 is near W5, W6, and W8
      #      'W8': ['W7', 'W9', 'H7'],      # W8 is near W7 and W9
      #      'W9': ['W8', 'W10', 'H8'],     # W9 is near W8 and W10
      #      'W10': ['W9', 'W11', 'H9'],    # W10 is near W9 and W11
      #      'W11': ['W10'],          # W11 is near W10
      #      'H1': ['W2'],
      #      'H2': ['W3'],
      #      'H3': ['W4'],
      #      'H4': ['W5'],
      #      'H5': ['W6'],
      ###      'H6': ['W7'],
      #      'H7': ['W8'],
      #      'H8': ['W9'],
      #      'H9': ['W10'],
      #  }

        self.neighbors = {
                                    'W1': ['W2'],  # W1 is near W2
            'W2': ['W1', 'W3'],  # W2 is near W1 and W3
            'W3': ['W2', 'W4'],  # W3 is near W2 and W4
            'W4': ['W3', 'W5'],  # W4 is near W3 and W5
            'W5': ['W4', 'W6'],  # W5 is near W4 and W6
            'W6': ['W5', 'W7'],  # W6 connects many points
            'W7': ['W6', 'W8','W86'],  # W7 is near W6 and W8
            'W8': ['W7', 'W9'],  # W8 is near W7 and W9
            'W9': ['W8', 'W10'], # W9 is near W8 and W10
            'W10': ['W9', 'W11'], # W10 is near W9 and W11
            'W11': ['W10', 'W12','H25','H26'], # W11 is near W10 and W12
            'W12': ['W11', 'W13','H23','H24'], # W12 is near W11 and W13
            'W13': ['W12', 'W14','H21','H22'], # W13 is near W12 and W14
            'W14': ['W13', 'W15'], # W14 is near W13 and W15
            'W15': ['W14', 'W16'], # W15 is near W14 and W16
            'W16': ['W15', 'W17'], # W16 is near W15 and W17
            'W17': ['W16', 'W18'], # W17 is near W16 and W18
            'W18': ['W17', 'W19'], # W18 is near W17 and W19
            'W19': ['W18', 'W20'], # W19 is near W18 and W20
            'W20': ['W19', 'W21'], # W20 is near W19 and W21
            'W21': ['W20', 'W22'], # W21 is near W20 and W22
            'W22': ['W21', 'W23'], # W22 is near W21 and W23
            'W23': ['W22', 'W24'], # W23 is near W22 and W24
            'W24': ['W23', 'W25'], # W24 is near W23 and W25
            'W25': ['W24', 'W26','H19','H20'], # W25 is near W24 and W26
            'W26': ['W25', 'W27','H18','H17'], # W26 is near W25 and W27
            'W27': ['W26', 'W28','H15','H16'], # W27 is near W26 and W28
            'W28': ['W27', 'W9','H13','H14'], # W28 is near W27 and W29
            'W29': ['W7', 'W30'], # W29 is near W28 and W30
            'W30': ['W29', 'W31'], # W30 is near W29 and W31
            'W31': ['W30', 'W32'], # W31 is near W30 and W32
            'W32': ['W31', 'W33'], # W32 is near W31 and W33
            'W33': ['W32', 'W34'], # W33 is near W32 and W34
            'W34': ['W33', 'W35'], # W34 is near W33 and W35
            'W35': ['W34', 'W36','W47'], # W35 is near W34 and W36
            'W36': ['W35', 'W37','O86'], # W36 is near W35 and W37
            'W37': ['W36', 'W38','W90','O88','O89'], # W37 is near W36 and W38
            'W38': ['W37', 'W39', 'W40'], # W38 is near W37 and W39
            'W39': ['W38','H9'], # W39 is near W38 and W40
            'W40': ['W39','H10'], # W40 is near W39 and W41
            'W41': ['W38', 'W42'], # W41 is near W40 and W42
            'W42': ['W41', 'W43', 'W44'], # W42 is near W41 and W43
            'W43': ['W42','H12'], # W43 is near W42 and W44
            'W44': ['W42','H11'], # W44 is near W43 and W45
            'W45': ['W35', 'W46','W85'], # W45 is near W44 and W46
            'W46': ['W45', 'W47','W81'], # W46 is near W45 and W47
            'W47': ['W35', 'W46', 'W48', 'W66'], # W47 is near W46 and W48
            'W48': ['W47', 'W49'], # W48 is near W47 and W49
            'W49': ['W48', 'W50','W96'], # W49 is near W48 and W50
            'W50': ['W49', 'W51'], # W50 is near W49 and W51
            'W51': ['W50', 'W52'], # W51 is near W50 and W52
            'W52': ['W51', 'W53'], # W52 is near W51 and W53
            'W53': ['W52', 'W54'], # W53 is near W52 and W54
            'W54': ['W53', 'W55'], # W54 is near W53 and W55
            'W55': ['W54', 'W56'], # W55 is near W54 and W56
            'W56': ['W55', 'W57'], # W56 is near W55 and W57
            'W57': ['W56', 'W58'], # W57 is near W56 and W58
            'W58': ['W57', 'W59'], # W58 is near W57 and W59
            'W59': ['W58', 'W60'], # W59 is near W58 and W60
            'W60': ['W61','H31'], # W60 is near W59 and W61
            'W61': ['W60', 'W62','H29','H30'], # W61 is near W60 and W62
            'W62': ['W61', 'W63','H27','H28'], # W62 is near W61 and W63
            'W63': ['W62', 'W64'], # W63 is near W62 and W64
            'W64': ['W63', 'W65'], # W64 is near W63 and W65
            'W65': ['W64', 'W66','S97'], # W65 is near W64 and W66
            'W66': ['W47','W65', 'W67'], # W66 is near W65 and W67
            'W67': ['W66', 'W68'], # W67 is near W66 and W68
            'W68': ['W67', 'W69'], # W68 is near W67 and W69
            'W69': ['W68', 'W70'], # W69 is near W68 and W70
            'W70': ['W69', 'W71'], # W70 is near W69 and W71
            'W71': ['W70', 'W72','H33'], # W71 is near W70 and W72
            'W72': ['W71', 'W73','H32'], # W72 is near W71 and W73
            'W73': ['W72'], # W73 is near W72 and W74
            'W74': ['W67', 'W75'], # W74 is near W73 and W75
            'W75': ['W74', 'W76'], # W75 is near W74 and W76
            'W76': ['W75', 'W77'], # W76 is near W75 and W77
            'W77': ['W76', 'W78','H34','H35'], # W77 is near W76 and W78
            'W78': ['W77', 'W79'], # W78 is near W77 and W79
            'W79': ['W78', 'W80'], # W79 is near W78 and W80
            'W80': ['W79','H36','H37'], # W80 is near W79 and W81
            'W81': ['W46', 'W82'], # W81 is near W80 and W82
            'W82': ['W81', 'W83'], # W82 is near W81 and W83
            'W83': ['W82', 'W84'], # W83 is near W82 and W84
            'W84': ['W83', 'W85'], # W84 is near W83 and W85
            'W85': ['W45','W84'],  # W85 is near W84
            'W86': ['W7','W87'],
            'W87': ['W86','W88'],
            'W88': ['W87','W89'],
            'W89': ['W88','W90'],
            'W90': ['W37','W89','H4','H5','H6','H7','H8','O86','O87'],
            'W91': ['W92''W4'],
            'W92': ['W91','W93'],
            'W93': ['W92','W94'],
            'W94': ['W93','W95','H2'],
            'W95': ['W94','H1'],
            'W96': ['W49','S96'],
            'S96': ['W96'],
            'S97': ['W65'],
            'O86': ['W90'],
            'O87': ['W90'],
            'O88': ['W37'], 
            'O89': ['W37'],
            'O86': ['W36'],
            'S98': ['W95'], #Middle and high schoolaw
            'S99': ['W91'], #Movie theather 
            'S86': ['W36'],  
                                
                            # W11 is near W10
            'H1': ['W95'],
            'H2': ['W94'],
            'H3': ['W90'],
            'H4': ['W90'],
            'H5': ['W90'],
            'H6': ['W90'],
            'H7': ['W90'],
            'H8': ['W90'],
            'H9': ['W39'],
            'H10': ['W40'],
            'H11': ['W44'],
            'H12': ['W43'],
            'H13': ['W28'],
            'H14': ['W28'],
            'H15': ['W27'],
            'H16': ['W27'],
            'H17': ['W26'],
            'H18': ['W26'],
            'H19': ['W24'],
            'H20': ['W24'],
            'H21': ['W13'],
            'H22': ['W13'],
            'H23': ['W12'],
            'H24': ['W12'],
            'H25': ['W11'],
            'H26': ['W11'],
            'H27': ['W62'],
            'H28': ['W62'],
            'H29': ['W61'],
            'H30': ['W61'],
            'H31': ['W60'],
            'H32': ['W71'],
            'H33': ['W72'],
            'H34': ['W77'],
            'H35': ['W77'],
            'H36': ['W80'],
            'H37': ['W80'],



        }

        self.HouseWaypoints = {
            'H1': (1685.0, 1755.0), 'H2': (1905.0, 1875.0), 'H3': (1585.0, 935.0), 'H4': (1510.0, 875.0),
    'H5': (1620.0, 795.0), 'H6': (1725.0, 740.0), 'H7': (1830.0, 780.0), 'H8': (1740.0, 875.0),
    'H9': (2015.0, 610.0), 'H10': (2245.0, 455.0), 'H11': (2470.0, 605.0), 'H12': (2235.0, 745.0),
    'H13': (2065.0, 1140.0), 'H14': (2105.0, 1175.0), 'H15': (2240.0, 1270.0), 'H16': (2315.0, 1300.0),
    'H17': (2475.0, 1420.0), 'H18': (2545.0, 1450.0), 'H19': (2695.0, 1535.0), 'H20': (2785.0, 1590.0),
    'H21': (2760.0, 1330.0), 'H22': (2710.0, 1270.0), 'H23': (2525.0, 1210.0), 'H24': (2445.0, 1135.0),
    'H25': (2330.0, 1080.0), 'H26': (2225.0, 1020.0), 'H27': (2765.0, 1045.0), 'H28': (2825.0, 1090.0),
    'H29': (2980.0, 1180.0), 'H30': (3065.0, 1220.0), 'H31': (3210.0, 1300.0), 'H32': (3190.0, 1075.0),
    'H33': (3040.0, 1000.0), 'H34': (3145.0, 745.0), 'H35': (3210.0, 720.0), 'H36': (2950.0, 640.0),
    'H37': (3015.0, 595.0)
     }

        self.NPC_Houses = [
            'H3',
            'H4',
            'H5',
            'H6',
            'H7',
            'H8',
            'H9',
            'H10',
            'H11',
            'H12',
            'H13',
            'H14',
            'H15',
            'H16',
            'H17',
            'H18',
            'H19',
            'H20',
            'H21',
            'H22',
            'H23',
            'H24',
            'H25',
            'H26',
            'H27',
            'H28',
            'H29',
            'H30',
            'H31',
            'H32',
            'H33',
            'H34',
            'H35',
            'H36',
            'H37'
        
        ]

        self.NPC_work_locations = ['O86','O87','O88', 'O89','O86']
    
class choose_points():
    def __init__(self):
        self.waypoints_instance = Waypoints_class()

    def pick_house(self):
        # Pick a random house
        selected_house = random.choice(self.waypoints_instance.NPC_Houses)
        print(selected_house)
        #Remove the selected house from the dictionary
        return selected_house
    
    def Get_time(self):
           empty_string = []
           with file_lock:
            file_path = rf"C:\Users\narwh\Documents\Pythonshit\Hotspots\Support Files\TIME"
            with open(file_path, "r") as f:
                TIME = f.readlines()# 0 is Current order not open 1 is current buy order open 2 is current sell order open
                str_conversion = TIME
                while TIME == empty_string:
                    TIME = f.readlines()
                else:
                    data_tuple = eval(TIME[0])
            # Partition the tuple into variables
            hour_label, hour, minute_label, minute, day_label, day, calendar_label, calendar = data_tuple

            # Output the results
            #print(f"Hour: {hour}, Minute: {minute}, Day: {day}, Calendar: {calendar}") 
            #print(TIME)   
            return(day,minute,hour,calendar)
    
    def Draw_Points(self, screen):
        # Draw points
        activate_class = Waypoints_class()
        my_list = activate_class.points 
        for point, pos in my_list.items():
            pg.draw.circle(screen, (0, 0, 0), pos, 5)
            font = pg.font.Font(None, 24)
            text = font.render(point, True, (0, 0, 0))
            screen.blit(text, (pos[0] + 10, pos[1] - 10))

