from threading import Thread
import os
import time


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


threads = []
num_threads = 4

accuracy = 1
for i in range(num_threads):
    t = Thread(target=compute_pi, args=(accuracy,))
    accuracy *= 100
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()
