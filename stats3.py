from scipy.stats import binom

# Probability Of 9 Heads in 10
prob_of_9_heads_in_10 = binom.pmf(9, 10, 0.5)

# Probability Of 18 heads in 20
probs_of_18_heads_in_20 = binom.pmf(18, 20, 0.5)

# Probaility Of getting heads more than 18 times in 20
prob_of_more_than_18_heads_in_20 = binom.sf(18, 20, 0.5)


print(prob_of_more_than_18_heads_in_20)
