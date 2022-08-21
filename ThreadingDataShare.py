import multiprocessing
from multiprocessing import Process
import os

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