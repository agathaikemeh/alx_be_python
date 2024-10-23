# polymorphism_demo.py
import math

class Shape:
    def area(self):
        """Method to calculate area, intended to be overridden by derived classes."""
        raise NotImplementedError("This method should be overridden in derived classes.")

class Rectangle(Shape):
    def __init__(self, length: float, width: float):
        """Initialize Rectangle attributes."""
        self.length = length
        self.width = width

    def area(self):
        """Calculate the area of the rectangle."""
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius: float):
        """Initialize Circle attributes."""
        self.radius = radius

    def area(self):
        """Calculate the area of the circle."""
        return math.pi * (self.radius ** 2)

