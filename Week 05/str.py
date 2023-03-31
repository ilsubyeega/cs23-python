"""
s = str('test')
s[1] = 'e' # <- This throws `SyntaxError: unterminated string literal (detected at line 1)`.
print(s)
"""

msg = '  good morning  '

print(msg, '(raw)')


stripped = msg.strip()
print(stripped, '(stripped)')

print(stripped.capitalize(), '(capitalized)')
print(stripped.title(), '(title)')

print('hello my world'.title())

print(msg.count('o'), '(count{o})')
print(msg.count('oo'), '(count{oo})')

print('1'.isdigit(), '(isdigit{1})')
print('1.0'.isdigit(), '(isdigit{1.0})')
print('a1'.isdigit(), '(isdigit{a1})')

words = msg.strip().split()
print(words, '(words)')
for word in words:
    print(word)