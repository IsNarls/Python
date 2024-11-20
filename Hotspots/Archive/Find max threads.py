import threading
import time


class NumberPrinter(threading.Thread):
    def __init__(self, args):
        self.counter = args[0]

    def run(self) -> None:
        time.sleep(5)
        print(f"Thread Name: {threading.current_thread().name}, Counter: {self.counter}")


if __name__ == '__main__':
    for i in range(10000000):
        number_printer = NumberPrinter(args=(i+1,))
        number_printer.start()