from shapely.geometry import Polygon
from shapely.geometry import MultiPolygon
from shapely.geometry import box
from shapely.affinity import translate
from ast import literal_eval
import itertools as it
import matplotlib.pyplot as plt
import xlrd_test

numberOfChillers = 0
numberOfBoilers = 0
shapeOfRoom = 0
lengthWidthChiller = 0
lengthWidthBoiler = 0
numberOfAHUs = 0
lengthWidthAHU =0 
numberOfPumps = 0
lengthWidthPump =0 


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
        self.listBounds

    def multiple(self, room):
        self.possiblePlacements(room)
        num = self.number
        if (num == 1): return self.listBounds
        check = list(it.combinations(self.listBounds,num))
        if (check == []): print ("Too many units for this area")
        self.multiList = check

    def boundaryCheck(self, val1, val2):
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
        if (self.number == 1): return self.multiList
        for tup in self.multiList:
            while (i<self.number):
                val = tup[i]
                for elem in tup:
                    if (elem != val): 
                        bool_check = self.boundaryCheck(val,elem)
                        if (bool_check != True): 
                            flag = 1                    
                i+=1
            if (flag == 0): tmp.append(tup)
            bool_check = False
            flag = 0
            i=0     
        self.multiList = tmp
        #return self.multiList
        #print (self.multiList)


def howMany():
    global numberOfChillers, numberOfBoilers, shapeOfRoom, lengthWidthBoiler, lengthWidthChiller, numberOfAHUs, lengthWidthAHU, numberOfPumps, lengthWidthPump
    shapeOfRoom = xlrd_test.readRoom()
    numberOfChillers = xlrd_test.readChillerNumber()
    print (numberOfChillers)
    if numberOfChillers>0:
        lengthWidthChiller = literal_eval(input("Enter the width and length of chiller [width,length]: "))
    numberOfBoilers = literal_eval(input("Enter the number of boilers: "))
    if numberOfBoilers>0:
        lengthWidthBoiler = literal_eval(input("Enter the width and length of boiler [width,length]: "))
    numberOfAHUs = literal_eval(input("Enter the number of AHUs: "))
    if numberOfAHUs>0:
        lengthWidthAHU = literal_eval(input("Enter the width and length of AHU [width,length]: "))
    numberOfPumps = literal_eval(input("Enter the number of pumps: "))
    if numberOfPumps>0:
        lengthWidthPump = literal_eval(input("Enter the width and length of pump [width,length]: "))


def boundsCheck(val1, val2):
        min_y_2 = val2[1]
        max_y_2 = val2[3]
        min_y_1 = val1[1]
        max_y_1 = val1[3]
        
        min_x_2 = val2[0]
        max_x_2 = val2[2]
        min_x_1 = val1[0]
        max_x_1 = val1[2]

        if (min_y_2 >= max_y_1 or min_y_1 >= max_y_2): return True
        elif (min_x_2 >= max_x_1 or min_x_1 >= max_x_2): return True
        
    
def finalConfigurations(tup1, tup2):
    if (tup1 == 0):
        return tup2
    if (tup2 == 0): 
        return tup1
    final = []
    flag = 0

    for i in tup1:
        #print("test")
        for test in tup2:
            #print ("test1")
            for tup in i:
                for check in test:
                    #print ("test3")
                    if(boundsCheck(tup,check)!=True): flag = 1
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
        tmp2 = []
        for bounds in i:
            tmp=[]
            tup = (bounds[0],bounds[1])
            width = bounds[2]-bounds[0]
            length = bounds[3]-bounds[1]
            tmp.append(tup)
            tmp.extend([width,length])
            tmp2.append(tuple(tmp))
        final.append(tmp2)
    return final
    
        



#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def main():
    global numberOfChillers, numberOfBoilers, shapeOfRoom, lengthWidthBoiler, lengthWidthChiller, numberOfAHUs, lengthWidthAHU, numberOfPumps, lengthWidthPump
    #try:
    
    howMany()
    room1 = Room(shapeOfRoom)

    chiller_val = 0
    boiler_val = 0
    AHU_val = 0
    pump_val = 0

    if (numberOfChillers>0):
        chiller = Unit(numberOfChillers,lengthWidthChiller)
        chiller.multiple(room1.polygon)
        chiller.clearOverlaps()
        chiller_val = chiller.multiList
    if (numberOfBoilers>0):
        boiler = Unit(numberOfBoilers, lengthWidthBoiler)
        boiler.multiple(room1.polygon)
        boiler.clearOverlaps()
        boiler_val = boiler.multiList
    if (numberOfAHUs>0):
        AHU = Unit(numberOfAHUs, lengthWidthAHU)
        AHU.multiple(room1.polygon)
        AHU.clearOverlaps()
        AHU_val = AHU.multiList
    if (numberOfPumps>0):
        pump = Unit(numberOfPumps, lengthWidthPump)
        pump.multiple(room1.polygon)
        pump.clearOverlaps()
        pump_val = pump.multiList

    # finalConfig1 = finalConfigurations(chiller_val,boiler_val)
    # finalConfig2 = finalConfigurations(AHU_val, pump_val)
    finalConfig = finalConfigurations(finalConfigurations(chiller_val,boiler_val),finalConfigurations(AHU_val, pump_val))
    finalList = finalTupToCoords(finalConfig)
    #print(finalConfig)

    initAxis()

    r = 0
    while(1):
        room = drawRoom(roomTupToList(shapeOfRoom))
        plt.gca().add_patch(room)
        r = r%(len(finalList))
        # finalList = finalTupToCoords(finalConfig2)
        #colors = ["g","r","c","m","y","k","w"]
        #j= 0
        #j=j%6
        for i in finalList[r]:
            #j+=1
            polygon2 = plt.Rectangle(*i,fc="r",edgecolor="b")
            plt.gca().add_patch(polygon2)

        showAxis()
        command = input("Press Enter to view more options or press X/x to close: ")
        if (command == "X" or command == "x"): break
        r+=1

    #except:
        # print ("Not possible")


if __name__ == '__main__':
    main()

