import threading
import multiprocessing
import time
import NPC_Crim_init
import os


# Constantss
total_instances = 200 #120  # Total instances to run
threads_per_process =  10  # Number of threads per process (you can adjust this)

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
        print(f"All files have been deleted from {directory}.")
    else:
        print(f"The specified directory {directory} does not exist.")


def worker():
    """Worker function that performs the task using threads."""
    person = NPC_Crim_init.NPC_Crime()
    person.update()


def thread_worker(start_index, total_threads):
    """Run a batch of threads within a process."""
    threads = []
    for _ in range(start_index, total_threads):
        thread = threading.Thread(target=worker)
        thread.start()
        threads.append(thread)

    # Wait for all threads in this process to complete
    for thread in threads:
        thread.join()


def process_worker(start_index, end_index):
    """Run the multiprocessing worker."""
    # Spawn multiple threads in this process
    thread_worker(start_index, end_index)


def main():
    # Delete all files in directories first
    delete_all_files_in_directory(NPC_data_dir)
    delete_all_files_in_directory(NPC_loc_data_dir)
    delete_all_files_in_directory(NPC_consent_data_dir)

    # Determine number of processes and threads per process
    processes = []
    num_processes = total_instances // threads_per_process

    # Create multiprocessing processes
    for i in range(num_processes):
        start_index = i * threads_per_process
        end_index = start_index + threads_per_process
        process = multiprocessing.Process(target=process_worker, args=(start_index, end_index))
        processes.append(process)

    # Start all processes
    for process in processes:
        process.start()

    # Wait for all processes to complete
    for process in processes:
        process.join()


if __name__ == "__main__":
    main()
