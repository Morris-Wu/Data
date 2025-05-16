import pandas as pd
import os

def load_all_data(folder_path, data_type='batting'):
    """
    讀取指定資料夾中所有年度的 CSV 檔案（1990–2023），並加入年份欄位。

    :param folder_path: 資料夾路徑，例如 'data'
    :param data_type: 'batting' 或 'pitching'
    :return: 結合後的 DataFrame，若無資料則回傳空 DataFrame
    """
    dfs = []
    for year in range(1990, 2024):
        file_path = os.path.join(folder_path, f'{data_type}_{year}.csv')
        if os.path.exists(file_path):
            try:
                df = pd.read_csv(file_path)
                df['年份'] = year
                dfs.append(df)
            except Exception as e:
                print(f"[警告] 無法讀取 {file_path}：{e}")
        else:
            print(f"[提示] 找不到檔案：{file_path}")

    if dfs:
        return pd.concat(dfs, ignore_index=True)
    else:
        print("[錯誤] 無可用資料，請確認資料夾與檔案是否存在")
        return pd.DataFrame()


def filter_data(df, team=None, year_start=None, year_end=None):
    """
    根據球隊名稱與年份範圍過濾資料。

    :param df: 原始資料
    :param team: 球隊名稱（完全符合）
    :param year_start: 起始年份（含）
    :param year_end: 結束年份（含）
    :return: 過濾後的 DataFrame
    """
    if team:
        df = df[df['Team Name'] == team]
    if year_start:
        df = df[df['年份'] >= year_start]
    if year_end:
        df = df[df['年份'] <= year_end]
    return df


