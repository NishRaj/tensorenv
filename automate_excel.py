from openpyxl import Workbook, load_workbook

wb = load_workbook('Security.xlsx')
ws = wb.active
# Access the value
print(ws['A1'].value)
# Change the value
ws['A2'].value = "Nishank"
# Need to save the workbook
wb.save("Security.xlsx")
