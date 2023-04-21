itext = input('성적(0~100점)? ')
flag_failture = True
if itext.isdigit():
    point = int(itext)
    if 0 <= point <= 100:
        print(f'{"*" * (point // 10):>10}: {point:>3}')
        # FAIL: Was `print(f'{'*' * (point // 10):>10}: {point}')`. But quotes were not seperated (' and "), also point wasnt right aligned for 3 chars.
        flag_failture = False

if flag_failture:
    print('입력 오류')

"""
Point: (6/10)"""