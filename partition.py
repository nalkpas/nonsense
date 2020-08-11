import numpy as np

partition = [24] + [4]*12 + [3]
N = 15

# partition = [24] + [4]*9
# N=7

p = np.poly1d([1])
for l in partition:
    p= p*np.poly1d([1]*(l+1))

print(p.c[N+1])
