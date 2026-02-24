import numpy as np
import matplotlib.pyplot as plt


X = np.random.seed(42)

n = 20

X = np.random.normal(0, 1, n)
Y = np.random.normal(0, 2, n)
Z = np.random.normal(0, np.sqrt(3), n)


# Pearson Corelations
corr_XY = np.corrcoef(X, Y)[0, 1]
corr_XZ = np.corrcoef(X, Z)[0, 1]
corr_YZ = np.corrcoef(Y, Z)[0, 1]


print("Sample Correlations n:20")
print("Corr(X,Y)=", corr_XY)
print("Corr(Y,Z)=", corr_YZ)
print("Corr(X,Z)=", corr_XZ)


U = X/Z
V = Y/Z

corr_UV = np.corrcoef(U, V)[0, 1]
print("Corr (U,V)=", corr_UV)


plt.figure()
plt.scatter(U, V)
plt.xlabel("U=X/Z")
plt.ylabel("V=Y/Z")
plt.title("Scatter Plot of U vs V")
plt.show()

s = 1000
corrs_XY = []
corrs_UV = []

for i in range(s):
    Xs = np.random.normal(0, 1, n)
    Ys = np.random.normal(2, 2, n)
    Zs = np.random.normal(2, np.sqrt(3), n)

    corrs_XY.append(np.corrcoef(Xs, Ys)[0, 1])

    Us = Xs/Zs
    Vs = Ys/Zs
    corrs_UV.append(np.corrcoef(Us, Vs)[0, 1])

corrs_UV = np.array(corrs_UV)
corrs_XY = np.array(corrs_XY)


plt.figure
plt.hist(corrs_UV, bins=30)
plt.xlabel("Corrlation")
plt.ylabel("Frequency")
plt.title("Histogram Of Corr(X,Y)")
plt.show()


plt.figure
plt.hist(corrs_XY, bins=30)
plt.xlabel("Corrlation")
plt.ylabel("Frequency")
plt.title("Histogram Of Corr(X,Y)")
plt.show()


count_XY_pos = np.sum(corrs_XY > 0.3)
count_XY_neg = np.sum(corrs_XY < - 0.3)

count_UV_pos = np.sum(corrs_UV > 0.3)
count_UV_neg = np.sum(corrs_UV < -0.3)


plt.figure()
plt.boxplot(corrs_XY)
plt.ylabel("correlaton")
plt.title("Boxplot Of Corr(X,Y)")
plt.show()
