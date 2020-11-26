import openpyxl

wb = openpyxl.load_workbook("売上データ.xlsx")

# シート名の変更
ws = wb["Sheet1"]
ws.title = "第1四半期"

wb.save("売上データ.xlsx")