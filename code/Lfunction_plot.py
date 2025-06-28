import numpy as np
import matplotlib.pyplot as plt
from mpmath import mp

mp.dps = 50
N = 300
a_n = np.zeros(N + 1)

for a in range(1, 50):
    for b in range(1, a):
        n = a**2 - b**2
        if n <= N:
            a_n[n] += 1

def L_struct(s):
    return sum(a_n[n] / (n ** s) for n in range(1, N+1) if a_n[n] != 0)
