import random

def getTotal(data):
    total = 0
    for x in data:
        total += x
    return total

rndlist = [random.randint(0, 100) for _ in range(10)]
evenlst = [n for n in rndlist if n % 2 == 0]
print(evenlst)
print(getTotal(evenlst))

evenlst = [n for n in [random.randint(0, 100) for _ in range(10)] if n % 2 == 0]
print(evenlst)
print(getTotal(evenlst))

"""
Point: (11/11)
"""