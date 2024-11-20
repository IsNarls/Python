#start of game
# Import Modules
import os
import pygame as pg
import random
import time
import Main_init
import random
from collections import deque



class NPC_Crime(pg.sprite.Sprite):
    """generate and NPC on screen and print its position"""

    def __init__(self):
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

        # Vitals
        self.health_status = 100  # Max health
        self.walking_speed = 1.0   # Base walking speed
        self.heart_rate = 70       # BPM
        self.emotional_state = "flat"  # flat, angry, excited, stressed
        self.health_conditions = []  # List of health conditions
        self.hunger = 0             # 0-100 scale
        self.need_entertainment = False
        self.sleep_counter = 0              # Track sleep hours
        self.is_alive = True
        self.WORK_DURATION = 20
        self.work_ticks = 0
        self.work_cooldown = False
        self.death_count = 0
        self.sleep_duration = random.randint(4, 10)
        self.Min_sleep_duration = None
        self.hunger_rate = .75
        self.wake_time = None
        


        # Apartment
        self.apartment_capacity = 1
        self.food_supply = 3        # Initial meals
        self.max_food_supply = 9    # Max meals that can be stored

        # Economics
        self.net_worth = 0          # Initial net worth
        self.income = 0             # Income determined by occupation
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

        # Actions
        self.actions = ['work', 'idle', 'sleep', 'Get Groceries']  #'work',
       
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

    def tick(self):
        """Simulate the passage of time."""
        Day,minute,hour,Calender = Main_init.Get_time()
        self.Current_Hour = int(hour)
        self.Current_minute = int(minute)
        self.Current_day = int(Day)
        self.Calender_counter = int(Calender)
        #print('NPC at:', self.npc_position,self.Current_day,self.Current_minute,self.Current_Hour,self.Calender_counter)
        #print('NPC at:', self.npc_position,self.Current_day,self.Current_minute,self.Current_Hour,self.Calender_counter, self.npc_position, self.hunger, self.emotional_state, self.health_status, self.state, self.Current_day, self.Current_Hour, self.Current_minute)
        #print(self.Current_Hour, self.Current_minute, self.Current_day)
        self.CURRENT_TIME = (self.Current_Hour,self.Current_minute)
        print(self.CURRENT_TIME)
        self.Hour_of_current = self.Current_Hour
        if self.old_hour != self.Hour_of_current:
            #print(self.Current_Hour, self.Current_minute, self.Current_day, self.Calender_counter)
            #self.check_death()
            self.hunger += self.hunger_rate 
        if self.Calender_counter == 365:
            self.age += 1
            self.Calender_counter = 0 
        self.old_hour = self.Hour_of_current
        if self.Min_work_time <= self.Current_Hour < self.Max_work_time and self.unemployed != False:
            self.actions = ['work', 'idle', 'Get Groceries']
        elif self.Current_Hour >= 17 or self.Current_Hour < 8: 
            self.actions = ['sleep', 'idle', 'Get Groceries']
        
    def check_death(self):
        """Check if the NPC has died."""
        if self.hunger > 100:
            self.hunger = 100
        if self.hunger == 100:
            self.health_status = self.health_status - 1
        if self.hunger == 100 and self.health_status <= 0:
            self.is_alive = False
        if self.is_alive == False and self.death_count == 1:
            print("they are dead")
        self.get_state()

    def idle(self):
        idle_timer = 0
        """NPC stays at home and consumes meals."""
        #if self.food_supply > -6:
            #self.food_supply -= 1  # Consume one meal
            ## Simulate 4 hours passing in-game
        #if self.counter_timer == 25:
            #self.tick()
            #self.counter_timer == 0
        #else:
            #self.counter_timer += 1  # Pass time and update status
        self.state = "idleing"
        self.action_lock = False
        self.reward = 0
        self.update_q_value(self.action, self.reward)

    def Get_Groceries(self,screen):
        """NPC stays at home and consumes meals."""
        self.state = 'Getting Groceries'
        if self.is_traveling == True and self.finished_shopping == 0:
            self._walk(screen, self.Grocery_location)
        elif self.is_traveling == False:
            if self.first_counter == 0:
                self.temp_minute = self.Current_minute
                self.first_counter = 1
                self.finished_shopping_time = self.temp_minute + self.shopping_duration
                if self.finished_shopping_time > 60:
                    self.temp_minute_over60 +=  self.finished_shopping_time - self.shopping_duration
                    self.finished_shopping_time = abs(self.temp_minute_over60)
            print('here1')
            #print('Current MINUTE:', self.Current_minute, 'Current finish time:',self.finished_shopping_time)
            if self.Current_minute == self.finished_shopping_time:
                self.is_traveling = True
                self.reward = 10
                self.success = 0
                self.finished_shopping  = 1
                #print('done shopping')
                #print('shopping')
                print('here2')
        elif self.finished_shopping  == 1:
            if self.success == 1:
                self.finished_shopping = 0
                self.first_counter = 0
                self.arrival_counter = 0
                self.action_lock = False
                self.success = 2
                #print("At Home")
                print('here3')
            else:
                self._walk(screen, self.house_location)

    def Go_to_convience_store(self,screen):
        """NPC stays at home and consumes meals."""
        if self.is_traveling == True and self.finished_shopping == 0:
            self._walk(screen, self.Convience_Store_location)
        elif self.is_traveling == False:
            if self.first_counter == 0:
                self.temp_minute = self.Current_minute
                self.first_counter = 1
                self.finished_shopping_time = self.temp_minute + self.shopping_duration
                if self.finished_shopping_time > 60:
                    self.temp_minute_over60 +=  self.finished_shopping_time - self.shopping_duration
                    self.finished_shopping_time = abs(self.temp_minute_over60)
            #print('here11')
            #print('Current MINUTE:', self.Current_minute, 'Current finish time:',self.finished_shopping_time)
            if self.Current_minute == self.finished_shopping_time:
                self.is_traveling = True
                self.reward = 10
                self.success = 0
                self.finished_shopping  = 1
                #print('done shopping')
                #print('shopping')
        elif self.finished_shopping  == 1:
            if self.success == 1:
                self.finished_shopping = 0
                self.first_counter = 0
                self.arrival_counter = 0
                self.action_lock = False
                self.success = 2
                #print("At Home")
            else:
                self._walk(screen, self.house_location)
    
    def Write_location_to_file(Time):
            file_path = rf"C:\Users\narwh\OneDrive\Documents\Pythonshit\Hotspots\Support Files\Location"
            with open(file_path, "w+") as f:
                f.write(Time) 
                f.close()

    def sleep(self):
        """NPC sleeps, does not consume meals."""
        if self.sleep_lock  != 0:
            self.state = "sleeping"
            self.hunger_rate = .25
            self.sleep_lock = 1
            print('fell asleep')
            self.Min_sleep_duration = self.Current_Hour + self.sleep_duration
            if self.Min_sleep_duration > 24:
                self.wake_time = self.Min_sleep_duration - 24
                self.wakeup = 0 + self.wake_time 
                print("greater than 24", self.wakeup)
            else:
                self.wakeup = self.Min_sleep_duration 
                print("Less than 24", self.wakeup)
        #print(self.Current_Hour + self.sleep_duration)
        if self.wakeup == self.Current_Hour:
            self.action_lock = False
            self.sleep_lock = 0
            print("Woke up")
            self.sleep_counter = 1
            #self.state = "Awake"
            self.hunger_rate = .75
            self.success == 2
        else:
            if self.sleep_lock  == 0:
                self.sleep_lock = 1
                print('fell asleep')
                self.Min_sleep_duration = self.Current_Hour + self.sleep_duration
                if self.Min_sleep_duration > 24:
                    self.wake_time = self.Min_sleep_duration - 24
                    self.wakeup = 0 + self.wake_time 
                    print("greater than 24", self.wakeup)
                else:
                    self.wakeup = self.Min_sleep_duration 
                    print("Less than 24", self.wakeup)
        #print(self.old_hour, self.Current_Hour)
     
    def work(self,screen):
        if self.is_traveling == True and self.finished_work == 0:
            self._walk(screen, self.work_location)
            #print('here1')
            #print(self.is_traveling, self.arrival_counter, self.work_counter)
        elif self.is_traveling == False and self.arrival_counter == 1 and self.work_counter == 0:
            """NPC works and earns income."""
            self.state = "working"
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
            # Simulate working hours
            if self.Current_Hour != self.clock_off_time:
                self.work_counter = 0
                #print(self.Current_Hour, self.clock_off_time)
                #print('here6')
            if self.Current_Hour == self.clock_off_time:
                self.working_hours_temp +=  self.Current_Hour - self.temp_hour
                self.working_hours = abs(self.working_hours_temp)
                if self.working_hours > 8:
                    self.working_hours -= 1
                    self.working_hours += self.working_hours
                    print('here4')
                else:
                    self.working_hours += self.working_hours
                print(self.working_hours)
                self.working_hours_temp = 0
                self.finished_work = 1
                self.is_traveling = True
                self.reward = 10
                self.success = 0
                self.work_counter = 0
                print('finished working')
                #self.state = "walking home"
                self.work_counter = 1
                self.clock_in_check = 0
        elif    self.finished_work == 1:
            if self.success == 1:
                self.finished_work = 0
                self.first_counter = 0
                self.arrival_counter = 0
                self.action_lock = False
                self.success = 2
                self.work_counter = 0
                print("At Home")
            else:
                self._walk(screen, self.house_location)
        #elif self.is_traveling == False:
        #elif self.success == 1:
            #if self.success == 1:
                #self.finished_work = 0
                #self.first_counter = 0
                ##self.arrival_counter = 0
                #self.action_lock = False
                #self.success = 2
                #print("At Home")
        
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
        
    def Draw_current_pos(self, screen):
        pg.draw.circle(screen, (255, 0, 0), (int(self.current_position[0]), int(self.current_position[1])), 20)

    def update(self,screen):
        self.tick()
        #print(self.success)
        #if self.counter_timer == 1:
                #self.persist_state == False
        if self.is_alive == True:
            # Choose an action
            if self.action_lock == False:
                self.action = self.choose_action()
                self.is_traveling = True
                self.action_lock = True
                self.success = 0
                #print('here1')
            #action chosen do not change until completed
            if self.action_lock == True:
                if self.action == 'work':
                    self.work(screen)
                    if self.success == 2:
                        self.reward = self.age + self.net_worth
                        self.update_q_value(self.action, self.reward)
                        #print('here2')
                elif self.action == 'idle':
                    self.idle()
                elif self.action == 'Get Groceries':
                    self.Get_Groceries(screen)
                    if self.success == 2:
                        self.reward = 0
                        self.update_q_value(self.action, self.reward)
                elif self.action == 'sleep':
                    self.sleep()
                    if self.success == 2:
                        self.reward = 0
                        self.update_q_value(self.action, self.reward)
                        #print('here3')
        else:
            print('NPC IS DEAD')
            pass
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


            

