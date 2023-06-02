msg = 'hello world'

w = open('hi.tmp', 'w')
w.write(msg)
w.write(str(3.14))
w.close()

r = open('hi.tmp', 'r')
print(r.read())
r.close()