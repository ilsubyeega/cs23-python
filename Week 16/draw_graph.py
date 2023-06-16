import matplotlib.pyplot as plt
import numpy as np
import random

x = np.arange(0, 10, 1)
#y = np.arange(0, 10, 1)
y = [random.uniform(0,1) for _ in range(10)]

plt.plot(x, y, ':')
plt.show()