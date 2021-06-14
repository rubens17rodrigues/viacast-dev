from math import *


class Rectangle:
  def __init__(this, width, height):
    this.width = width
    this.height = height

  def perimeter(this):
    return 2*this.width + 2*this.height

  @property
  def area(this):
    return this.width*this.height


class IsoscelesTriangle:
  def __init__(this, base, height):
    this.base = base
    this.height = height

  def perimeter(this):
    side = sqrt(this.height**2 + (this.base/2)**2)
    return 2*side + base

  @property
  def area(this):
    return this.base*this.height/2


class Circle:
  def __init__(this, radius):
    this.radius = radius

  def perimeter(this):
    return 2*pi*this.radius

  @property
  def area(this):
    return pi*this.radius**2


if __name__ == '__main__':
  width, height = map(int, input('Enter the width and height for the rectangle (<width>,<height>):\n>>').split(','))
  rectangle = Rectangle(width, height)
  print(f"Area: {rectangle.area}\nPerimeter: {rectangle.perimeter()}")

  base, height = map(int, input('Enter the base and height for the isosceles triangle (<base>,<height>):\n>>').split(','))
  triangle = IsoscelesTriangle(base, height)
  print(f"Area: {triangle.area}\nPerimeter: {triangle.perimeter()}")

  radius = int(input('Enter the radius for the circle:\n>>'))
  circle = Circle(radius)
  print(f"Area: {circle.area}\nPerimeter: {circle.perimeter()}")
