class Shape:
    def __init__(self,color):
        self.color = color
    def getColor(self):
        return self.color
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self,height,width):
        self.height = height
        self.width = width
        self.color = "blue"
    def area(self):
        area = self.height * self.width
        return area
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
        self.color = "red"
    def area(self):
        area = 3.14 * (self.radius**2)
        return area
   
c1 = Circle(8)
print(c1.area())
print(c1.getColor())
c2 = Rectangle(3,4)
print(c2.area())
print(c2.getColor())
print("\n")


# Using Super()
        
class Shape:
    def __init__(self, color):
        self.color = color
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, height, width, color):
        super().__init__(color)  
        self.height = height
        self.width = width

    def area(self):
        area = self.height * self.width
        return area

class Circle(Shape):
    def __init__(self, radius, color):
        super().__init__(color)  
        self.radius = radius

    def area(self):
        area = 3.14 * (self.radius ** 2)
        return area


c1 = Circle(4,"brown")
print(c1.area())
print(c1.color)  

c2 = Rectangle(6, 7,"green")
print(c2.area())
print(c2.color) 
