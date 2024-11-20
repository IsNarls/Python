#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <dirent.h>

#define MAX_PATH 1024
#define MAX_LINE_LENGTH 512
#define MAX_FILE_NAME_LENGTH 256
#define MAX_LOCATIONS 100

// Struct to store a location and its neighbors
typedef struct {
    char location[MAX_LINE_LENGTH];  // NPC location (e.g., H6)
    char neighbors[MAX_LOCATIONS][MAX_FILE_NAME_LENGTH]; // Neighboring file names
    int neighbor_count;
} Location;

// Function to read a file and return the content as a string
int read_file(const char *file_path, char lines[MAX_LOCATIONS][MAX_LINE_LENGTH]) {
    FILE *file = fopen(file_path, "r");
    if (file == NULL) {
        perror("Failed to open file");
        return -1;
    }

    int line_count = 0;
    while (fgets(lines[line_count], MAX_LINE_LENGTH, file) != NULL) {
        // Strip newline character
        lines[line_count][strcspn(lines[line_count], "\n")] = 0;
        line_count++;
    }
    fclose(file);
    return line_count;
}

// Function to look around and populate neighbor information
void look_around(const char *folder_path, const char *npc_name, Location *locations, int *location_count) {
    struct dirent *entry;
    DIR *dir = opendir(folder_path);

    if (dir == NULL) {
        perror("Failed to open directory");
        return;
    }

    char npc_location[MAX_LINE_LENGTH][MAX_LINE_LENGTH];
    int npc_location_lines = 0;
    
    // Loop through all files in the directory
    while ((entry = readdir(dir)) != NULL) {
        // Skip directories (e.g., . and ..)
        if (entry->d_type == DT_DIR) {
            continue;
        }

        // Get the NPC name from the file name (before the dot)
        char file_name[MAX_FILE_NAME_LENGTH];
        strncpy(file_name, entry->d_name, MAX_FILE_NAME_LENGTH);
        file_name[MAX_FILE_NAME_LENGTH - 1] = '\0';  // Ensure null-termination
        char *dot_pos = strchr(file_name, '.');
        if (dot_pos != NULL) {
            *dot_pos = '\0';  // Remove file extension
        }

        // If the NPC name matches, read its location
        if (strcmp(file_name, npc_name) == 0) {
            char file_path[MAX_PATH];
            snprintf(file_path, MAX_PATH, "%s/%s", folder_path, entry->d_name);
            npc_location_lines = read_file(file_path, npc_location);
        } else {
            // Read neighbor's location
            char neighbor_lines[MAX_LOCATIONS][MAX_LINE_LENGTH];
            char file_path[MAX_PATH];
            snprintf(file_path, MAX_PATH, "%s/%s", folder_path, entry->d_name);
            int neighbor_lines_count = read_file(file_path, neighbor_lines);
            
            if (neighbor_lines_count > 0) {
                // Check if the location matches the NPC location
                if (strcmp(neighbor_lines[0], npc_location[0]) == 0) {
                    // Store the neighbor in the list
                    strcpy(locations[*location_count].location, npc_location[0]);
                    strcpy(locations[*location_count].neighbors[locations[*location_count].neighbor_count], entry->d_name);
                    locations[*location_count].neighbor_count++;
                }
            }
        }
    }

    closedir(dir);
}

int main() {
    const char *folder_path = "C:\\Users\\narwh\\Documents\\Pythonshit\\Hotspots\\Support Files\\NPC_Location";
    const char *npc_name = "416735";  // Example NPC name
    
    Location locations[MAX_LOCATIONS];
    int location_count = 0;

    // Call the function to look around and gather neighbor info
    look_around(folder_path, npc_name, locations, &location_count);

    // Print the collected neighbors information
    for (int i = 0; i < location_count; i++) {
        printf("Location: %s\n", locations[i].location);
        printf("Neighbors:\n");
        for (int j = 0; j < locations[i].neighbor_count; j++) {
            printf("\t%s\n", locations[i].neighbors[j]);
        }
    }

    return 0;
}
