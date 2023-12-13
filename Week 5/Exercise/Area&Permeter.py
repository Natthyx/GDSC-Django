class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def areaOfRectangle(self):
        return self.width*self.height
    def permeterOfRectangle(self):
        return 2*(self.width+self.height)

R1 = Rectangle(5,4)
R2 = Rectangle(9,7)

print(R1.areaOfRectangle())
print(R2.permeterOfRectangle())

