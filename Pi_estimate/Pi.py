import numpy as np
import math


a = 0
b = 1
k = 800
m = 0

for i in range(k):
    x = np.random.uniform(low=a, high=b)
    y = np.random.uniform(low=a, high=b)

    if (math.sqrt(x**2+y**2)<=1):
        m = m + 1



print(4*m/k)