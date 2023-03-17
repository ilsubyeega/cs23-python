n = int(input("n: "))
m = int(input("m: "))

print(n & (0x1 << m) == 0)

# 0 & 0 == 0 이기 때문에, 0b00010 & (0x << 1) != 0 이다.