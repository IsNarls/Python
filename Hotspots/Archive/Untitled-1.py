def _walk(self,screen, destination):
            # Choose a new random destination if we don't have one or we've reached the current one
            # Use the NPC's current position as the starting point
            npc_position = next(point for point, pos in Main_init.points.items() if pos == self.current_position)
            available_points = list(Main_init.points.keys())
            #print(available_points)
            available_points.remove(npc_position)  # Exclude the current position

            # Ensure the destination is different from the current position
            self.destination = available_points[destination]  # Select a new destination
            self.path = self.bfs(npc_position, self.destination)  # Find the path to the new destination

        
        