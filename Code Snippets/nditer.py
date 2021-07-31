import numpy as np

a = np.arange(10).reshape(2,5)
print(a)

b = np.arange(2).reshape(2,1)
print(b)

#Iterate two arrays simulatenously using nditer
for x,y in np.nditer([a,b]):
    print(x,y)
