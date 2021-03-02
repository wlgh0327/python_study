import math
from typing import Any

class Rectangle:
    def __init__(self, x1:int, y1:int, x2:int, y2:int) -> None :
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2


rect = Rectangle(x1=20, y1=20, x2=40, y2=30)

dx = abs(rect.x1-rect.x2)
dy = abs(rect.y1-rect.y2)

ret = dx * dy
print(ret)
