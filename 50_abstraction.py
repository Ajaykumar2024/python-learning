from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):     #abstract class 
        pass

class Sqare(Shape):
    def __init__(self,side):
        self.side=side

    def area(self):
        print("area of Sqare=",self.side*self.side)


class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius

    def area(self):
            print("area of circle=",3.14*self.radius*self.radius)
s=Sqare(3)
s.area()

c=Circle(10)
c.area()
        