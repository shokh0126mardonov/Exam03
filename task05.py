from abc import ABC,abstractmethod

class Shape(ABC):
    
    @abstractmethod
    def area():
        pass

class Circle(Shape):
    
    def __init__(self,radius):
        self.radius = radius
        
    def area(self):
        return  self.radius * self.radius * 3.14
        

class Rectangle(Shape):
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def area(self):
        return  self.a * self.b
    
c = Circle(5)
r = Rectangle(4, 6)
print(c.area())
print(r.area())