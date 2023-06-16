import numpy as np
position = 0
walk = [position]
steps = 1000
for i in range(steps):
    step = 1 if np.random.randint(0,2) else -1
    position += step
    walk.append(position)

print(position)
print(min(walk))
print(max(walk))