year = int(input('년도 입력: '))
if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
    print('평년')
else:
    print('윤년')