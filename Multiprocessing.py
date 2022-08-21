import multiprocessing
from multiprocessing import Process
import os

# Process: An instance of a program
# - Uses multiple CPUs and cores
# - Separate memory space, memory is not shared between processes
# - Interruptable/killable
# - Starting a process is slower than starting a thread
# - IPC (inter process communication) is more complicated

# Thread: Entity within a process that can be scheduled (known as a lightweight process)
# - A process can spawn multiple threads
# - Starting a thread is faster than a process
# - Great for I/O bound tasks
# - Careful with race conditions (changing the same variable at the same time in multiple threads)

# Global Interpreter Lock: GIL
# - Only allows one thread at a time to execute in python
# - Memory management is not thread-safe in CPython


# Multiprocessing:

# Example functions
processes = []
num_processes = os.cpu_count()
pi = []

def compute_pi(iterations):
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
    print(pi_sum)

def worker(q: multiprocessing.Queue):
    q.get()  # Runs the method


if __name__ == '__main__':  # This line is needed! Tells PyCharm this is the main thread
    queue = multiprocessing.Queue()

    # Create process
    for i in range(num_processes):
        p = Process(target=worker, args=(queue,))  # Create a new process object to calculate digits of pi in a
        # thread - args must be given a tuple (hence the comma)
        processes.append(p)

    for p in processes:
        # Start process
        p.start()

    # Compute pi to varying degrees of accuracy
    queue.put(compute_pi(100))
    queue.put(compute_pi(10000))
    queue.put(compute_pi(1000000))
    queue.put(compute_pi(100000000))

    # Wait for all processes to finish
    for p in processes:
        # Start process
        p.join()
