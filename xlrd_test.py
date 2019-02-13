import xlrd

excel_file = 'Dimensions.xlsx'
wb = xlrd.open_workbook(excel_file)
sheet = wb.sheet_by_index(0)

print(sheet.cell_value(0,0))

# print ("Column headings:")
# print (df.columns)