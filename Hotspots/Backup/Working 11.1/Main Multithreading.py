import threading
import time
import NPC_Crim_init

total_instances = 500  # Total instances to run
threads = []          # List to hold thread references

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