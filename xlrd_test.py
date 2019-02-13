import xlrd

excel_file = 'Dimensions.xlsx'
wb = xlrd.open_workbook(excel_file)
sheet = wb.sheet_by_index(0)

for i in range(1,sheet.nrows):
    print (sheet.cell_value(i,0))
# print ("Column headings:")
# print (df.columns)