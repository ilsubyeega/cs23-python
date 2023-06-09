import numpy as np
arr0 = np.zeros(shape=(3,5), dtype=np.int32)
print(arr0)

arr0[1,2] = 7
arr0[0,4] = 8

print(arr0)
print(arr0.shape, arr0.dtype, arr0.size, arr0.ndim)