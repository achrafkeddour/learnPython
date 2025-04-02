""" Polymorphism : is a greek word that means 'to have many forms or faces' 
Poly = many
morphism = form

TWO WAYS TO ACHIEVE POLYMORPHISM
1. Inheritance = When a subclass overrides a method from its superclass, allowing different behaviors for the same method name in different classes.
2. Duck typing = When an object is used based on its behavior rather than its actual class, meaning if it "quacks like a duck and walks like a duck," it's treated as a duck.

""" 

# Polymorphism using Inheritance
# When a child class overrides a method from its parent class, we achieve polymorphism.

# Parent class (Base class)
class Shape:
    def area(self):
        return "Each shape has a different way to calculate area"

# Child classes (Derived classes)
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):  # Overriding the parent method
        return 3.14 * self.radius * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):  # Overriding the parent method
        return self.side * self.side

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):  # Overriding the parent method
        return 0.5 * self.base * self.height

# Function to demonstrate polymorphism
def print_area(shape):
    print(shape.area())  # Calls the overridden method based on the object type

# Creating objects of different subclasses
circle = Circle(5)
square = Square(4)
triangle = Triangle(6, 3)

# Using polymorphism to call the correct area() method
print_area(circle)  # Output: 78.5
print_area(square)  # Output: 16
print_area(triangle)  # Output: 9.0

# Another example of polymorphism with a loop
shapes = [Circle(3), Square(2), Triangle(4, 5)]
for shape in shapes:
    print(shape.area())
