import numpy as np
import random

lst1 = [[random.randint(1, 10) for _ in range(3)] for _ in range(4)]
lst2 = [[random.randint(1, 10) for _ in range(3)] for _ in range(4)]

arr1 = np.array(lst1)
arr2 = np.array(lst2)

print(arr1)
print(arr2)

print('arr1 + arr2', arr1 + arr2, sep='\n')
print('arr1 - arr2', arr1 - arr2, sep='\n')
print('arr1 * arr2', arr1 * arr2, sep='\n')
print('arr1 / arr2', arr1 / arr2, sep='\n')
print('arr1 % arr2', arr1 % arr2, sep='\n')
print('arr1 ** arr2', arr1 ** arr2, sep='\n')