
from abc import abstractclassmethod, abstractmethod
from cmath import sqrt
from distutils.command.install_egg_info import to_filename
import math
from re import L

class Figure:
    @abstractmethod
    def __str__(self) -> str:
        pass
class Dot(Figure):
    def __init__(self, x:float,y:float) -> None:
        super().__init__()
        self.x = x
        self.y = y
    
    def __str__(self) -> str:
        return f"X: {self.x},y:  {self.y}"
    
class Segment(Dot):
    def __init__(self, x: float, y: float, ending_x:float, ending_y:float) -> None:
        super().__init__(x, y)
        self.ending_x = ending_x
        self.ending_y = ending_y
        self.length = math.sqrt(pow(self.ending_x - self.x, 2) + pow(self.ending_y - self.y, 2))

    def __str__(self) -> str:
        return "{}, ending x: {}, ending y: {}, , length: {:.1f}".format(super().__str__(),self.ending_x, self.ending_y,self.length)

class Circle(Dot):
    def __init__(self, x: float, y: float, radius:float) -> None:
        super().__init__(x, y)
        self.radius = radius
        
    def __str__(self) -> str:
        return "{}, radius: {}".format(super().__str__(),self.radius)

class Rect(Figure):
    def __init__(self, side:float, top_side:float) -> None:
        super().__init__()
        self.side_length = side
        self.top_side_length = top_side
        self.area = self.side*self.top_side
        self.diagonal = math.sqrt(math.pow(self.side,2) + math.pow(self.top_side,2))
    
    def __str__(self):
        return "side length: {}, top side length: {}, area: {}, diagonal: {:.1f}".format(self.side, self.top_side, self.area, self.diagonal)
    
class Sphere(Figure):
    def __init__(self, x:float, y:float, z:float, radius:float) -> None:
        super().__init__()
        self.x = x
        self.y = y
        self.z = z
        self.radius = radius
        self.area = 4 * 3.14 *pow(self.radius,2)
    
    def __str__(self)->str:
        return "x: {}, y: {}, z: {}, radius: {}, area: {}".format(self.x, self.y, self.z, self.radius, self.area)
    
class Parallelepiped(Rect):
    def __init__(self, side: float, top_side: float, height:float) -> None:
        super().__init__(side, top_side)
        self.height = height
        self.area = 2 * (self.side * self.top_side + self.side * self.height + self.top_side * self.height)
        self.diagonal = math.sqrt(math.pow(self.side, 2) + math.pow(self.top_side, 2) + math.pow(self.height, 2))
    
    def __str__(self):
        return"{}, height: {}".format(super().__str__(), self.height)



