import time
from threading import Thread, Lock  # Locks prevent two functions from accessing the same variables at the same time

# Store the pi data
pi_stored = []

# Store a value
database_value = 0


def compute_pi(iterations):
    """
    A simple function to compute pi given a certain amount of iterations
    :param iterations: The number of times to repeat the calculations
    """
    global pi_stored  # Use between multiple threads
    # Initialize denominator
    k = 1

    # Initialize sum
    pi_sum = 0

    for i in range(int(iterations)):
        # even index elements are positive
        if i % 2 == 0:
            pi_sum += 4 / k
        else:
            # odd index elements are negative
            pi_sum -= 4 / k
        # denominator is odd
        k += 2
    pi_stored.append(pi_sum)


def increase(lock: Lock):
    """
    Write a value to a global variable - demonstrate locks
    """
    global database_value

    with lock:  # Could also do lock.acquire() and lock.release() but context manager makes it happen automatically
        local_copy = database_value
        local_copy += 1
        time.sleep(0.1)
        database_value = local_copy


threads = []
increments = 4

# Change condition to run this - example with getting data back in the form of a list with varying iterations on pi
if __name__ == '__main__' and False:

    # Create threads with an additional x100 iterations with each increment
    iterations = 10
    for i in range(increments):
        threads.append(Thread(target=compute_pi, args=(iterations,)))
        iterations *= 100

    for t in threads:
        t.start()

    # Wait for all threads to complete
    for t in threads:
        t.join()

    print(pi_stored)

if __name__ == '__main__':
    lock = Lock()

    print("Start value:", database_value)

    thread1 = Thread(target=increase, args=(lock,))
    thread2 = Thread(target=increase, args=(lock,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("End value:", database_value)  # Without locks the database value will be 1 - NOT 2
