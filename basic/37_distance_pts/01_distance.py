from typing import Any
import math

class Point2D :
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

def calcDistance(p1: Point2D, p2: Point2D) -> Any :

    ret = 0
    dx = abs(p1.x - p2.x)
    dy = abs(p1.y - p2.y)

    ret = math.sqrt(dx**2 + dy**2)

    return ret

if __name__ == '__main__' :
    p1 = Point2D(x=30, y=20)
    p2 = Point2D(x=60, y=50)

    print('p1 : {} / {}'.format(p1.x, p1.y))
    print('p2 : {} / {}'.format(p2.x, p2.y))

    print('Distance : {}'.format(calcDistance(p1, p2)))


