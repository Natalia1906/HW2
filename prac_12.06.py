import openpyxl
import json

workbook = openpyxl.load_workbook("work (1).xlsx")
worksheet = workbook.active
print(worksheet.cell(1,1).value)
