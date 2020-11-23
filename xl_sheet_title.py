import openpyxl

wb = openpyxl.load_workbook("売上データ.xlsx")
# シートの指定
ws = wb["4月"]
print(ws.title)

# シートの指定
ws2 = wb.worksheets[1]
print(ws2.title)