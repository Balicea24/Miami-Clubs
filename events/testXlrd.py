import xlrd
from MiamiClubsEvents import getInfo
import os

pre = os.path.dirname(os.path.realpath(__file__))
fname = 'ClubsInfo.xls'
path = os.path.join(pre, fname)
book = xlrd.open_workbook(path, 'r')
sheet = book.sheet_by_name('Space')

for row in range(sheet.nrows):
    date = sheet.cell(row, 1).value
    date = str(date[4:6]) + "." + str(date[6::])
#    sheet.write(row, 6, date)
    print (date)
