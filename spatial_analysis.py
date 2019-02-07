# import matplotlib.pyplot as plt
# plt.plot([1,2,3],[5,7,4])
# plt.show()

from shapely.geometry import Polygon
from shapely.geometry import MultiPolygon
from shapely.geometry import box
from shapely.affinity import translate
from ast import literal_eval
import itertools as it

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
        x_bound = room.bounds[2]
        y_bound = room.bounds[3]
        x_trans = 0
        new_geom = self.box
        self.listBounds = []
        while (new_geom.bounds[2]<=x_bound):
            while (new_geom.bounds[3]<=y_bound):
                if (room.contains(new_geom)):
                    self.listBounds.append(new_geom.bounds)
                new_geom = translate(new_geom,0,1)
            x_trans+=1
            new_geom = self.box
            new_geom = translate(new_geom,x_trans)

    def multiple(self, room):
        self.possiblePlacements(room)
        num = self.number
        if (num == 1): return self.listBounds
        check = list(it.combinations(self.listBounds,num))
        if (check == []): return "Too many units for this area"
        return check
        


numberOfChillers = 0
numberOfBoilers = 0
shapeOfRoom = 0
lengthWidthChiller = 0
lengthWidthBoiler = 0
def howMany():
    global numberOfChillers, numberOfBoilers, shapeOfRoom, lengthWidthBoiler, lengthWidthChiller
    shapeOfRoom = literal_eval(input("Enter the coordinates of the room [(0,0),(1,1)...]: "))
    numberOfChillers = literal_eval(input("Enter the number of chillers: "))
    lengthWidthChiller = literal_eval(input("Enter the width and length of chiller [width,length]: "))
    numberOfBoilers = literal_eval(input("Enter the number of boilers: "))
    lengthWidthBoiler = literal_eval(input("Enter the width and length of boiler [width,length]: "))

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def main():
    howMany()
    room1 = Room(shapeOfRoom)
    chiller = Unit(numberOfChillers,lengthWidthChiller)
    print(chiller.multiple(room1.polygon))
    boiler = Unit(numberOfBoilers, lengthWidthBoiler)
    print(boiler.multiple(room1.polygon))
    #print (chiller.possiblePlacements(room1.polygon))
    # print (list(chiller.box.exterior.coords))
    # print (list(room1.polygon.exterior.coords))
    # print (chiller.box.area)
    # print (room1.polygon.area)

    # newRoom = translate(room,0,1)
    # print (list(newRoom.exterior.coords))
    
    # if (room1.polygon.contains(chiller.box)): print('True')
    # else: print ('False')












    
if __name__ == '__main__':
    main()

