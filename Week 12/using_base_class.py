class Animal:
    def sound(self):
        return 'Not defined'

class Dog(Animal):
    def count_legs(self):
        return 4

dog = Dog()
print(dog.count_legs())
print(dog.sound())