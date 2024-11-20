# Original list of waypoints
Waypoints = ['S95', (2560.0, 880.0), 'S96', (2660.0, 930.0), 'S97', (2760.0, 745.0), 'S98', (1980.0, 1560.0), 'S99', (2400.0, 1755.0), 'S100', (2800.0, 2010.0)]
# Initialize an empty dictionary to store the result
waypoints_dict = {}

# Iterate through the list in steps of 2
for i in range(0, len(Waypoints), 2):
    waypoint_name = Waypoints[i]  # Name of the waypoint
    coordinates = Waypoints[i+1]  # Coordinates of the waypoint
    waypoints_dict[waypoint_name] = coordinates

# Print the result
print(waypoints_dict)