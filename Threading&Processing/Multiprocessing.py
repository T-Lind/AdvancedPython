import time
from multiprocessing import Process, Value, Array, Lock, Pool
import os


class Timer:
    """
    Simple timer object to measure the length of time things take
    """

    def __init__(self):
        self.end = 0
        self.start = time.time()

    def stop(self):
        self.end = time.time()
        print("Time:", self.end - self.start)


def add_100(number: Value, lock: Lock):
    for i in range(100):
        # Just acting as an operation that takes some time
        time.sleep(0.01)
        with lock:  # Use context manager instead of lock.acquire() and lock.release()
            number.value += 1


def add_100_array(array: Array, lock: Lock):
    for i in range(100):
        time.sleep(0.01)

        # CANNOT use a regular for loop for the array! Creates a local copy

        with lock:
            for i in range(len(array)):
                array[i] += 1


def cube(number):
    return number ** 3


if __name__ == '__main__':
    lock = Lock()

    # Shared number here
    print("Shared value:")

    shared_number = Value('i', 0)  # 'i' for integer and a starting value of zero, 'd' for double
    print("Original number is", shared_number.value)

    p1 = Process(target=add_100, args=(shared_number, lock))
    p2 = Process(target=add_100, args=(shared_number, lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Number at end is", shared_number.value, "should be 200")  # Without any locks this value can be inaccurate!

    print("Shared array:")

    shared_array = Array('d', [0.0, 100.0, 200.0])  # Provide a data type and list for the sharred array object

    print("Shared array at beginning is",
          shared_array[:])  # Must use the colon otherwise it will not return the list datatype

    # Use the two processes to increase each element in the array by 200 total
    p1 = Process(target=add_100_array, args=(shared_array, lock))
    p2 = Process(target=add_100_array, args=(shared_array, lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Shared array at end is",
          shared_array[:])  # Must use the colon otherwise it will not return the list datatype

    # Create a list of numbers 0-1000 and compare the performance of the regular method of cubing to multithreading
    # Only saves time when numbers > 7m (roughly) as starting threads is costly
    numbers = range(10000000)

    # Use a pool to divide a task among all the CPUs and combine the result

    # Time it
    timer1 = Timer()


    pool = Pool()
    result = pool.map(cube, numbers)
    # pool.apply(cube, numbers[0])  # Only interact with one element in the iterable

    pool.close()
    pool.join()

    # Stop the timer
    timer1.stop()

    # Now ordinarily cube the numbers
    timer2 = Timer()

    list_result = []
    for item in numbers:
        list_result.append(cube(item))

    timer2.stop()
