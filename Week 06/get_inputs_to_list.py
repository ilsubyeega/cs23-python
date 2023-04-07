arr = []
while True:
    _input = input("integer(-1 for stop): ")
    if _input == '-1':
        break

    if _input.isdigit():
        arr.append(int(_input))
    else:
        print("Invalid input")

print("Total =", sum(arr), "Average =", f'{sum(arr)/len(arr):.2f}')