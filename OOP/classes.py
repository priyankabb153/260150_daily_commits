class Cat:
    def __init__(self, color, legs):
        self.color = color
        self.legs = legs

felix = Cat("ginger", 4)
rover = Cat("dog-colored", 4)
stumpy = Cat("brown", 3)

print(felix.color,felix.legs)
print(rover.color,rover.legs)
print(stumpy.color,stumpy.legs)

# In the example above, the __init__ method takes two arguments and
# assigns them to the object's attributes.
# The __init__ method is called the class constructor.


class Dog:
    legs = 4 # attribute
    def __init__(self,name,color):
        self.name = name
        self.color = color

    def bark(self):
        print("woof")


fido = Dog("Fido", "brown")
print(fido.name, fido.legs)
print(Dog.legs)
fido.bark()

# Class attributes are shared by all instances of the class.


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def display(self):
        print(self.length, self.width)

rect = Rectangle(4,5)
rect.display()

