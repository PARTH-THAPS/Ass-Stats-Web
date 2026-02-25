import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import t
import statsmodels.api as sm

data = pd.read_csv("/Users/user/Downloads/carmileage.csv")


data["MPG"] = pd.to_numeric(data["MPG"], errors="coerce")
data["HP"] = pd.to_numeric(data["HP"], errors="coerce")


data = data.dropna(subset=["MPG", "HP"])

X1 = sm.add_constant(data["HP"])
Y1 = data["MPG"]
model1 = sm.OLS(Y1, X1).fit()
print("-----Simple Linear regression-------")
print(model1.summary())

plt.figure()
plt.scatter(data["HP"], data["MPG"], color="blue", label="data")
plt.plot(data["HP"], model1.predict(X1), color="red", label="Fitted Line")
plt.show()
