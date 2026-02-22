import numpy as np
import matplotlib.pyplot as plt

B = 5000
n_values = [1, 5, 25, 100, 10000]

for n in n_values:
    means = []

    for _ in range(B):
        sample = np.random.uniform(0, 1, n)
        means.append(np.mean(sample))

    plt.figure()
    plt.hist(means, bins=30, density=True)
    plt.title(f"Sampling Distribution of Mean (n={n})")
    plt.xlabel("Sample Mean")
    plt.ylabel("Density")
    plt.show()
