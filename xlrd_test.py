import xlrd


excel_file = 'Dimensions.xlsx'
wb = xlrd.open_workbook(excel_file)
sheet = wb.sheet_by_index(0)

def readRoom():

    room_coordinates = []

    for i in range(1,sheet.nrows):
        room_coordinates.append(eval(sheet.cell_value(i,0)))

    return room_coordinates

def readChillerNumber():
    return int(sheet.cell_value(1,3))



    