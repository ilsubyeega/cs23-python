class D(object):
    def __init__(self):
        print('Class_D')
        self.data = 1

class B(D):
    def __init__(self):
        print('Class_B')
        self.data = 2

class C(D):
    def __init__(self):
        print('Class_C')
        self.data = 3
    def get(self):
        return self.data, 3
    def calc(self, n):
        return self.data + n

class E(object):
    def __init__(self):
        print('Class_E')
        self.data = 4

class A(B, C, E):
    def __init__(self):
        print('Class_A')
        super(C, self).__init__()
        C.__init__(self)
        print(self.data)
        self.data = 5

obj = A()
print(obj.get())
print(obj.calc(9))