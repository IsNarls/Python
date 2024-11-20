#start of game
# Import Modules
import os
import pygame as pg
import random
import time
import Main_init
import random
from collections import deque
import math


class NPC_Crime(pg.sprite.Sprite):
    """generate and NPC on screen and print its position"""

    def __init__(self):
        self.NPC_NAME = random.randint(1,12345667)
        self.counter_timer = 0
        pg.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.image, self.rect = Main_init.load_image(r"C:\Users\narwh\OneDrive\Documents\Pythonshit\Hotspots\Support Files\PersonDot.png", -1, 1)
        screen = pg.display.get_surface()
        self.area = screen.get_rect()
        self.running = True
        self.path = []
        self.destination = None
        self.success = 0
        # Initialize NPC starting position and first destination
        self.npc_position = Main_init.pick_house()
        self.current_position = Main_init.points[self.npc_position]
        self.age = 24
        self.first_counter = 0
        self.gender = 'Male'
        self.race = 'white'
        self.occupation = 'Janitor'
        self.clock_off_time = 17
        self.work_location = 'H2'
        self.Grocery_location = 'H8'
        self.Convience_Store_location = 'H9'
        self.reward = 0 
        self.temp_minute_over60 = 0
        self.house_location = self.npc_position
        self.Current_time = None
        self.arrival_counter = 0
        self.CURRENT_TIME=None
        self.FINISHED_TASK = False
        self.CURRENT_TIME = None
        self.TASK_COUNTER = None
        self.TASK_FINISH_TIME = None
        self.TASK_TOTAL_HOURS_COMPLETED_TEMP = 0
        self.TASK_START_TIME = None
        self.TASK_DURATION_FINAL = None
        self.TASK = None
        self.INITIAL_ARRIVAL = True
        self.TASK_LOCATION = None

        # Vitals
        self.health_status = 100  # Max health
        self.walking_speed = 1.0   # Base walking speed
        self.heart_rate = 70       # BPM
        self.emotional_state = "flat"  # flat, angry, excited, stressed
        self.health_conditions = []  # List of health conditions
        self.hunger = 0             # 0-100 scale
        self.energy = 100
        self.energy_decay = random.randint(1, 5)
        self.need_entertainment = False
        self.sleep_counter = 0              # Track sleep hours
        self.is_alive = True
        self.WORK_DURATION = 480
        self.work_ticks = 0
        self.work_cooldown = False
        self.death_count = 0
        self.sleep_duration = random.randint(240, 600)
        self.Min_sleep_duration = None
        self.hunger_rate = .75
        self.wake_time = None
        


        # Apartment
        self.apartment_capacity = 1
        self.food_supply = 3        # Initial meals
        self.max_food_supply = 9    # Max meals that can be stored

        # Economics
        self.net_worth = random.randint(0,1500)          # Initial net worth
        self.income = random.randint(700,1400)             # Income determined by occupation
        self.expenses = 0           # Net loss to income
        self.working_hours = 0       # Hours worked
        self.max_late_times = random.randint(1, 10)
        self.Late_counter = 0
        self.Min_work_time = 8
        self.Max_work_time = 17


        # State
        self.state = None        # idle, sleeping, walking, working
        self.action = None

        # Q-learning attributes
        self.action = None
        self.action_lock = False
        self.q_table = {}  # Q-table to store Q-values
        self.learning_rate = 0.1
        self.discount_factor = 0.9
        self.exploration_rate = 1.0
        self.exploration_decay = 0.99
        self.min_exploration_rate = 0.1
        self.action = None
        self.reward = None
        self.is_traveling = None
        self.walk_counter = 0
        self.work_counter = 0 
        self.tick_counter = 0
        self.first_draw_counter = True
        self.finished_work = 0
        self.time = 0
        self.sleep_timer = 0
        self.Current_minute = None
        self.Current_day = None
        self.old_hour = None
        self.Hour_of_current = None
        self.sleep_lock = 0
        self.differential = 0
        self.wakeup = None
        self.clock_in_check = 0
        self.working_hours_temp = 0
        self.temp_hour = None
        self.temp_minute = None
        self.unemployed = None
        self.shopping_duration = random.randint(15, 60)
        self.finished_shopping_time = None
        self.finished_shopping = 0
        self.color = (255, 0, 0)

        # Actions
        self.actions = ['work', 'idle', 'sleep', 'Get Groceries', 'Go_to_convience_store', 'Eat']  #'work',
   #Q value block     
    def choose_action(self):
        """Choose an action based on the Q-learning policy."""
        state = self.get_state()  # Get current state representation

        # Exploration vs Exploitation
        if random.random() < self.exploration_rate:
            return random.choice(self.actions)  # Explore
        else:
            # Exploit: Choose the best action based on Q-values
            if state not in self.q_table:
                self.q_table[state] = {action: 0 for action in self.actions}
            return max(self.q_table[state], key=self.q_table[state].get)
    def get_state(self):
        """Return a representation of the current state."""
        #if self.Current_minute == 30:
        #print(self.npc_position, self.hunger, self.emotional_state, self.health_status, self.state, self.Current_day, self.Current_Hour, self.Current_minute)
        return (self.npc_position, self.hunger, self.emotional_state)
    def calculate_reward(self):
        penalty = 10  # Example penalty value
        reward = 0
        
        

        if new_net_worth < self.net_worth:
            reward -= penalty  # Penalty for losing net worth
        if new_age > self.age:
            reward -= penalty  # Penalty for aging
        
        return reward
    def update_q_value(self, action, reward):
        """Update the Q-value based on the action taken."""
        state = self.state
        print('THIS IS THE Q TABLE', self.q_table)
        # Initialize the state in the Q-table if it doesn't exist
        if state not in self.q_table:
            self.q_table[state] = {a: 0 for a in self.actions}

        # Check if the action exists in the Q-table for the current state
        if action not in self.q_table[state]:
            # If the action is not initialized, add it
            self.q_table[state][action] = 0

        # Get the best future reward for the next state
        future_reward = max(self.q_table[state].values()) if state in self.q_table else 0

        # Q-learning formula
        self.q_table[state][action] += self.learning_rate * (reward + self.discount_factor * future_reward - self.q_table[state][action])

        # Decay exploration rate
        if self.exploration_rate > self.min_exploration_rate:
            self.exploration_rate *= self.exploration_decay
        self.action_lock = False

        print(f"Final Reward: {reward}")
        print(f"Q-table for state {state}: {self.q_table[state]}")
    
   #status checks 
    def tick(self):
        """Simulate the passage of time."""
        Day,minute,hour,Calender = Main_init.Get_time()
        self.Current_Hour = int(hour)
        self.Current_minute = int(minute)
        self.Current_day = int(Day)
        self.Calender_counter = int(Calender)
        self.CURRENT_TIME = (self.Current_Hour,self.Current_minute)
        self.Hour_of_current = self.Current_Hour
        self.update_vitals()
        self.old_hour = self.Hour_of_current
        self.update_avaliable_actions()
      
    def check_death(self):
        """Check if the NPC has died."""
        if self.hunger > 100:
            self.hunger = 100
        if self.hunger == 100:
            self.health_status = self.health_status - 1
        if self.energy == 0:
            self.is_alive = False
        if self.hunger == 100 and self.health_status <= 0:
            self.is_alive = False
        if self.is_alive == False and self.death_count == 1:
            print("they are dead")
        self.get_state()

    def update_vitals(self):
        if self.old_hour != self.Hour_of_current:
            self.hunger += self.hunger_rate 
            self.energy -= self.energy_decay
        if self.Calender_counter == 365:
            self.age += 1
            self.Calender_counter = 0 
            
    def update_avaliable_actions(self):
        if self.Min_work_time <= self.Current_Hour < self.Max_work_time and self.unemployed != False:
            self.actions = ['work', 'idle', 'Get Groceries', 'Go_to_convience_store', 'Eat']
        elif self.Current_Hour >= 17 or self.Current_Hour < 8: 
            self.actions = ['sleep', 'idle', 'Get Groceries', 'Go_to_convience_store', 'Eat']   


#start action definition
    def idle(self):
        """NPC stays at home and consumes meals."""
        self.state = "idleing"
        self.action_lock = False
    
    def Get_Groceries(self):
        """NPC stays at home and consumes meals."""
        self.food_supply = self.max_food_supply
        self.net_worth -= 100
        if self.net_worth < 0:
            self.net_worth = 0
            self.food_supply = 0
       
    def Go_to_convience_store(self):
        """NPC stays at home and consumes meals."""
        self.food_supply = self.max_food_supply 
        self.net_worth -= 100
        if self.net_worth < 0:
            self.net_worth = 0
            self.food_supply = 0

    def sleep(self):
        self.energy = 100
        """NPC sleeps, does not consume meals."""
        pass
     
    def work(self):
        self.work_counter += 8
        if self.work_counter == 40:
            self.net_worth += self.income
            self.work_counter = 0
        self.Eat()

    def Eat(self):
        if self.food_supply > 0:
            self.energy += 50
            self.hunger -= 50
            if self.energy > 100:
                self.energy = 100
            if self.hunger > 100:
                self.hunger = 100
            self.food_supply -= 1
        else:
            #print('Out of Food')
            pass  

#Task completion section
    def Do_Task(self,screen,Task,Duration,location,TaskName):
            self.TASK = Task
            if self.is_traveling == True and self.FINISHED_TASK == False:
                self._walk(screen, location)
            elif self.is_traveling == False and self.arrival_counter == 1 and self.FINISHED_TASK == False: #NPC is not traveling, has arrived, and has not finished task
                self.state = TaskName
                if  self.INITIAL_ARRIVAL == True:
                    self.calculate_TASK_END_TIME(Duration)
                    self.INITIAL_ARRIVAL = False
                    print(Task, self.CURRENT_TIME, self.TASK_FINISH_TIME )
                if  self.CURRENT_TIME == self.TASK_FINISH_TIME: #Task is complete trigger walking home
                    self.TASK_TOTAL_HOURS_COMPLETED_TEMP += Duration  #self.CURRENT_TIME - self.TASK_START_TIME
                    self.TASK_DURATION_FINAL = abs(self.TASK_TOTAL_HOURS_COMPLETED_TEMP)
                    self.TASK_TOTAL_HOURS_COMPLETED_TEMP = 0
                    self.FINISHED_TASK = True
                    self.is_traveling = True
                    self.success = 0
                    print('finished', Task)
                    self.TASK # This triggers the associated task function once.
                    self.TASK_START_TIME = 0
                else: #Task is not complete counter remains at 0 indicating not completed Task function can be implemented here
                    self.TASK_COUNTER = 0
                    #self.TASK 
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
        length_of_time = 0
        Minutes = 0
        Hour_mark = 0
        mod_check = 0 
        length_of_time = Duration #in minutes 
        current_hour, current_minute = self.CURRENT_TIME 
        Minutes = current_minute  + length_of_time
        if Minutes >= 61:
            Hour_mark = math.floor(Minutes/60)
            print(Hour_mark,Minutes)
            check_hour_over_24 = current_hour + Hour_mark
            mod_check = Minutes % 60
            time = Hour_mark + current_hour
            if check_hour_over_24 >= 24:
                Hour_mark = check_hour_over_24 % 24 
                time = Hour_mark
            if mod_check == 0:  
                self.TASK_FINISH_TIME = (time,0)
            else:  
                Minutes = mod_check 
                self.TASK_FINISH_TIME = (time,Minutes)
        else:
            self.TASK_FINISH_TIME = (current_hour,Minutes)
        

    def _walk(self,screen, destinationn):
        #print('Walking to: ' + destinationn)
            # Choose a new random destination if we don't have one or we've reached the current one
        if self.destination is None or self.current_position == Main_init.points[self.destination]:
            #print(self.destination, self.current_position, self.path)
            
            # Use the NPC's current position as the starting point
            npc_position = next(point for point, pos in Main_init.points.items() if pos == self.current_position)
            available_points = list(Main_init.points.keys())
            #print(available_points)
            available_points.remove(npc_position)  # Exclude the current position

            # Ensure the destination is different from the current position
            if available_points:
                self.destination = destinationn #random.choice(available_points)  # Select a new destination
                self.path = self.bfs(npc_position, self.destination)
                #print('here1')  # Find the path to the new destination
                if self.first_counter == 1:
                    self.first_counter = 0
                    self.success = 1
                    self.is_traveling = False
                    self.arrival_counter = 1
                elif self.first_counter == 0:
                    self.first_counter = 1
                    #self.is_traveling = True
                #self.is_traveling == True

        # Move to next point in the path
        if self.path and self.current_position:
            next_point = self.path[0]  # Get the next point in the path
            next_position = Main_init.points[next_point]
            
            # Create a vector to the next point
            direction = pg.math.Vector2(next_position) - pg.math.Vector2(self.current_position)
            if direction.length() > 0:
                direction.normalize_ip()
                self.current_position = (self.current_position[0] + direction.x * 2, self.current_position[1] + direction.y * 2)

            # Check if we've reached the next point
            if pg.math.Vector2(self.current_position).distance_to(next_position) < 2:
                self.current_position = next_position
                self.path.pop(0)  # Remove the reached point from the path
        self.walk_counter += 1
        #self.Draw_Points(screen)
        self.Draw_current_pos(screen)

        # Draw the destination point
        if self.destination:
            pg.draw.circle(screen, (0, 255, 0), Main_init.points[self.destination], 10)  # Destination in green
    def bfs(self, start, goal):
        queue = deque([[start]])
        visited = {start}
        
        while queue:
            path = queue.popleft()
            node = path[-1]
            if node == goal:
                return path
            for neighbor in Main_init.neighbors[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append(new_path)
        #print("No Path", neighbor, Main_init.neighbors[node])
        return None  # No path found     
    #def Write_location_to_file(self,Location):
            #file_path = rf"C:\Users\narwh\OneDrive\Documents\Pythonshit\Hotspots\Support Files\NPC_DATA\{self.NPC_NAME}"
            #with open(file_path, "w+") as f:
            #    f.write(str(Location)) 
            #    f.close()    
    def Draw_current_pos(self, screen):
        #ocation = int(self.current_position[0]), int(self.current_position[1])
        #self.Write_location_to_file(Location)
        if self.first_draw_counter == True:
            pg.draw.circle(screen, self.color, (int(self.current_position[0]), int(self.current_position[1])), 20)
        else:
            # In your game loop
            screen.blit(screen, (int(self.current_position[0]), int(self.current_position[1])))
        #pg.draw.circle(screen, self.color, (int(self.current_position[0]), int(self.current_position[1])), 20)
    
    def update(self,screen):
        self.tick()
        if self.is_alive == True:
            # Choose an action
            if self.action_lock == False:
                self.action = self.choose_action()
                self.is_traveling = True
                self.action_lock = True
                self.success = 0
            #action chosen do not change until completed
            if self.action_lock == True:
                if self.action == 'work':
                    self.Do_Task(screen,self.work(),self.WORK_DURATION,self.work_location,'Work')
                    if self.success == 2:
                        self.reward = self.age + self.net_worth + self.energy + self.hunger
                        self.update_q_value(self.action, self.reward)
                elif self.action == 'idle':
                    self.idle()
                    if self.success == 2:
                        self.reward = self.age + self.net_worth + self.energy + self.hunger
                        self.update_q_value(self.action, self.reward)
                elif self.action == 'Get Groceries':
                    self.Do_Task(screen,self.Get_Groceries(),self.shopping_duration,self.Grocery_location,'Get Groceries')
                    if self.success == 2:
                        self.reward = self.age + self.net_worth + self.energy + self.hunger
                        self.update_q_value(self.action, self.reward)
                elif self.action == 'sleep':
                    self.Do_Task(screen,self.sleep(),self.sleep_duration,self.house_location,'Sleep')
                    if self.success == 2:
                        self.reward = self.age + self.net_worth + self.energy + self.hunger
                        self.update_q_value(self.action, self.reward)
                elif self.action == 'Go_to_convience_store':
                    self.Do_Task(screen,self.Go_to_convience_store(),self.shopping_duration,self.Convience_Store_location,'Sleep')
                    if self.success == 2:
                        self.reward = self.age + self.net_worth + self.energy + self.hunger
                        self.update_q_value(self.action, self.reward)
                elif self.action == 'Eat':
                    self.Do_Task(screen,self.Eat(), 5,self.house_location,'Eating')
                    if self.success == 2:
                        self.reward = self.age + self.net_worth + self.energy + self.hunger
                        self.update_q_value(self.action, self.reward)
             
        else:
            #print('NPC IS DEAD')
            self.color = (0, 0, 255)
        self.Draw_current_pos(screen)
        self.check_death()

           
#buildings that need to built
#Park
#School
#Apartment
#Factory Work
#Library
#Construction Work
#Gas Station. 


            

