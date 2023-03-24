text = '534183552676'

for idx, i in enumerate(list(text)):
    if (int(i) > 5):
        print(idx)
        break

reversed = list(text)
reversed.reverse()
for idx, i in enumerate(reversed):
    if (int(i) > 5):
        print(len(reversed) - idx)
        break

# This is very bad idea through.