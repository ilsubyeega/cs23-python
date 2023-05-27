class Stack:
    def __init__(self):
        self.__data = []
    def push(self, item):
        self.__data.append(item)
    def pop(self):
        try:
            return self.__data.pop()
        except IndexError:
            return None
    def get_size(self):
        return len(self.__data)