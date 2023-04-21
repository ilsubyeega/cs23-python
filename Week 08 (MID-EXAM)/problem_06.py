msg = 'hello my name is Hong Gil Dong'
msg = msg.lower()
wc = {}
for c in msg:
    # FAIL: Ws `for c msg` (fuck)
    if ord('a') <= ord(c) <= ord('z'):
        if c in wc.keys():
            wc[c] += 1
        else:
            wc[c] = 1
print(f'문자열: {msg}')
for c in wc.keys():
    # FAIL: Was `for c wc.keys()` (fuck)
    print(f'{c}: {wc[c]}')

"""
Point: (6/8)
"""