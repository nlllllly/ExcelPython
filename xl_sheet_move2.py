import openpyxl

wb = openpyxl.load_workbook("売上データ.xlsx")

# -1で末尾のシートを取得する
ws = wb.worksheets[-1]

# 全部のシート数を計算して、末尾から先頭へ移動させる
to_top = 1 - len(wb.worksheets)
wb.move_sheet(ws, offset=to_top)

wb.save("売上データ.xlsx")