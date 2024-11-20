#start scripts
import os
import time




def start_Clock():
    os.startfile(r"C:\Users\narwh\Documents\Pythonshit\Hotspots\Clock.py")
def start_Multithreading():
    os.startfile(r"C:\Users\narwh\Documents\Pythonshit\Hotspots\Main_Multi_Thread_Processing.py")
def start_Main():
    os.startfile(r"C:\Users\narwh\Documents\Pythonshit\Hotspots\Main_init.py")

def start_script():
    start_Clock()
    time.sleep(1)
    start_Multithreading()
    time.sleep(5)
    start_Main()
    
    #time.sleep(5)
    


start_script()    