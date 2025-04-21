import pandas as pd
import os

def load_all_data(folder_path, data_type='batting'):
    dfs = []
    for year in range(1990, 2024):
        file_path = os.path.join(folder_path, f'{data_type}_{year}.csv')
        if os.path.exists(file_path):
            df = pd.read_csv(file_path)
            df['年份'] = year
            dfs.append(df)
    return pd.concat(dfs, ignore_index=True)

def filter_data(df, team=None, year_start=None, year_end=None):
    if team:
        df = df[df['Team Name'] == team]
    if year_start:
        df = df[df['年份'] >= year_start]
    if year_end:
        df = df[df['年份'] <= year_end]
    return df

