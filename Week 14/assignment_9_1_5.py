with open('Week 14/hi.tmp', 'w+', encoding='utf-8') as f:
    __input = []
    while True:
        msg = input('input: ')
        if msg == '':
            break
        # 문제에선 문장이라고 표기되었지만, 문장을 구분하는 방법은 .과 ! 밖에 없습니다. 따라서 .과 ! 의 경우만 생각합니다.
        __is_next_line = False
        for i in msg.strip():
            
            # 다음 문장이 스페이스로 시작하지 않기 위한 조치.
            if __is_next_line:
                if i == ' ':
                    continue
                __is_next_line = False
            
            __input.append(i)

            if i == '.' or i == '!':
                __input.append('\n')
                __is_next_line = True
            
    f.write(''.join(__input))