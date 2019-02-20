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

def readChillerBounds():
    chiller_bounds = []
    chiller_bounds.append(sheet.cell_value(2,3))
    chiller_bounds.append(sheet.cell_value(3,3))
    return chiller_bounds

def readBoilerNumber():
    return int(sheet.cell_value(1,6))

def readBoilerBounds():
    boiler_bounds = []
    boiler_bounds.append(sheet.cell_value(2,6))
    boiler_bounds.append(sheet.cell_value(3,6))
    return boiler_bounds

def readAHUNumber():
    return int(sheet.cell_value(1,9))

def readAHUBounds():
    AHU_bounds = []
    AHU_bounds.append(sheet.cell_value(2,9))
    AHU_bounds.append(sheet.cell_value(3,9))
    return AHU_bounds
    
def readPumpNumber():
    return int(sheet.cell_value(1,12))

def readPumpBounds():
    Pump_bounds = []
    Pump_bounds.append(sheet.cell_value(2,12))
    Pump_bounds.append(sheet.cell_value(3,12))
    return Pump_bounds

def readNumberUnit5():
    return int(sheet.cell_value(1,15))

def readUnit5Bounds():
    Unit5_bounds = []
    Unit5_bounds.append(sheet.cell_value(2,15))
    Unit5_bounds.append(sheet.cell_value(3,15))
    return Unit5_bounds

def readNumberUnit6():
    return int(sheet.cell_value(1,18))

def readUnit6Bounds():
    Unit6_bounds = []
    Unit6_bounds.append(sheet.cell_value(2,18))
    Unit6_bounds.append(sheet.cell_value(3,18))
    return Unit6_bounds

def readNumberUnit7():
    return int(sheet.cell_value(1,21))

def readUnit7Bounds():
    Unit7_bounds = []
    Unit7_bounds.append(sheet.cell_value(2,21))
    Unit7_bounds.append(sheet.cell_value(3,21))
    return Unit7_bounds

def readNumberUnit8():
    return int(sheet.cell_value(1,24))

def readUnit8Bounds():
    Unit8_bounds = []
    Unit8_bounds.append(sheet.cell_value(2,24))
    Unit8_bounds.append(sheet.cell_value(3,24))
    return Unit8_bounds