class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)


first = Vector2D(5, 7)
second = Vector2D(3, 9)
result = first + second
print(result.x)
print(result.y)

"""
The __add__ method allows for the definition of a custom behavior for the + operator in our class.
As you can see, it adds the corresponding attributes of the objects and returns a new object, containing the result.
Once it's defined, we can add two objects of the class together.

Magic Methods


More magic methods for common operators:
__sub__ for -
__mul__ for *
__truediv__ for /
__floordiv__ for //
__mod__ for %
__pow__ for **
__and__ for &
__xor__ for ^
__or__ for |

"""


class SpecialString:
    def __init__(self, cont):
        self.cont = cont

    def __truediv__(self, other):
        line = "=" * len(other.cont)
        return "\n".join(([self.cont, line, other.cont]))


spam = SpecialString("spam")
hello = SpecialString("Hello world!")
print(spam / hello)

"""
__lt__ for <
__le__ for <=
__eq__ for ==
__ne__ for !=
__gt__ for >
__ge__ for >=


"""

class Special:
    def __init__(self, cont):
        self.cont = cont

    def __gt__(self, other):
        for index in range(len(other.cont)+1):
            result = other.cont[:index] + ">" + self.cont
            result+=">"+other.cont[index:]
            print(result)

spam = Special("spam")
eggs = Special("eggs")
spam > eggs
