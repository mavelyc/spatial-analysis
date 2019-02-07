# import matplotlib.pyplot as plt
# plt.plot([1,2,3],[5,7,4])
# plt.show()

from shapely.geometry import Polygon
from shapely.geometry import MultiPolygon
from shapely.geometry import box
from shapely.affinity import translate
from ast import literal_eval

class Room:
    def __init__(self, shape):
        self.shape = shape
        self.polygon = Polygon(self.shape)
        self.bounds = self.polygon.bounds

class Unit:
    def __init__(self, number, shape):
        self.number = number
        self.shape = shape
        width = self.shape[0]
        length = self.shape[1]
        self.box = box(0,0,width,length,ccw=False)
        self.bounds = self.box.bounds

    def possiblePlacements(self, room):
        if (room.contains(self.box)): print ("True")
        else: print ("False")



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




#---------------------------------------------------------------------------------------------------------------------------
def main():
    howMany()
    room1 = Room(shapeOfRoom)
    chiller = Unit(1,lengthWidthChiller)
    chiller.possiblePlacements(room1.polygon)
    # print (list(chiller.box.exterior.coords))
    # print (list(room1.polygon.exterior.coords))
    # print (chiller.box.area)
    # print (room1.polygon.area)

    # newRoom = translate(room,0,1)
    # print (list(newRoom.exterior.coords))
    
    if (room1.polygon.contains(chiller.box)): print('True')
    else: print ('False')


    
if __name__ == '__main__':
    main()

