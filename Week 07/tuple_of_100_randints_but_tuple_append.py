import random
t = ()
for _ in range(100):
    t += (random.randint(0, 100),)

print("tuple", t)
print("odd count", len([x for x in t if x % 2 == 1]))
