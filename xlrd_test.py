import xlrd

def readRoom():
    global numberOfChillers, numberOfBoilers, shapeOfRoom, lengthWidthBoiler, lengthWidthChiller, numberOfAHUs, lengthWidthAHU, numberOfPumps, lengthWidthPump
    excel_file = 'Dimensions.xlsx'
    wb = xlrd.open_workbook(excel_file)
    sheet = wb.sheet_by_index(0)

    room_coordinates = []

    for i in range(1,sheet.nrows):
        # print (eval(sheet.cell_value(i,0)),sheet.cell_value(i,0))
        room_coordinates.append(eval(sheet.cell_value(i,0)))

    return room_coordinates

    