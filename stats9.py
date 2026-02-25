import numpy as np
from scipy.stats import bernoulli
from tqdm import tqdm
import matplotlib.pyplot as plt

alpha = 0.05
p = 0.4
B = 50000
N = 10000


num = np.arange(1, N+1)
eppisoln_n = np.sqrt((1/(2*num))*np.log(2/alpha))

p_hat = np.empty((B, N))


for i in tqdm(range(B)):
    X = bernoulli.rvs(p, N, random_state=i)
    p_hat[i] = np.cumsum(X)/num


coverage = np.mean((p_hat + eppisoln_n >= p) &
                   (p_hat - eppisoln_n <= p), axis=0)


plt.figure(figsize=(12, 8))
plt.plot(num, coverage)
plt.xlabel('n')
plt.ylabel('Coverage')
plt.show()


plt.figure(figsize=(12, 8))
plt.plot(num, 2 * eppisoln_n, label='Interval length')
plt.xlabel('n')
plt.ylabel(r'$2\eppisoln_n$')
plt.hlines(.05, xmin=0, xmax=N, color='red', label='Threshold')
plt.yscale('log')
plt.legend(loc='upper right')
plt.show()
