class Position:
    def __init__(self, x=0, y=0):
        self.set_position(x, y)
    def __str__(self):
        return "(x, y) = ({0}, {1})".format(self.__x, self.__y)
    
    def set_position(self, x, y):
        if x < 0 or y < 0:
            raise ValueError("Position cannot be negative")
        self.__x = x
        self.__y = y
    def get_position(self):
        return (self.__x, self.__y)

center = Position(15, 20)
print(center.get_position())
print(center)