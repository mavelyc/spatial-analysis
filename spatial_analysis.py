# import matplotlib.pyplot as plt
# plt.plot([1,2,3],[5,7,4])
# plt.show()

from shapely.geometry import Polygon
from shapely.geometry import MultiPolygon
from shapely.geometry import box
from shapely.affinity import translate
from ast import literal_eval
import itertools as it
import matplotlib.pyplot as plt

numberOfChillers = 0
numberOfBoilers = 0
shapeOfRoom = 0
lengthWidthChiller = 0
lengthWidthBoiler = 0


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
        return self.listBounds

    def multiple(self, room):
        self.possiblePlacements(room)
        num = self.number
        if (num == 1): return self.listBounds
        check = list(it.combinations(self.listBounds,num))
        if (check == []): return "Too many units for this area"
        self.multiList = check

    def boundaryCheck(self, val1, val2):
        # print (val1,val2)
        min_y_2 = val2[1]
        max_y_2 = val2[3]
        min_y_1 = val1[1]
        max_y_1 = val1[3]
        
        min_x_2 = val2[0]
        max_x_2 = val2[2]
        min_x_1 = val1[0]
        max_x_1 = val1[2]

        if (min_y_2 >= max_y_1 or min_y_1 >= max_y_2):
            #print ("True")
            return True
        elif (min_x_2 >= max_x_1 or min_x_1 >= max_x_2):
            #print ("True")
            return True


    def clearOverlaps(self):
        i=0
        flag = 0
        tmp = []
        if (self.number == 1): return
        for tup in self.multiList:
            # print (tup)
            # print (flag)
            while (i<self.number):
                val = tup[i]
                # print(val)
                for elem in tup:
                    if (elem == val): 
                        continue
                    else:
                        bool_check = self.boundaryCheck(val,elem)
                        if (bool_check != True): 
                            flag = 1                    
                i+=1
            if (flag == 0): tmp.append(tup)
            bool_check = False
            flag = 0
            i=0     
        self.multiList = tmp
        return self.multiList
        #print (self.multiList)


def howMany():
    global numberOfChillers, numberOfBoilers, shapeOfRoom, lengthWidthBoiler, lengthWidthChiller
    shapeOfRoom = literal_eval(input("Enter the coordinates of the room [(0,0),(1,1)...]: "))
    numberOfChillers = literal_eval(input("Enter the number of chillers: "))
    lengthWidthChiller = literal_eval(input("Enter the width and length of chiller [width,length]: "))
    numberOfBoilers = literal_eval(input("Enter the number of boilers: "))
    lengthWidthBoiler = literal_eval(input("Enter the width and length of boiler [width,length]: "))


def boundsCheck(val1, val2):
        # print (val1,val2)
        min_y_2 = val2[1]
        max_y_2 = val2[3]
        min_y_1 = val1[1]
        max_y_1 = val1[3]
        
        min_x_2 = val2[0]
        max_x_2 = val2[2]
        min_x_1 = val1[0]
        max_x_1 = val1[2]

        if (min_y_2 >= max_y_1 or min_y_1 >= max_y_2):
            #print ("True")
            return True
        elif (min_x_2 >= max_x_1 or min_x_1 >= max_x_2):
            #print ("True")
            return True
        
    
def finalConfigurations(tup1, tup2):
    final = []
    flag = 0

    for i in tup1:
        for test in tup2:
            for tup in i:
                for check in test:
                    #print (tup,check)
                    if(boundsCheck(tup,check)!=True): flag = 1
                    #print (flag)
                #print (flag)
            if (flag==0):
                final.append(i+test)
            flag = 0

    return final    


def roomTupToList(listOfTups):
    ListofLists = []
    for i in listOfTups:
        ListofLists.append(list(i))
    return (ListofLists)


def drawRoom(coordsOfRoom):
    points = coordsOfRoom
    polygon = plt.Polygon(points, closed=True)
    return polygon

def initAxis():
    plt.axes()

def showAxis():
    plt.axis('scaled')
    plt.show()

def finalTupToCoords(coordinates):
    final = []
    for i in coordinates:
        tmp = []
        for each in i:
            tmp.append(list(each))
        final.append(tmp)
    print (final)



#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def main():
    howMany()
    room1 = Room(shapeOfRoom)
    chiller = Unit(numberOfChillers,lengthWidthChiller)
    boiler = Unit(numberOfBoilers, lengthWidthBoiler)
    chiller.multiple(room1.polygon)
    # chiller.clearOverlaps()
    boiler.multiple(room1.polygon)
    # boiler.clearOverlaps()
    finalConfig = finalConfigurations(chiller.clearOverlaps(),boiler.clearOverlaps())
    finalTupToCoords(finalConfig)
    

    colors = ["g","r","c","m","y","k","w"]

    initAxis()
    room = drawRoom(roomTupToList(shapeOfRoom))
    plt.gca().add_patch(room)
    points2 = [[0,0],[1,1],[1,0]]
    polygon2 = plt.Polygon(points2, closed=True, color=colors[2])
    plt.gca().add_patch(polygon2)


    showAxis()



if __name__ == '__main__':
    main()

