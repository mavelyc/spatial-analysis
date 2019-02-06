# import matplotlib.pyplot as plt
# plt.plot([1,2,3],[5,7,4])
# plt.show()

from shapely.geometry import Polygon
from shapely.geometry import MultiPolygon
from ast import literal_eval

# list1 = literal_eval(input("Enter it: "))
# polygon = Polygon(list1)
# print (polygon.area)
# print (polygon.length)
# print (type(list1))

#object.contains(other)  This returns True if no points of other lie in the exterior of the object and at least one point of the interior of other lies in the interior of object
#object.within(other)  This is the same as object.contains but only returns True if the obeject within intersects ONLY with interior not its boundary

# print(polygon.contains(polygon2))

class Room:
    def __init__(self, shape):
        self.shape = shape

    def area(self):
        tmp = Polygon(self.shape)
        print (tmp.area)

class Unit:
    def __init__(self, number, shape):
        self.number = number
        self.shape = shape

numberOfChillers = 0
numberOfBoilers = 0
shapeOfRoom = 0
def howManyUnits():
    global numberOfChillers, numberOfBoilers, shapeOfRoom
    shapeOfRoom = literal_eval(input("Enter the coordinates of the room [(0,0),(1,1)...]: "))
    numberOfChillers = input("Enter the number of chillers: ")
    numberOfBoilers = input("Enter the number of boilers: ")





def main():
    howManyUnits()
    room = Room(shapeOfRoom)
    room.area()

    
if __name__ == '__main__':
    main()

