import pygame
import random
from collections import deque

# Initialize Pygame
pygame.init()

# Set up display
width, height = 400, 300
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# Define points with coordinates
points = {
    'A1': (50, 50),
    'A2': (150, 50),
    'A3': (250, 50),
    'A4': (350, 50),
    'B1': (50, 100),
    'B2': (150, 100),
    'B3': (250, 100),
    'B4': (350, 100),
    'C1': (50, 150),
    'C2': (150, 150),
    'C3': (250, 150),
    'C4': (350, 150),
}

# Define adjacency (neighbors) for each point
neighbors = {
    'A1': ['A2', 'B1'],
    'A2': ['A1', 'A3', 'B2'],
    'A3': ['A2', 'A4', 'B3'],
    'A4': ['A3', 'B4'],
    'B1': ['A1', 'B2', 'C1'],
    'B2': ['A2', 'B1', 'B3', 'C2'],
    'B3': ['A3', 'B2', 'B4', 'C3'],
    'B4': ['A4', 'B3', 'C4'],
    'C1': ['B1', 'C2'],
    'C2': ['B2', 'C1', 'C3'],
    'C3': ['B3', 'C2', 'C4'],
    'C4': ['B4', 'C3'],
}

# BFS to find a path from start to goal
def bfs(start, goal):
    queue = deque([[start]])
    visited = {start}

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == goal:
            return path

        for neighbor in neighbors[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

    return None  # No path found

# Initialize NPC starting position and first destination
npc_position = 'A1'
current_position = points[npc_position]

# Main loop
running = True
path = []
destination = None

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Choose a new random destination if we don't have one or we've reached the current one
    if destination is None or current_position == points[destination]:
        print(destination, current_position, path)
        
        # Use the NPC's current position as the starting point
        npc_position = next(point for point, pos in points.items() if pos == current_position)

        available_points = list(points.keys())
        print(available_points)
        available_points.remove(npc_position)  # Exclude the current position

        # Ensure the destination is different from the current position
        if available_points:
            destination = random.choice(available_points)  # Select a new destination
            path = bfs(npc_position, destination)  # Find the path to the new destination

    # Clear screen
    screen.fill((255, 255, 255))

    # Draw points
    for point, pos in points.items():
        pygame.draw.circle(screen, (0, 0, 0), pos, 5)
        font = pygame.font.Font(None, 24)
        text = font.render(point, True, (0, 0, 0))
        screen.blit(text, (pos[0] + 10, pos[1] - 10))

    # Move to next point in the path
    if path and current_position:
        next_point = path[0]  # Get the next point in the path
        next_position = points[next_point]
        
        # Create a vector to the next point
        direction = pygame.math.Vector2(next_position) - pygame.math.Vector2(current_position)
        if direction.length() > 0:
            direction.normalize_ip()
            current_position = (current_position[0] + direction.x * 2, current_position[1] + direction.y * 2)

        # Check if we've reached the next point
        if pygame.math.Vector2(current_position).distance_to(next_position) < 2:
            current_position = next_position
            path.pop(0)  # Remove the reached point from the path

    # Draw current position
    if current_position:
        pygame.draw.circle(screen, (255, 0, 0), (int(current_position[0]), int(current_position[1])), 10)

    # Draw the destination point
    if destination:
        pygame.draw.circle(screen, (0, 255, 0), points[destination], 10)  # Destination in green
    #print(destination,current_position,path)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
