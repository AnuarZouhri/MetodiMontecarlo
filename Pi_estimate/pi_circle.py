import numpy as np
import math


a = 0
b = 1
m = 0
k= 1000
for i in range(k):
    x = np.random.uniform(a, b)
    y = np.random.uniform(a, b)

    if (math.sqrt(x**2+y**2)<=1):
        m = m + 1



print(4*m/k)