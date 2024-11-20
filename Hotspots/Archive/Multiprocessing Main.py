#multishitshowV2
import multiprocessing
from multiprocessing import Process, Queue, Lock
import yfinance as yf
import time
import time
import yfinance as yf
from collections import deque
import pygame as pg
import math 
import random
import Mark_Time
from multiprocessing import Lock
import NPC_Crim_init

main_counter = 0
file_lock = Lock()

            
#person = NPC_Crime()
def worker():
    person = NPC_Crim_init.NPC_Crime()
    person.update()
   
def main():
    #low processes WORKING
    length = 60
    # Create a multiprocessing pool with the specified number of processes
    pool = multiprocessing.Pool(processes=length)

    # Start the NPC_Crime instances
    for i in range(length):
        person = worker()
        pool.apply_async(person.update)

    # Keep the main process alive
    try:
        while True:
            time.sleep(1)  # Adjust sleep as necessary for your needs
    except KeyboardInterrupt:
        pool.terminate()
        pool.join()

if __name__ == "__main__":
    main()
    





















