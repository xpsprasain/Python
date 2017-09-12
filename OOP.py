class Animal:
    __count = 0

    def __init__(self, name):
        self.name = name

    @staticmethod
    def getCount():
        return Animal.__count

    @staticmethod
    def incrementCount():
        Animal.__count += 1


class Dog(Animal):
    def __init__(self, name):
        Animal.incrementCount()
        self.name = name


class Cat(Animal):
    def __init__(self, name):
        Animal.incrementCount()
        self.name = name


d = Dog("d")
c = Cat("c")

print(Animal.getCount())


class A:
    __c = 12


g = A()

print(g._A__c)

