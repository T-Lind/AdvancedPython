from queue import Queue
import time
from threading import Thread, Lock, current_thread

def worker(q: Queue, lock: Lock):
    while True:  # Continue going through the queue
        value = q.get()

        # Processing
        with lock:
            print(f'in {current_thread().name} got {value}')

        q.task_done()  # Finishes the thread and exits the while True loop

if __name__ == '__main__':
    queue = Queue()
    lock = Lock()

    num_threads = 10

    for i in range(num_threads):
        thread = Thread(target=worker, args=(queue, lock))
        thread.daemon = True  # Background thread that will die when the main thread dies
        thread.start()

    for i in range(1, 21):
        queue.put(i)

    queue.join()
