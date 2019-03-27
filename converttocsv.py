import xlrd
import csv

def csv_from_excel():
    
    wb = xlrd.open_workbook('HBlabprimers.xls')
    sh = wb.sheet_by_name('HB lab primers')
    your_csv_file = open('HBlabprimers.csv', 'w')
    wr = csv.writer(your_csv_file, delimiter=",", quoting=csv.QUOTE_ALL)

    for rownum in range(sh.nrows):
        wr.writerow(sh.row_values(rownum))

    your_csv_file.close()

csv_from_excel()
