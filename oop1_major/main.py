import openpyxl
from CSpace import CSpace

wb = openpyxl.load_workbook('cSpace_booking.xlsx')
cspace = CSpace(wb)
print("Please enter a date from selection:")
for name in wb.sheetnames:
    if name != 'Clients' and name != 'Rates' and name != 'Facilities':
        print(name)
date = input()
print(cspace.run(date))


