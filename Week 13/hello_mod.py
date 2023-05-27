def sum(*data):
    print(f'hello_mod: Called `sum`. ({data})')
    total = 0
    for v in data:
        total = total + v
    return total

print(f'hello_mod: The name of this module is {__name__}')