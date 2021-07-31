import numpy as np

a = np.arange(15).reshape(3,5)
print(a)

#Normal boolean array
b = a > 6
print(b)

#different approach of boolean array
print(a[b])

print(a[b] == 0)
