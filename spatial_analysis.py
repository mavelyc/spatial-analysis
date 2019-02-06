# import matplotlib.pyplot as plt
# plt.plot([1,2,3],[5,7,4])
# plt.show()

from shapely.geometry import Polygon
from shapely.geometry import MultiPolygon
from shapely.geometry import box
from ast import literal_eval

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





#---------------------------------------------------------------------------------------------------------------------------
def main():
    howMany()
    room = Room(shapeOfRoom).setSurface()
    chiller = Unit(1,lengthWidthChiller).setBox()
    print (room.area, chiller.area)
    if (doesContain(room, chiller)): print('True')
    else: print ('False')


    
if __name__ == '__main__':
    main()

