from stack import Stack

class PostFixNotation:
    def __init__(self):
        self.__stack = Stack()
        self.__opr = {'+': self.__add, '*':self.__mul}
    
    def __add(self, n1, n2):
        return n1 + n2
    
    def __mul(self, n1, n2):
        return n1 * n2
    
    def calculate(self, expr):
        for token in expr.split(' '):
            if token.isdigit():
                self.__stack.push(int(token))
            elif token in self.__opr:
                n2 = self.__stack.pop()
                n1 = self.__stack.pop()
                self.__stack.push(self.__opr[token](n1, n2))
            else:
                raise ValueError('Invalid token')
        return self.__stack.pop()
    
if __name__ == '__main__':
    postifx = PostFixNotation()
    print(postifx.calculate('12 3 10 + *'))