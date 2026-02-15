import random
import matplotlib.pyplot as plt


def simulate_coin(p, n):
    heads = 0
    proportions = []

    for i in range(1, n+1):
        if random.random() < p:
            heads += 1
        proportions.append(heads / i)

    return proportions


n = 1000

p1 = 0.3
proportions1 = simulate_coin(p1, n)

plt.figure()
plt.plot(range(1, n+1), proportions1)

plt.xlabel("Number Of Flips (n)")
plt.ylabel("Proportion Of Heads")
plt.title("Proportion Of Heads Vs Number Of Flips (p = 0.3)")
plt.show()
