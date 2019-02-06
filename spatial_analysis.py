# import matplotlib.pyplot as plt

# plt.plot([1,2,3],[5,7,4])

# plt.show()

from shapely.geometry import Polygon
from shapely.geometry import MultiPolygon

polygon = Polygon([(0,0),(1,1),(2,1),(1,0)])
print (polygon.area)
print (polygon.length)

polygon2 = Polygon([(1,1),(2,1),(1,0)])
print (polygon2.area)
print (polygon2.length)

polygons = MultiPolygon([polygon,polygon2])

print (polygons.bounds)

#object.contains(other)  This returns True if no points of other lie in the exterior of the object and at least one point of the interior of other lies in the interior of object
#object.within(other)  This is the same as object.contains but only returns True if the obeject within intersects ONLY with interior not its boundary

print(polygon.contains(polygon2))

class Unit:
    def __init__(self, name):
        shape = input("Enter the coordinates of the room [(0,0),(1,,1)...]:")
        self.name = name
        self.shape = shape
        print(self.name)
        print(self.shape)

test = Unit("bruv")
test1 = Unit("Oi")

