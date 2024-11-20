

self.FINISHED_TASK = False
self.CURRENT_TIME = None
self.TASK_COUNTER = None
self.TASK_FINISH_TIME = None
self.TASK_TOTAL_HOURS_COMPLETED_TEMP = None
self.TASK_START_TIME = None
self.TASK_DURATION_FINAL = None
self.TASK = None
self.INITIAL_ARRIVAL = True


def Do_Task(self,screen,Task,Duration):
        self.TASK = Task
        if self.is_traveling == True and self.FINISHED_TASK == False:
            self._walk(screen, self.TASK_LOCATION)
        elif self.is_traveling == False and self.arrival_counter == 1 and self.FINISHED_TASK == False: #NPC is not traveling, has arrived, and has not finished task
            self.state = "TASK"
            if  self.INITIAL_ARRIVAL == True:
                calculate_TASK_END_TIME(Duration)
                self.INITIAL_ARRIVAL = False
            if  self.CURRENT_TIME == self.TASK_FINISH_TIME: #Task is complete trigger walking home
                self.TASK_TOTAL_HOURS_COMPLETED_TEMP +=  self.CURRENT_TIME - self.TASK_START_TIME
                self.TASK_DURATION_FINAL = abs(self.TASK_TOTAL_HOURS_COMPLETED_TEMP)
                self.TASK_TOTAL_HOURS_COMPLETED_TEMP = 0
                self.FINISHED_TASK = True
                self.is_traveling = True
                self.success = 0
                print('finished', Task)
                self.TASK_START_TIME = 0
            else: #Task is not complete counter remains at 0 indicating not completed
                self.TASK_COUNTER = 0
        elif    self.FINISHED_TASK == True:
            if  self.success == 1:
                self.FINISHED_TASK = False
                self.first_counter = 0
                self.arrival_counter = 0
                self.action_lock = False
                self.success = 2
                self.TASK_COUNTER = 0
                self.INITIAL_ARRIVAL = True
                print("At Home")
            else:
                #Go Home
                self._walk(screen, self.house_location)

def calculate_TASK_END_TIME(self,Duration):
    length_of_time = Duration #in minutes 
    current_hour, current_minute = self.CURRENT_TIME 
    Minutes = current_minute  + length_of_time
    if Minutes >= 61:
        mod_check = Minutes % 60 
        if mod_check == 0:
            Hour_mark = Minutes / 60   
            self.TASK_FINISH_TIME = (Hour_mark,0)
        else: 
            Hour_mark = Minutes / 60 
            hour = Hour_mark   
            minute = mod_check 
            self.TASK_FINISH_TIME = (hour,minute)
    else:
        self.TASK_FINISH_TIME = (current_hour,Minutes)
    

     
    

def actual_work(self):
        #simulate clocking in
            if self.clock_in_check == 0:
                self.temp_hour = self.Current_Hour
                self.clock_in_check = 1
                if self.Current_Hour != self.Min_work_time:
                    self.Late_counter += 1
                    print(self.Late_counter, self.max_late_times)
                if self.Late_counter == self.max_late_times:
                    self.unemployed == True
                    self.clock_off_time == self.Current_Hour
                    print('UNEMPLOYED')
            else:
                 pass
            if self.working_hours > 8:
                    self.working_hours -= 1
                    self.working_hours += self.working_hours
                else:
                    self.working_hours += self.working_hours