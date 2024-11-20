if self.counter_timer == 100:    
                # Perform the action and update Q-values
                if self.is_alive == True:
                    #update passage of time
                    self.tick()
                    # Choose an action
                    action = self.choose_action()
                    if action == 'idle':
                        #print('idling')
                        self.idle()
                        #reward = -1  # Negative reward for idling
                    elif action == 'work':
                        self._walk(self,screen, self.work_location)
                        # Start traveling to work
                        if self.is_traveling = True:
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





def do_q_learning_stuff():
    self.update_q_value(action, self.reward)

if self.counter_timer == 100:    
                # Perform the action and update Q-values & tick
                if self.is_alive == True:
                    self.tick()
                    # Choose an action
                    if self.action_lock == False:
                        action = self.choose_action()
                        if action == 'work':
                            # Start traveling to work
                            self.is_traveling == True
                            self.start_travel_to_work(self,screen)
                        self.update_q_value(action, self.reward)
                        # Here you can include your walking logic
                        #self._walk(screen, self.destination)
                        self.check_death()
                    elif self.action_lock == True:
                        if action == 'work':
                            # Start traveling to work
                            self.is_traveling == True
                            self.start_travel_to_work(self,screen)
                        self.check_death()
                else:
                    print('NPC IS DEAD')
                self.counter_timer = 0
        else:
            self.counter_timer += 1