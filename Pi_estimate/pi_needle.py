import numpy as np
import math

l = float(input("Insert needle length:"))
theta = 0
d = float(input("Insert lines distance:"))
k = 10000
m = 0
pi_estimate = 0
for i in range(k):
    y = np.random.uniform(0, d/2)
    theta = np.random.uniform(0, np.pi)

    if ((l/2) * np.sin(theta) >= y):
        m = m + 1

print(m)
if (m != 0 and d != 0):
    pi_estimate = (2 * l * k)/(m * d)

print(pi_estimate)