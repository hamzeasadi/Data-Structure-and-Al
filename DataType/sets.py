import math
import random






class Polygon():
    def __init__(self, no_of_sides):
        self.nos = no_of_sides
        self.sides = [0 for x in range(no_of_sides)]

    def inputSides(self):
        self.sides = [eval(input(f"Enter side {i+1}: ").strip()) for i in range(self.nos)]

    def dispSides(self):
        for i in range(self.nos):
            print(f"side {i+1}: {self.sides[i]}")


class Triangle(Polygon):

    def __init__(self):
        super(Triangle, self).__init__(3)

    def findArea(self):
        a, b, c = self.sides
        s = sum(self.sides)/2
        area = (s*(s-a)*(s-b)*(s-c))**0.5
        print(f'Triangle area with sides {a}, {b}, {c} is: {area}')

class Point(Triangle):
    """this is a simple cartesian space"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __call__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'x={self.x}, y={self.y}'

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

def For(obj):
    obj_iterator = iter(obj)
    while True:
        try:
            print(next(obj_iterator))
        except StopIteration:
            break


def main():
    # For([1, 2, 3])
    a = [1, 2]
    a_iterator = iter(a)
    print(*a)
    print(*a_iterator)



if __name__ == '__main__':
    main()
