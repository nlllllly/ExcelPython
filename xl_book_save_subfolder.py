import openpyxl
# フォルダを作るためのモジュール読み込み
from pathlib import Path

wb = openpyxl.load_workbook("売上データ.xlsx")
# Copyディレクトリを作成（同名のフォルダがある時は作成しない）
path("Copy").mkdir(exist_ok=Ture)
# コピーを保存
wb.save("Copy/売上データ_copy.xlsx")