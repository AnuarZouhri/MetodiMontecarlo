import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.arctan(x)


a = 0
b = 10
N = 1000
repeat = 1000
estimates = []

for i in range(repeat):
    x_random = np.random.uniform(a, b, N)
    estimate = (b-a)*np.mean(f(x_random))
    estimates.append(estimate)

plt.hist(estimates, bins=30, edgecolor='black')
plt.title("Monte Carlo Estimate Distribution")
plt.xlabel("Estimate")
plt.ylabel("Frequency")
plt.show()