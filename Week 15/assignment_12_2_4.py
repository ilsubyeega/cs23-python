# p.264

import numpy as np
import random

arr0 = np.zeros(shape=(10,10), dtype=np.float32)

for _ in range(10):
    arr0[random.randint(0,9), random.randint(0,9)] = random.uniform(0,1)

print(arr0)