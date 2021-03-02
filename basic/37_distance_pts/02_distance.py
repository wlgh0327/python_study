import math
import collections

Point2D = collections.namedtuple('Point2D', ['x', 'y'])

p1 = Point2D(x=30, y=20)
p2 = Point2D(x=60, y=50)

dx = abs(p1.x - p2.x)
dy = abs(p1.y - p2.y)

d = math.sqrt(dx**2 + dy**2)

print(d)
