# https://www.qu3vipon.com/why-numbering-should-start-at-zero

data = '철수와 친구들'

print(data) # 철수와 친구들
print(data[0], data[4], data[6]) # 철 친 들
print(data[2:5]) # 와 친
# ^ 이거 "와 친" 3글자인데, (2,3,4,5) 총 4글자가 아닌 3글자임
print(data[:4]) # 철수와
print(data[2:]) # 와 친구들

print("2:1", data[2:1])
print("2:2", data[2:2])
print("3:3", data[3:3])