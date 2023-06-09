import numpy as np

arr = np.linspace(0, 5, 12, dtype=np.float32)

arr0 = arr.reshape(3,4)
arr1 = arr.reshape(4,3)

print(arr0, arr1, np.dot(arr0, arr1), sep='\n\n') # inner product through.