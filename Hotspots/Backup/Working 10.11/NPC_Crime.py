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
        self.npc_position = 'W1' 
        self.current_position = Main_init.points[self.npc_position]
        self.age = 24
        self.first_counter = 0
        self.gender = 'Male'
        self.race = 'white'
        self.occupation = 'Janitor'
        self.work_location = 'H2'
        self.Grocery_location = 'H8'
        self.reward = 0 
        self.persist_state = True
        self.house_location = 'H1'
        self.Current_time = None

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

        # Apartment
        self.apartment_capacity = 1
        self.food_supply = 3        # Initial meals
        self.max_food_supply = 9    # Max meals that can be stored

        # Economics
        self.net_worth = 0          # Initial net worth
        self.income = 0             # Income determined by occupation
        self.expenses = 0           # Net loss to income
        self.working_hours = 0       # Hours worked

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
        self.Curret_minute = None
        self.Current_day = None
        self.old_hour = None
        self.Hour_of_current = None

        # Actions
        self.actions = ['work', 'idle', 'sleep']  #'work',
       
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
        print(self.npc_position, self.hunger, self.emotional_state, self.health_status, self.state)
        return (self.npc_position, self.hunger, self.emotional_state)

    def update_q_value(self, action, reward):
        """Update the Q-value based on the action taken."""
        state = self.get_state()
        if state not in self.q_table:
            self.q_table[state] = {a: 0 for a in self.actions}

        # Get the best future reward for the next state
        future_reward = max(self.q_table[state].values()) if state in self.q_table else 0

        # Q-learning formula
        self.q_table[state][action] += self.learning_rate * (reward + self.discount_factor * future_reward - self.q_table[state][action])

        # Decay exploration rate
        if self.exploration_rate > self.min_exploration_rate:
            self.exploration_rate *= self.exploration_decay
        self.action_lock = False

    def tick(self,time_of_day):
        """Simulate the passage of time."""
        self.Current_Hour, self.Curret_minute, self.Current_day, self.Calender_counter = time_of_day
        #print(self.Current_Hour, self.Curret_minute, self.Current_day)
        self.Hour_of_current = self.Current_Hour
        if self.old_hour != self.Hour_of_current:
            print(self.Current_Hour, self.Curret_minute, self.Current_day, self.Calender_counter)
            self.check_death()
            self.hunger += .75
        if self.Calender_counter == 365:
            self.age += 1
            self.Calender_counter = 0 
        self.old_hour = self.Hour_of_current

    def check_death(self):
        """Check if the NPC has died."""
        if self.hunger > 100:
            self.hunger = 100
        if self.hunger == 100:
            self.health_status = self.health_status - 1
        if self.hunger == 100 and self.health_status <= 0:
            self.is_alive = False
            #print("they are dead")

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
        if self.Current_Hour != self.Hour_of_current:
            ("Chilling")
        self.state = "idleing"


    def go_to_store(self):
        """NPC stays at home and consumes meals."""
        if self.food_supply > -6:
            self.food_supply -= 1  # Consume one meal
            # Simulate 4 hours passing in-game
            self.tick()  # Pass time and update status

    def sleep(self):
        """NPC sleeps, does not consume meals."""
        #if self.sleep_timer == 25 and self.sleep_counter < 8:
            #self.sleep_counter += 1
            #self.tick()  # Sleep for 8 hours
        #else:
            #self.sleep_timer += 1
        if self.Current_Hour != self.Hour_of_current:
            self.sleep_timer += 1
            print("sleeping")
        self.state = "sleeping"
        # Simulate time passing
        #self.tick()

    def work(self,screen):
        """NPC works and earns income."""
        self.state = "working"
        # Simulate working hours
        if self.Current_Hour < 17:
            self.work_counter = 0
            #self.tick_counter += 1
        if self.Current_Hour == 17:
            self.working_hours = 0
            #self.tick_counter = 0
            self.finished_work = 1
            self.is_traveling = True
            self.reward = 10
            self.work_counter = 0
            print('finished working')
            self.state = "walking home"
        self.work_counter += 1
            #self.food_supply -= 1  # Works for 8 hours
        #self.income += self.calculate_income() 
        #print('working') # Earn income based on occupation
        # Update stress and health status based on occupation

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
                elif self.first_counter == 0:
                    self.first_counter = 1
                    #self.is_traveling = True
                #self.is_traveling == True

        if self.walk_counter == 200:
            #self.tick()
            self.walk_counter = 0
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
        

    #def do_q_learning_stuff(self, action, reward):
        #self.update_q_value(action, reward)

    def Draw_Points(self, screen):
        # Draw points
        for point, pos in Main_init.points.items():
            pg.draw.circle(screen, (0, 0, 0), pos, 5)
            font = pg.font.Font(None, 24)
            text = font.render(point, True, (0, 0, 0))
            screen.blit(text, (pos[0] + 10, pos[1] - 10))

    def Draw_current_pos(self, screen):
        pg.draw.circle(screen, (255, 0, 0), (int(self.current_position[0]), int(self.current_position[1])), 20)


    def update(self,screen):
        self.Draw_Points(screen)
        #print(self.success)
        if self.counter_timer == 1:
                self.persist_state == False
                # Perform the action and update Q-values & tick
                if self.is_alive == True:
                    #self.tick()
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
                            # Start traveling to work
                            if self.is_traveling == True and self.finished_work == 0:
                                self._walk(screen, self.work_location)
                            elif self.is_traveling == False and self.finished_work == 0:
                                    self.work(screen)
                            elif self.is_traveling == True and self.finished_work == 1:
                                self._walk(screen, self.house_location)
                            elif self.is_traveling == False and self.success == 1:
                                #self.actions = ['work', 'idle', 'sleep']
                                #print('here3')
                                self.update_q_value(self.action, self.reward)
                                self.finished_work = 0
                                self.first_counter = 0
                                self.work_cooldown = True
                                self.actions = ['idle', 'sleep']
                                self.action = None
                        elif self.action == 'idle':
                            self.idle()
                            self.reward = 0
                            self.update_q_value(self.action, self.reward)
                        elif self.action == 'sleep':
                            self.sleep()
                            self.reward = 0
                            self.update_q_value(self.action, self.reward)
                        #self.check_death()
                        #print('Data:',self.action ,self.is_traveling, self.first_counter)
                            #print(self.npc_position, self.hunger, self.emotional_state, self.health_status, self.state)
                else:
                    #print('NPC IS DEAD')
                    pass
                self.counter_timer = 0
        if self.persist_state == True:
            self.Draw_Points(screen)
            self.Draw_current_pos(screen)
            self.counter_timer += 1
            #self.persist_state = True
        self.check_death()

           


            

