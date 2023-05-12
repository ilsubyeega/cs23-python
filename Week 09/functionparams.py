def fun1(a, b, c, d):
    print(a, b, c, d)

fun1(1, 2, 3, 4)
fun1(d=1, c=2, b=3, a=4)

def fun2(a, b, *, c, d):
    print(a, b, c, d)

def fun3(a, b, /, c, d):
    print(a, b, c, d)

# ^ ???