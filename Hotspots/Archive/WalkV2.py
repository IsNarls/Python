import random
from collections import deque


Waypoints = {
    'W1': (255.0, 1300.0),
    'W2': (395.0, 1165.0),
    'W3': (585.0, 975.0),
    'W4': (760.0, 765.0),
    'W5': (935.0, 565.0),
    'W6': (1155.0, 360.0),
    'W7': (1335.0, 180.0),
    'W8': (1465.0, 50.0),
    'W9': (1635.0, 90.0),
    'W10': (1795.0, 230.0),
    'W11': (1975.0, 350.0),
}

neighbors = {
    'W1': ['W2', 'W6'],      # W1 is near W2 and W6
    'W2': ['W1', 'W3', 'W6'],  # W2 is near W1, W3, and W6
    'W3': ['W2', 'W4', 'W6'],  # W3 is near W2, W4, and W6
    'W4': ['W3', 'W5', 'W6'],  # W4 is near W3, W5, and W6
    'W5': ['W4', 'W6', 'W7'],  # W5 is near W4, W6, and W7
    'W6': ['W1', 'W2', 'W3', 'W4', 'W5', 'W7'],  # W6 connects many points
    'W7': ['W5', 'W6', 'W8'],  # W7 is near W5, W6, and W8
    'W8': ['W7', 'W9'],      # W8 is near W7 and W9
    'W9': ['W8', 'W10'],     # W9 is near W8 and W10
    'W10': ['W9', 'W11'],    # W10 is near W9 and W11
    'W11': ['W10'],          # W11 is near W10
}
HouseWaypoints = {
    'H1': (295.0, 1140.0),
    'H2': (490.0, 930.0),
    'H3': (675.0, 715.0),
    'H4': (850.0, 500.0),
    'H5': (1045.0, 315.0),
    'H6': (1235.0, 120.0),
    'H7': (1380.0, 30.0),
    'H8': (1690.0, 60.0),
    'H9': (1805.0, 145.0),
}

points = Waypoints + HouseWaypoints
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

# Main loop
running = True
path = []
destination = None

def walk(self):
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

    # Draw points
    for point, pos in points.items():
        pg.draw.circle(self.screen, (0, 0, 0), pos, 5)
        font = pg.font.Font(None, 24)
        text = font.render(point, True, (0, 0, 0))
        self.screen.blit(text, (pos[0] + 10, pos[1] - 10))

    # Move to next point in the path
    if path and current_position:
        next_point = path[0]  # Get the next point in the path
        next_position = points[next_point]
        
        # Create a vector to the next point
        direction = pg.math.Vector2(next_position) - pg.math.Vector2(current_position)
        if direction.length() > 0:
            direction.normalize_ip()
            current_position = (current_position[0] + direction.x * 2, current_position[1] + direction.y * 2)

        # Check if we've reached the next point
        if pg.math.Vector2(current_position).distance_to(next_position) < 2:
            current_position = next_position
            path.pop(0)  # Remove the reached point from the path

    # Draw current position
    if current_position:
        pg.draw.circle(self.screen, (255, 0, 0), (int(current_position[0]), int(current_position[1])), 10)

    # Draw the destination point
    if destination:
        pg.draw.circle(self.screen, (0, 255, 0), points[destination], 10)  # Destination in green
    
