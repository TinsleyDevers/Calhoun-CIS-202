class Shape:
    def area(self):
        pass
        
class Square(Shape):
    def __init__(self, side):
        self.side = side
        
    def area(self):
        return self.side ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

square = Square(3)
triangle = Triangle(3, 6)


print(f"Area of the square: {square.area()}")
print(f"Area of the triangle: {triangle.area()}")
