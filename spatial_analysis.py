# import matplotlib.pyplot as plt
# plt.plot([1,2,3],[5,7,4])
# plt.show()

from shapely.geometry import Polygon
from shapely.geometry import MultiPolygon
from shapely.geometry import box
from shapely.affinity import translate
from ast import literal_eval
import itertools as it

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

def finalTuple(list1, list2):
    return list(it.product(list1,list2))


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
        return self.multiList

    def boundaryCheck(self, val1, val2):
        #print (val1,val2)
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
                        # box1 = box(*val)
                        # box2 = box(*elem)
                        # bool_check = box1.intersects(box2)
                        if (bool_check == True): 
                            flag = 1                    
                i+=1
            if (flag == 1): tmp.append(tup)
            bool_check = False
            flag = 0
            i=0     
        self.multiList = tmp
        print (tmp)
        
    

# def finalConfigurations(finalList):
#     final = []
#     flag = 0

#     #SPECIAL Needed CASE IF NUMBER OF BOILERS AND CHILLERS ARE 1 EACH

#     for tup in finalList:
#         #print (tup)
#         for first in tup[0]:
#             print (first)
#             box1 = box(*first)
#             for second in tup[1]:
#                 print (second)
#                 box2 = box(*second)
#                 bool_check = box1.intersects(box2)
#     #             if (bool_check == True): 
#     #                 print("True")
#     #                 flag = 1
#     #         if (flag==1): break
#     #     if (flag==0): final.append(tup)
#     #     flag = 0
#     # if (final == []): print ("No possible combination of units will fit in room")
#     # return final




#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def main():
    howMany()
    room1 = Room(shapeOfRoom)
    chiller = Unit(numberOfChillers,lengthWidthChiller)
    boiler = Unit(numberOfBoilers, lengthWidthBoiler)
    listaz1 = chiller.possiblePlacements(room1.polygon)
    print(listaz1)
    listaz2 = chiller.multiple(room1.polygon)
    print(listaz2)
    print("---------------------------------------------")
    chiller.clearOverlaps()
    #listaz2 = boiler.multiple(room1.polygon)
    #print(listaz2)
    #print(finalConfigurations(finalTuple(listaz1,listaz2)))
    # print (list(chiller.box.exterior.coords))
    # print (list(room1.polygon.exterior.coords))

    # if (room1.polygon.contains(chiller.box)): print('True')
    # else: print ('False')












    
if __name__ == '__main__':
    main()

