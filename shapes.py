from math import *


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, new_width):
        self._width = new_width
    
    def perimeter(self):
        return 2*self.width + 2*self.height

    def area(self):
        return self.width*self.height


class IsoscelesTriangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def perimeter(self):
        side = sqrt(self.height**2 + (self.base/2)**2)
        return 2*side + base

    def area(self):
        return self.base*self.height/2


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        return 2*pi*self.radius

    def area(self):
        return pi*self.radius**2


if __name__ == '__main__':
    width, height =  map(int, input('Enter the width and height for' \
        'the rectangle (<width>,<height>):\n>>').split(','))
   
    rectangle = Rectangle(width, height)
    print(f"Area: {rectangle.area()}\nPerimeter: {rectangle.perimeter()}")

    base, height = map(int, input('Enter the base and height for ' \
        'the isosceles triangle (<base>,<height>):\n>>').split(','))

    triangle = IsoscelesTriangle(base, height)
    print(f"Area: {triangle.area()}\nPerimeter: {triangle.perimeter()}")

    radius = int(input('Enter the radius for the circle:\n>>'))
    circle = Circle(radius)
    print(f"Area: {circle.area()}\nPerimeter: {circle.perimeter()}")
