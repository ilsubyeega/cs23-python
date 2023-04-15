import random
list = []
for _ in range(100):
    list.append(random.randint(0, 100))

t = tuple(list)
print("tuple", t)
print("odd count", len([x for x in t if x % 2 == 1]))
