import openpyxl

wb = openpyxl.load_workbook("売上データ.xlsx")

ws = wb.worksheets[0]
wb.remove(ws)

wb.save("売上データ.xlsx")