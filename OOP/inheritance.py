"""
Inheritance


Inheritance provides a way to share functionality between classes.

"""

class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def display(self):
        print(self.name, self.color)


class Cat(Animal):
    def purr(self):
        print("Purr....")

    def display(self):
        print("Purrrrrr...")
        print(self.name, self.color)


class Dog(Animal):
    def bark(self):
        print("bark")

fido = Dog("fido","brown")
fido.display()
fido.bark()

rover = Cat("rover","white")
rover.display()


class A:
    def method(self):
        print("A method")

class B(A):
    def another_method(self):
        print("B method")

class C(B):
    def third_method(self):
        print("C method")

c= C()
c.method()
c.another_method()
c.third_method()

class X:
    def spam(self):
        print(1)

class Y(X):
    def spam(self):
        print(2)
        super().spam()

Y().spam()
