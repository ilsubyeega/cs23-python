list = [9, 15, 4, 5, 3, 13, 7, 8, 18, 11]

# Get odds
odds = [x for x in list if x % 2 == 1]
odds_length = len(odds)

# Get max
max_from_list = max(list)

# Get min
min_from_list = min(list)

print(odds_length, max_from_list, min_from_list)