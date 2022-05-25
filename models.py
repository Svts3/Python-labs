
from abc import abstractmethod
import math


class Figure:
    @abstractmethod
    def __str__(self) -> str:
        pass
class Dot(Figure):
    def __init__(self, x:float, y:float) -> None:
        super().__init__()
        self.x = x
        self.y = y
    def __str__(self) -> str:
        return f"X: {self.x}, y:  {self.y}"
class Segment(Dot):
    def __init__(self, x: float, y: float, ending_x:float, ending_y:float) -> None:
        super().__init__(x, y)
        self.ending_x = ending_x
        self.ending_y = ending_y
        self.length = math.sqrt(pow(self.ending_x - self.x, 2) + pow(self.ending_y - self.y, 2))

    def __str__(self) -> str:
        return (f"{super().__str__()}, ending x: {self.ending_x}, ending y: {self.ending_y},"
    f" length: {self.length:.1f}")
class Circle(Dot):
    def __init__(self, x: float, y: float, radius:float) -> None:
        super().__init__(x, y)
        self.radius = radius
    def __str__(self) -> str:
        return f"{super().__str__()}, radius: {self.radius}"
class Rect(Figure):
    def __init__(self, side:float, top_side:float) -> None:
        super().__init__()
        self.side_length = side
        self.top_side_length = top_side
        self.area = self.side_length*self.top_side_length
        self.diagonal = math.sqrt(math.pow(self.side_length,2) + math.pow(self.top_side_length,2))
    def __str__(self):
        return (f"side length: {self.side_length}, top side length: {self.top_side_length}, "
                f"area: {self.area}, diagonal: {self.diagonal:.1f}")
class Sphere(Figure):
    def __init__(self, x:float, y:float, z:float, radius:float) -> None:
        super().__init__()
        self.x = x
        self.y = y
        self.z = z
        self.radius = radius
        self.area = 4 * 3.14 *pow(self.radius,2)
    def __str__(self)->str:
        return f"x: {self.x}, y: {self.y}, z: {self.z}, radius: {self.radius}, area: {self.area}"
class Parallelepiped(Rect):
    def __init__(self, side: float, top_side: float, height:float) -> None:
        super().__init__(side, top_side)
        self.height = height
        self.area = 2 * (self.side_length * self.top_side_length + self.side_length
                         * self.height + self.top_side_length * self.height)
        self.diagonal = math.sqrt(math.pow(self.side_length, 2) + math.pow(self.top_side_length, 2)
                                  + math.pow(self.height, 2))
    def __str__(self):
        return f"{super().__str__()}, height: {self.height}"
    