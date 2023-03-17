credits = [3, 2, 3]
points = [4.5, 3.5, 4.0]

average = ((credits[0] * points[0]) + ((credits[1] * points[1])) + (credits[2] * points[2])) \
    / (points[0] + points[1] + points[2])

print(average)