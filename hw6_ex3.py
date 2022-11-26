# 3. In this exercise you will create an interface that will serve as template 
# for different figures to compute their perimeter and surface. 

# 3.1Create an abstract class (interface) called "PlaneFigure"
#  with two abstract methods:
# compute_perimeter() that will implement the formula to compute
#  the perimiter of the plane figure.
# compute_surface() that will implement the formula to compute 
# the surface of the plane figure.

from abc import ABCMeta, abstractmethod
import math

class PlaneFigure(metaclass=ABCMeta):

    @abstractmethod
    def compute_perimeter(self):
        return NotImplementedError

    @abstractmethod
    def compute_surface(self):
        return NotImplementedError

# 3.2 Create a child class called "Triangle" that inherits 
# from "PlaneFigure" and has as parameters in the constructor "base",
#  "c1", "c2", "h". ("base" being the base, "c1" and "c2" the other 
# two sides of the triangle and "h" the height). 
# Implement the abstract methods with the formula of the triangle.


class Triangle(PlaneFigure):
    def __init__(self, base, c1, c2, h):
        self.base = base
        self.c1 = c1
        self.c2 = c2
        self.h = h

    def compute_perimeter(self):
        return self.base + self.c1 + self.c2
    
    def compute_surface(self):
        return (self.base*self.h)/2
# 3.3 Create a child class called "Rectangle" that inherits 
# from "PlaneFigure" and has as parameters in the constructor 
# "a", "b" (sides of the rectangle). Implement the abstract methods 
# with the formula of the rectangle.


class Rectangle(PlaneFigure):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def compute_perimeter(self):
        return self.a + self.b
    
    def compute_surface(self):
        return (self.a*self.b)

# 3.3 Create a child class called "Circle" that inherits 
# from "PlaneFigure" and has as parameters in the constructor 
# "radius" (radius of the circle). Implement the abstract methods 
# with the formula of the circle.


class Circle(PlaneFigure):
    def __init__(self, radius):
        self.radius = radius

    def compute_perimeter(self):
        return 2*self.radius*math.pi

    def compute_surface(self):
        return math.pi*self.radius**2


tri1 = Triangle(2, 3, 4, 1)
print("triangle perimeter: " + str(tri1.compute_perimeter()))
print("triangle surface: " + str(tri1.compute_surface()))


rec1 = Rectangle(2, 4)
print("rectangle perimeter: " + str(rec1.compute_perimeter()))
print("rectangle surface: " + str(rec1.compute_surface()))

cir1 = Circle(2)
print("circle perimeter: " + str(cir1.compute_perimeter()))
print("circle surface: " + str(cir1.compute_surface()))
