import threading
import time

class Semaphore:
    def __init__(self, initial_value=1):
        self.value = initial_value
        self.lock = threading.Lock()

    def wait(self):
        with self.lock:
            while self.value <= 0:
                pass
            self.value -= 1

    def signal(self):
        with self.lock:
            self.value += 1

NUM_PHILOSOPHERS = 5
chopsticks = [Semaphore(1) for _ in range(NUM_PHILOSOPHERS)]
philosopher_status = ["thinking"] * NUM_PHILOSOPHERS
cycles_completed = 0

def philosopher(id):
    global cycles_completed
    while cycles_completed < 10:
        think(id)
        dine(id)
        cycles_completed += 1

def think(id):
    philosopher_status[id] = "thinking"
    print_status()
    time.sleep(2)

def dine(id):
    left_chopstick = id
    right_chopstick = (id + 1) % NUM_PHILOSOPHERS
    if chopsticks[left_chopstick].value > 0 and chopsticks[right_chopstick].value > 0:
        chopsticks[left_chopstick].wait()
        chopsticks[right_chopstick].wait()
        philosopher_status[id] = "eating"
        print_status()
        time.sleep(1)
        chopsticks[left_chopstick].signal()
        chopsticks[right_chopstick].signal()
    else:
        philosopher_status[id] = "hungry"
        print_status()

def print_status():
    for i in range(NUM_PHILOSOPHERS):
        print(f'Philosopher {i} is {philosopher_status[i]}')
    print()

if __name__ == "__main__":
    philosophers = []
    for i in range(NUM_PHILOSOPHERS):
        philosopher_thread = threading.Thread(target=philosopher, args=(i,))
        philosopher_thread.start()
        philosophers.append(philosopher_thread)

    for philosopher_thread in philosophers:
        philosopher_thread.join()