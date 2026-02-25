import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st
import pandas as pd


data_upload = pd.read_csv(
    "/Users/user/Downloads/Potassium_Konzent.csv", sep=";")
n = len(data_upload)

print(data_upload.columns)

mean = np.mean(data_upload["x"])
sd = np.std(data_upload["x"], ddof=1)
print(sd)

se = sd / np.sqrt(n)

print('mean:', mean)
print('sdt:', sd)
print('se:', se)


def ci_exact(mean, se, df, alpha):
    tcrit = st.t.ppf(1 - alpha/2, df)
    return mean - tcrit * se, mean + tcrit * se


def ci_approx(mean, se, alpha):
    zcrit = st.norm.ppf(1 - alpha/2)
    return mean - zcrit * se, mean + zcrit * se


for alpha in [0.05, 0.02]:
    print(f"\n=== {100*(1-alpha)}% CI ===")

    ci_e = ci_exact(mean, se, df=n-1, alpha=alpha)
    ci_a = ci_approx(mean, se, alpha=alpha)

    print("Exact CI:", ci_e)
    print("Approx CI:", ci_a)
