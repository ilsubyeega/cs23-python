credits = [3, 2, 2]
points = [4.5, 3.5, 4.0]

average = credits[0] * points[0]
average += credits[1] * points[1]
average += credits[2] * points[2]

average /= points[0] + points[1] + points[2]

print(f'{average:.2f}')