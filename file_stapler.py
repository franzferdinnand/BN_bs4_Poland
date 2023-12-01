import os
import pandas as pd


def stapler(folder, filename):
    files = os.listdir(folder)
    data = []
    df = pd.DataFrame()
    for file in files:
        new_df = pd.read_excel(f'output_files/{file}')
        data.append(new_df)
    df = pd.concat(data)
    df.drop_duplicates('name')
    df.to_excel(f'{filename}.xlsx', index=False, sheet_name=f"{filename}")


if __name__ == '__main__':
    stapler('output_files', 'Poland_mazowieckie')
