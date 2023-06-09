import numpy as np

arr = np.zeros(shape=(3,5))

for i in range(arr.shape[0]):
    arr[i, i] = 1
    arr[i, arr.shape[1] - i - 1] = 1

print(arr)