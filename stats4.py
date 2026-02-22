from scipy.stats import binom

n = 100000
p = 1/100000
ks = [1, 2, 3, 4]


for k in ks:
    prob_exact = binom.pmf(k, n, p)
    prob_less = binom.cdf(k-1, n, p)
    print(f"{k} \t {prob_exact} \t {prob_less}  ")
