import numpy as np
from collections import defaultdict
from pprint import pprint

def insert_pattern(key, value):
    if key not in pattern:
        pattern[key] = []  # crea la lista se la chiave non esiste
    if not any(np.array_equal(value, v) for v in pattern[key]):
        pattern[key].append(value)


'''
i = 0 -> type A
i = 1 -> type B
i = 2 -> type C
and so and so forth
'''

L = 100 #roll length

d = np.array([200,132,125]) #demand
c = np.array([7,4,5]) #cuts for type
s = np.array([0,0,0]) #pattern cut
n = 3 #size of the vector
pattern = defaultdict(list)

m = np.floor(L/np.mean(c)) #max value to sample

repeat = 1000

for i in range(repeat):
    s = np.random.randint(0, m, size=n)
    print(s)
    scal = np.dot(c,s)
    if scal <= L and np.any(s != 0):
        insert_pattern(L-scal, s)


pprint(pattern)