import openpyxl

wb = openpyxl.load_workbook("売上データ.xlsx")

# -1で末尾のシートを取得する
ws = wb.worksheets[-1]

# 左へ3つ移動させる
wb.move_sheet(ws, offset= -3)
wb.save("売上データ.xlsx")
