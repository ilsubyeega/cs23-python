n = int(input("Number: "))
m = n - ((n>>1)<<1)
# 짝수면 뒤가 0이기 때문에 0
# 홀수는 뒤가 1이기 때문에 1
print(m)