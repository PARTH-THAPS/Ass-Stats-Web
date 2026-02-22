from scipy.stats import binom
import matplotlib.pyplot as plt

n = 1000
prob_incidence = 1/1000

k_values = [1, 2, 3]

# Compute probabilities
prob_of_exactly_k = [binom.pmf(k, n, prob_incidence) for k in k_values]
prob_of_fewer_than_k = [binom.cdf(k-1, n, prob_incidence) for k in k_values]

plt.figure(figsize=(10, 5))

plt.bar(k_values, prob_of_exactly_k, color="green")
plt.xlabel("k (Number of affected persons)")
plt.ylabel("Probability")
plt.title("Probability of exactly k affected persons")
plt.yscale('log')

plt.show()
