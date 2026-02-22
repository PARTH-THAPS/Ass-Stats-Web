import numpy as np
from scipy.stats import norm, cauchy, bernoulli, expon
import matplotlib.pyplot as plt

n_max = 10000

# Case 1: Normal(0,1)

x_normal = np.random.normal(0, 1, n_max)
print(x_normal)
Xn_normal = np.cumsum(x_normal)/np.arange(1, n_max+1)

x_cauchy = np.random.standard_cauchy(n_max)
Xn_Cauchy = np.cumsum(x_cauchy)/np.arange(1, n_max+1)

plt.figure(figsize=(14, 6))
plt.subplot(1, 2, 1)
plt.plot(np.arange(1, n_max+1), Xn_normal)
plt.title("Sample mean Xn vs n For Normal(0,1)")
plt.xlabel('n')
plt.ylabel("Xn")
plt.grid(True)


plt.subplot(1, 2, 2)
plt.plot(np.arange(1, n_max+1), Xn_Cauchy)
plt.title("Sample mean Xn vs n For Cauchy(0,1)")
plt.xlabel('n')
plt.ylabel("Xn")
plt.grid(True)


plt.tight_layout()
plt.show()
