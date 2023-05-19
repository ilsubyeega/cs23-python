class App:
    def __init__(self):
        self.__flag = True
    def set_flag(self, value):
        if isinstance(value, bool):
            self.__flag = value
        else:
            raise TypeError("flag must be a bool")
    def get_flag(self):
        return self.__flag

app = App()
print(app.get_flag())
# True
app.set_flag(False)
print(app.get_flag())
# False
app.set_flag(1)
# TypeError: flag must be a bool