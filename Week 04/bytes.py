data = b"abc\xFF\xA5\xF0"
data2 = bytes([65, 0x42, 0o103, 0b1000100])

hangul = '안녕'.encode() # b'안녕'

print(len(data), data)
print(data[0], data[3])
print(data2, len(data2))
print(len(hangul), hangul, hangul.decode())


h = '\U0001f491'
print(h)
print(h.encode())