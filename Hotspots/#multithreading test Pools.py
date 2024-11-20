#multithreading test Pools
import threading
import time
import NPC_Crim_init
import os
from concurrent.futures import ThreadPoolExecutor

total_instances = 300  # Total instances to run (increased to 300)
max_threads = 120      # Limit the number of concurrent threads

NPC_data_dir = r"C:\Users\narwh\Documents\Pythonshit\Hotspots\Support Files\NPC_DATA"

def delete_all_files_in_directory(directory):
    """
    Deletes all files in the specified directory.

    :param directory: The path of the directory from which to delete files.
    """
    if os.path.exists(directory):
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)  # Delete the file
        print("All files have been deleted.")
    else:
        print("The specified directory does not exist.")

delete_all_files_in_directory(NPC_data_dir)

def worker():
    person = NPC_Crim_init.NPC_Crime()
    person.update()

def main():
    # Use ThreadPoolExecutor to limit the number of concurrent threads
    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        # Submit tasks to the thread pool
        for _ in range(total_instances):
            executor.submit(worker)

if __name__ == "__main__":
    main()
