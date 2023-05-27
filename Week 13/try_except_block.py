try:
    n = int(input('Enter a number: '))
    print('100/n:', 100/n)
except ZeroDivisionError as ev:
    print('Cannot divide by zero')
except ValueError:
    print('Invalid input')