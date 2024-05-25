import threading
import time

BUFFER_SIZE = 5
MAX_NUMBER = 25

empty = threading.Semaphore(BUFFER_SIZE)
full = threading.Semaphore(0)
mutex = threading.Semaphore(1)

buffer = []

def producer():
    for item in range(1, MAX_NUMBER + 1):
        empty.acquire()
        mutex.acquire()
        buffer.append(item)
        print(f"Produced: {item}")
        mutex.release()
        full.release()
        time.sleep(0.1)

def consumer():
    for _ in range(MAX_NUMBER):
        full.acquire()
        mutex.acquire()
        item = buffer.pop(0)
        print(f"Consumed: {item}")
        mutex.release()
        empty.release()
        time.sleep(0.1)

producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

producer_thread.start()
consumer_thread.start()

producer_thread.join()
consumer_thread.join()
