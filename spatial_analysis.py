# import matplotlib.pyplot as plt
# plt.plot([1,2,3],[5,7,4])
# plt.show()

from shapely.geometry import Polygon
from shapely.geometry import MultiPolygon
from shapely.geometry import box
from ast import literal_eval

# polygon = Polygon(list1)
# print (polygon.area)
# print (polygon.length)

#object.contains(other)  This returns True if no points of other lie in the exterior of the object and at least one point of the interior of other lies in the interior of object
#object.within(other)  This is the same as object.contains but only returns True if the obeject within intersects ONLY with interior not its boundary

# print(polygon.contains(polygon2))

class Room:
    def __init__(self, shape):
        self.shape = shape

    def setSurface(self):
        return Polygon(self.shape)

class Unit:
    def __init__(self, number, shape):
        self.number = number
        self.shape = shape
    
    def setBox(self):
        width = self.shape[0]
        length = self.shape[1]
        #print (width,length)
        return box(0,0,width,length)


numberOfChillers = 0
numberOfBoilers = 0
shapeOfRoom = 0
lengthWidthChiller = 0
lengthWidthBoiler = 0
def howMany():
    global numberOfChillers, numberOfBoilers, shapeOfRoom, lengthWidthBoiler, lengthWidthChiller
    shapeOfRoom = literal_eval(input("Enter the coordinates of the room [(0,0),(1,1)...]: "))
    numberOfChillers = input("Enter the number of chillers: ")
    lengthWidthChiller = literal_eval(input("Enter the width and length of chiller [width,length]: "))
    #numberOfBoilers = input("Enter the number of boilers: ")
    #lengthWidthBoiler = literal_eval(input("Enter the width and length of boiler [width,length]: "))

def doesContain(room, unit):
    return room.contains(unit)




def main():
    howMany()
    room = Room(shapeOfRoom).setSurface()
    chiller = Unit(1,lengthWidthChiller).setBox()
    print (room.area, chiller.area)
    if (doesContain(room, chiller)): print('True')
    else: print ('False')


    
if __name__ == '__main__':
    main()

