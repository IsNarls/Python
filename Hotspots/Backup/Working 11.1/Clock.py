from multiprocessing import Lock




file_lock = Lock()

class Mark_time_class():

    def __init__(self):
        self.main_counter = 0
        self.Game_clock = 0
        self.Minute_timer = 0
        self.Hour_timer = 8
        self.Day_timer = 1 
        self.Calender_counter = 0
        self.Year_counter = 1
        self.time_of_day = None
        
    def Mark_time(self):
        self.Game_clock += 1
        # 1 minute = 27 ticks, total ticks = 38880 (1440 minutes in 1 day)
        # start time is 8am, 480 minutes have passed 960 minutes to go.
        if self.Game_clock == 2500000:
            #print(Minute_timer)
            self.Game_clock = 0
            self.Minute_timer += 1
            self.time_of_day = ('Hour:', self.Hour_timer, 'minute:', self.Minute_timer,'Day:', self.Day_timer,'Calender:', self.Calender_counter)
            self.Write_time_to_file(str(self.time_of_day))
        if self.Minute_timer == 60:
            self.Minute_timer = 0 
            self.Hour_timer += 1
        if self.Hour_timer == 24:
            self.Day_timer += 1
            self.Hour_timer = 0
        if self.Day_timer == 7:
            self.Day_timer = 0
            self.Calender_counter += 7
        if self.Calender_counter == 365:
            self.Calender_counter = 0 
            self.Year_counter += 1
        
    def Write_time_to_file(self,Time):
            with file_lock:
                file_path = rf"C:\Users\narwh\Documents\Pythonshit\Hotspots\Support Files\TIME"
                with open(file_path, "w+") as f:
                    f.write(Time) 
                    print(Time)
                    f.close()
                        

mark_time_instance = Mark_time_class()
while True:
    start_clocking = mark_time_instance.Mark_time()
    start_clocking
