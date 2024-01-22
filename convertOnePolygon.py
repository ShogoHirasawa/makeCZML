import geopandas as gpd
from shapely.ops import unary_union
import os

# ファイル選択のための関数
def select_geojson_files():
    import tkinter as tk
    from tkinter import filedialog

    root = tk.Tk()
    root.withdraw()  # Tkウィンドウを表示しない
    file_paths = filedialog.askopenfilenames(filetypes=[("GeoJSON files", "*.geojson")])
    return file_paths

# 選択されたファイルのリスト
selected_files = select_geojson_files()

# 各ファイルを処理
for file_path in selected_files:
    # GeoJSONファイルの読み込み
    gdf = gpd.read_file(file_path)

    # 全てのポリゴンを結合
    combined_polygon = unary_union(gdf.geometry)

    # 新しいGeoDataFrameの作成
    new_gdf = gpd.GeoDataFrame(geometry=[combined_polygon])

    # 出力ファイル名の設定
    output_file = os.path.splitext(os.path.basename(file_path))[0] + '_combined.geojson'

    # 結合されたポリゴンを含む新しいGeoJSONファイルの保存
    new_gdf.to_file(output_file, driver='GeoJSON')

print("処理が完了しました。")
