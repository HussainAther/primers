import xlrd

path = "hblabprimers.xls"


seq_dict= []

wb = xlrd.open_workbook(path)
sheet = wb.sheet_by_index(0)

for row in range(sheet.nrows):
    
