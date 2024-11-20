import threading
import time
import NPC_Crim_init
import os



total_instances = 120 #120  # Total instances to run
threads = []        # List to hold thread references

NPC_data_dir = r"C:\Users\narwh\Documents\Pythonshit\Hotspots\Support Files\NPC_DATA"
NPC_loc_data_dir = r"C:\Users\narwh\Documents\Pythonshit\Hotspots\Support Files\NPC_Location"
NPC_consent_data_dir = r"C:\Users\narwh\Documents\Pythonshit\Hotspots\Support Files\NPC_Consent"


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
delete_all_files_in_directory(NPC_loc_data_dir)
delete_all_files_in_directory(NPC_consent_data_dir)

def worker():
    person = NPC_Crim_init.NPC_Crime()
    person.update()


def main():
    # Create and start threads
    for _ in range(total_instances):
        thread = threading.Thread(target=worker)
        thread.start()
        threads.append(thread)

    # Optionally, wait for all threads to complete
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
    
 
    