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
        # Initialize NPC starting position and first destination
        self.npc_position = 'W1' 
        self.current_position = Main_init.points[self.npc_position]
        self.age = 24
        self.gender = 'Male'
        self.race = 'white'
        self.occupation = 'Janitor'
        self.work_location = 'H9'
        self.Grocery_location = 'H8'

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
        self.state = "idle"         # idle, sleeping, walking, working

        # Q-learning attributes
        self.q_table = {}  # Q-table to store Q-values
        self.learning_rate = 0.1
        self.discount_factor = 0.9
        self.exploration_rate = 1.0
        self.exploration_decay = 0.99
        self.min_exploration_rate = 0.1
        
        # Actions
        self.actions = ['idle', 'walk', 'sleep']  #'work',
       
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

    def tick(self):
        """Simulate the passage of time."""
        self.age += 1  # Increase age over time
        self.hunger += 1  # Hunger increases over time
        if self.hunger > 100:
            self.hunger = 100  # Cap hunger at 100
        #self.check_death()  # Check for death due to hunger

    def check_death(self):
        """Check if the NPC has died."""
        if self.hunger == 100:
            self.health_status = self.health_status - 1
        if self.hunger == 100 and self.health_status <= 0:
            self.is_alive = False
            print("they are dead")

    def idle(self):
        """NPC stays at home and consumes meals."""
        if self.food_supply > -6:
            self.food_supply -= 1  # Consume one meal
            # Simulate 4 hours passing in-game
            self.tick()  # Pass time and update status

    def go_to_store(self):
        """NPC stays at home and consumes meals."""
        if self.food_supply > -6:
            self.food_supply -= 1  # Consume one meal
            # Simulate 4 hours passing in-game
            self.tick()  # Pass time and update status
    def sleep(self):
        """NPC sleeps, does not consume meals."""
        self.sleep_counter += 8  # Sleep for 8 hours
        # Simulate time passing
        self.tick()

    def walk_to_work(self):
        """Trigger walking to work."""
        self.state = "walking"
        # Logic for walking duration and reaching work

    def work(self,screen):
        """NPC works and earns income."""
        self.state = "working"
        self._walk(screen, self.work_location)
        # Simulate working hours
        self.working_hours += 8
        self.food_supply -= 1  # Works for 8 hours
        self.income += self.calculate_income()  # Earn income based on occupation
        # Update stress and health status based on occupation
    
    def start_travel_to_work(self):
        self.is_traveling = True
        self.travel_ticks = 0  # Reset travel ticks
        # Set destination coordinates or logic for work location

    def return_home(self):
        """Returns home and enters idle state."""
        self.state = "idle"
        self.idle()

    def calculate_income(self):
        """Determine income based on occupation."""
        # Placeholder for actual income calculation based on occupation
        return 100  # Example fixed income
 
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
                self.path = self.bfs(npc_position, self.destination)  # Find the path to the new destination

        # Draw points
        for point, pos in Main_init.points.items():
            pg.draw.circle(screen, (0, 0, 0), pos, 5)
            font = pg.font.Font(None, 24)
            text = font.render(point, True, (0, 0, 0))
            screen.blit(text, (pos[0] + 10, pos[1] - 10))

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

        # Draw current position
        if self.current_position:
            pg.draw.circle(screen, (255, 0, 0), (int(self.current_position[0]), int(self.current_position[1])), 20)

        # Draw the destination point
        if self.destination:
            pg.draw.circle(screen, (0, 255, 0), Main_init.points[self.destination], 10)  # Destination in green
        
    def finish_work(self):
        self.is_traveling = True  # Now travel back home
        self.travel_ticks = 0 

    def update(self,screen):
        if self.counter_timer == 100:    
                self.tick()
                # Perform the action and update Q-values
                if self.is_alive == True:
                    # Choose an action
                    action = self.choose_action()
                    if action == 'idle':
                        #print('idling')
                        self.idle()
                        #reward = -1  # Negative reward for idling
                    #elif action == 'walk':
                        #print('walking')
                        #self.walk_to_work() 
                        #reward = 0  # Neutral reward for walking
                    elif action == 'work':
                        # Start traveling to work
                        if not self.is_traveling:
                            self._walk(self,screen, self.work_location)
                            reward = 0  # No reward for starting travel
                        else:
                            # If already traveling, continue until reaching the destination
                            if self._walk(self,screen, self.work_location):
                                # Once arrived, work for the required ticks
                                self.work(screen)
                                if self.work_ticks < self.WORK_DURATION:
                                    reward = 0  # No reward for just working
                                else:
                                    # Finished working
                                    self.finish_work()
                                    reward = 10  # Positive reward for completing work 
                        #print('working')
                        #self.work(screen)
                        #reward = 10  # Positive reward for working
                    elif action == 'sleep':
                        #print('sleeping')
                        self.sleep()
                        reward = -2  # Negative reward for sleeping too much
                    # Update Q-value based on the action taken and reward received
                    self.update_q_value(action, reward)
                    # Here you can include your walking logic
                    #self._walk(screen, self.destination)
                    self.check_death()
                else:
                    print('NPC IS DEAD')
                self.counter_timer = 0
        else:
            self.counter_timer += 1

            

