import openpyxl

wb = openpyxl.load_workbook("売上データ.xlsx")
ws = wb["4月"]

for row in ws.iter_rows(min_row=4):
    if row[0].value is None:
        break
    value_lst = []
    for c in row:
        value_lst.append(c.value)
    print(value_lst)