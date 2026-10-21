import shape

class Circle(shape.Shapes):
    radius = 0

    def __init__(self, radius):
        self.radius = radius

    def getArea(self):
        return 3.14 * self.radius ** 2

    def getPerimeter(self):
        return 3.14 * self.radius * 2

    def __str__(self):
        return f"I am a circle. My radius is {self.radius}."