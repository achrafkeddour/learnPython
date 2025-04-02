class Shape:
    def __init__(self,color,is_filled):
        self.color= color
        self.is_filled = is_filled
        
    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not_filled'}")
        
class Circle(Shape):
    def __init__(self, color, is_filled,radius):
        super().__init__(color, is_filled)
        self.radius=radius

    def describe(self):
        super().describe()
        print(f"The area of this Circle is {3.14 * self.radius * self.radius }")

class Square(Shape):
    def __init__(self,color,is_filled,width):
        super().__init__(color,is_filled)
        self.width=width
    
    def describe(self):
        super().describe()
        print(f"The area of this Square is {self.width * self.width}")
        
class Triangle(Shape):
    def __init__(self,color,is_filled,width,height):
        super().__init__(color,is_filled)
        self.width = width
        self.height = height

    def describe(self):
        super().describe()
        print(f"The area of this Triangle is {self.width * self.height / 2}")
        

circle = Circle("Red", True, 5)
circle.describe()

print("\n")

square = Square("Blue", False, 4)
square.describe()

print("\n")

triangle = Triangle("Green", True, 6, 8)
triangle.describe()
