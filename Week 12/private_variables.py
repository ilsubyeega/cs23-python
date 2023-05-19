class BaseClass():
    __a = 'a'
    def getone(self):
        return self.__a

class DerivedClass(BaseClass):
    def gettwo(self):
        return self.__a
    __b = 'b'
    def getthree(self):
        return self.__b
    
baseClass = BaseClass()
derivedClass = DerivedClass()
print(baseClass.getone())
print(derivedClass.getone())
# print(derivedClass.gettwo())
# ^ AttributeError: 'DerivedClass' object has no attribute '_DerivedClass__a'.
print(derivedClass.getthree())