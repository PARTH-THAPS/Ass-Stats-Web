import random
import numpy as np
import matplotlib.pyplot as plt


def binomial_random(p, n, repetitions):

    results = []

    for i in range(repetitions):
        heads = 0

        for j in range(n):
            if random.random() < p:
                heads += 1

        results.append(heads)

    average_x = np.mean(results)
    theoretical_np = n * p

    return results, average_x, theoretical_np


# Example usage
p = 0.3
n = 20
repetitions = 1000

results, avg, theoretical = binomial_random(p, n, repetitions)

print("Simulated Mean:", avg)
print("Theoretical Mean:", theoretical)
