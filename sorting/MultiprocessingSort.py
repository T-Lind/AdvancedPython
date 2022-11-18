import random
import time
from multiprocessing import Process, Array

def is_sorted(array):
    prev = -2_147_483_647
    for item in array:
        if item > prev:
            prev = item
        else:
            return False
    return True

def sort(*args):
    return sorted(args)


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


if __name__ == '__main__':
    max = 2_147_483_647
    items = 1_000_000
    array = Array('i', [random.randint(-2_147_483_647, 2_147_483_647) for _ in range(items)])
    third = items // 3
    p1 = Process(target=sort, args=(array))
    # p2 = Process(target=sort, args=(array[third:2 * third]))
    # p3 = Process(target=sort, args=(array[2 * third:]))

    timer = Timer()
    p1.start()
    # p2.start()
    # p3.start()

    p1.join()
    # p2.join()
    # p3.join()
    timer.stop()

    print(is_sorted(array))
