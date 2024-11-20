#old code 


        if self.Current_Hour < 17:
            self.work_counter = 0
            self.tick_counter += 1
            self.working_hours += 1
        # Simulate working hours
        if self.work_counter == 25 and self.tick_counter < 8:
            #self.tick()
            self.work_counter = 0
            self.tick_counter += 1
            self.working_hours += 1
            #print('working')
        elif self.tick_counter == 8:
            self.working_hours = 0
            self.tick_counter = 0
            self.finished_work = 1
            self.is_traveling = True
            self.reward = 10
            self.work_counter = 0
            #print('finished working')
            self.state = "walking home"
        self.work_counter += 1
            #self.food_supply -= 1  # Works for 8 hours
        #self.income += self.calculate_income() 
        #print('working') # Earn income based on occupation
        # Update stress and health status based on occupation