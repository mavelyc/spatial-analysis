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

numberUnit5 =0
lengthWidthUnit5=0
numberUnit6=0
lengthWidthUnit6=0
numberUnit7=0
lengthWidthUnit7=0
numberUnit8=0
lengthWidthUnit8=0


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
            #print(len(self.listBounds))
            #if (len(self.listBounds)>100000): break
        self.listBounds

    def multiple(self, room):
        self.possiblePlacements(room)
        num = self.number
        if (num == 1): 
            one_it = []
            for i in self.listBounds:
                tmp_i = [i]
                one_it.append(tmp_i)
            self.multiList = one_it
        else:
            check = list(self.combinations(self.listBounds,num))
            # if (check == []): print ("Too many units for this area")
            self.multiList = check

    def boundaryCheck(self, val1, val2):
        if (val2[1] >= val1[3] or val1[1] >= val2[3]): return True
        elif (val2[0] >= val1[2] or val1[0] >= val2[2]): return True

    def combinations(self, iterable, r):
        pool = tuple(iterable)
        n = len(pool)
        # if n>100000: n=100000
        count=0
        for indices in it.permutations(range(n), r):
            count+=1
            if sorted(indices) == list(indices):
                yield tuple(pool[i] for i in indices)

    def clearOverlaps(self):
        i=0
        flag = 0
        tmp = []
        if (self.number != 1):
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
                if(len(tmp)>5000): break
            self.multiList = tmp
            #return self.multiList


def howMany():
    global numberOfChillers, numberOfBoilers, shapeOfRoom, lengthWidthBoiler, lengthWidthChiller, numberOfAHUs, lengthWidthAHU 
    global numberOfPumps, lengthWidthPump, numberUnit5, lengthWidthUnit5, numberUnit6, lengthWidthUnit6, numberUnit7, lengthWidthUnit7, lengthWidthUnit8, numberUnit8
    shapeOfRoom = xlrd_test.readRoom()
    numberOfChillers = xlrd_test.readChillerNumber()
    if numberOfChillers>0:
        lengthWidthChiller = xlrd_test.readChillerBounds()
    numberOfBoilers = xlrd_test.readBoilerNumber()
    if numberOfBoilers>0:
        lengthWidthBoiler = xlrd_test.readBoilerBounds()
    numberOfAHUs = xlrd_test.readAHUNumber()
    if numberOfAHUs>0:
        lengthWidthAHU = xlrd_test.readAHUBounds()
    numberOfPumps = xlrd_test.readPumpNumber()
    if numberOfPumps>0:
        lengthWidthPump = xlrd_test.readPumpBounds() 
    numberUnit5 = xlrd_test.readNumberUnit5()
    if numberUnit5>0:
        lengthWidthUnit5 = xlrd_test.readUnit5Bounds()
    numberUnit6 = xlrd_test.readNumberUnit6()
    if numberUnit6>0:
        lengthWidthUnit6 = xlrd_test.readUnit6Bounds()
    numberUnit7 = xlrd_test.readNumberUnit7()
    if numberUnit7>0:
        lengthWidthUnit7 = xlrd_test.readUnit7Bounds()
    numberUnit8 = xlrd_test.readNumberUnit8()
    if numberUnit8>0:
        lengthWidthUnit8 = xlrd_test.readUnit8Bounds()

def boundsCheck(val1, val2):
        if (val2[1] >= val1[3] or val1[1] >= val2[3]): return True
        elif (val2[0] >= val1[2] or val1[0] >= val2[2]): return True

def finalConfigurations(tup1, tup2):
    if (tup1 == 0):
        print ("tup2=" , len(tup2))
        print("---------------------------------")
        return tup2

    if (tup2 == 0): 
        print ("tup1=" , len(tup1))
        print("---------------------------------")
        return tup1
        
    print ("tup1=" , len(tup1))
    print ("tup2=" , len(tup2))
    final = []
    flag = 0
    for i in tup1:
        #print(i)
        for test in tup2:
            # print(test)
            for tup in i:
                #print(tup)
                for check in test:
                    if(boundsCheck(tup,check)!=True): flag = 1
            if (flag==0):
                print("in list")
                if (type(test) == list and type(i)==list):
                    tmp = list(i)
                    # print (tmp)
                    # print (i,test)
                    for j in test:
                        # print (j)
                        tmp.append(j)
                    final.append(tmp)
                elif (type(test) == list):
                    final.append(i+tuple(test))
                elif (type(i) == list):
                    final.append(tuple(i) + test) 
                else:
                    final.append(i+test)
            flag = 0
        if (len(final)>10000):
            break
    # print ("-----------------")
    print (len(final))
    print("---------------------------------")
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
    print(final)
    return final
      

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def main():
    # try:
    howMany()
    room1 = Room(shapeOfRoom)

    total = 0

    chiller_val = 0
    boiler_val = 0
    AHU_val = 0
    pump_val = 0
    unit5_val = 0
    unit6_val = 0
    unit7_val = 0
    unit8_val = 0

    if (numberOfChillers>0):
        chiller = Unit(numberOfChillers,lengthWidthChiller)
        chiller.multiple(room1.polygon)
        chiller.clearOverlaps()
        chiller_val = chiller.multiList
        total+=1
    if (numberOfBoilers>0):
        boiler = Unit(numberOfBoilers, lengthWidthBoiler)
        boiler.multiple(room1.polygon)
        boiler.clearOverlaps()
        boiler_val = boiler.multiList
        total+=1
    if (numberOfAHUs>0):
        AHU = Unit(numberOfAHUs, lengthWidthAHU)
        AHU.multiple(room1.polygon)
        AHU.clearOverlaps()
        AHU_val = AHU.multiList
        total+=1
    if (numberOfPumps>0):
        pump = Unit(numberOfPumps, lengthWidthPump)
        pump.multiple(room1.polygon)
        pump.clearOverlaps()
        pump_val = pump.multiList
        total+=1
    if (numberUnit5>0):
        unit5 = Unit(numberUnit5, lengthWidthUnit5)
        unit5.multiple(room1.polygon)
        unit5.clearOverlaps()
        unit5_val = unit5.multiList
        total+=1
    if (numberUnit6>0):
        unit6 = Unit(numberUnit6, lengthWidthUnit6)
        unit6.multiple(room1.polygon)
        unit6.clearOverlaps()
        unit_val = unit6.multiList
        total+=1

    total=4

    # print (total)
    if (total==1 or total==2):
        finalConfig = finalConfigurations(chiller_val,boiler_val)
        finalList = finalTupToCoords(finalConfig)
    elif(total==3 or total==4):
        finalConfig = finalConfigurations(finalConfigurations(chiller_val,boiler_val),finalConfigurations(AHU_val, pump_val))
        finalList = finalTupToCoords(finalConfig)
    elif(total==5 or total==6 or total==7 or total==8):
        tmp1 = finalConfigurations(chiller_val,boiler_val)
        print("1")
        tmp2 = finalConfigurations(AHU_val, pump_val)
        print("2")
        tmp3 = finalConfigurations(tmp1,tmp2)
        print("3")
        tmp4 = finalConfigurations(unit5_val,unit6_val)
        print("4")
        tmp5 = finalConfigurations(unit7_val, unit8_val)
        print("5")
        tmp6 = finalConfigurations(tmp4,tmp5)
        print("6")
        finalConfig = finalConfigurations(tmp3,tmp6)
        print("fC")
        finalList = finalTupToCoords(finalConfig)
        print("fL")

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

    # except:
    #     print ("Not possible")


if __name__ == '__main__':
    main()

