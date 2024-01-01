import os

import dotenv
import pandas as pd
import shutil

dotenv.load_dotenv('venv/.env')


def stapler(folder, filename):
    files = os.listdir(folder)
    data = []
    df = pd.DataFrame()
    for file in files:
        new_df = pd.read_excel(f'{folder}/{file}')
        data.append(new_df)
    df = pd.concat(data)
    df.drop_duplicates('name')

    df.to_excel(f'ready_to_use/{filename}/{filename}.xlsx', index=False, sheet_name=f"{filename}")


if __name__ == '__main__':
    print(os.getenv("WOJEWODZTWO"))
    os.mkdir(f'ready_to_use/{(os.getenv("WOJEWODZTWO")).capitalize()}')
    stapler('output_files', os.getenv("WOJEWODZTWO"))
    files_to_move = os.listdir('output_files')
    os.mkdir(f'archive/{(os.getenv("WOJEWODZTWO")).capitalize()}')
    for file_to_move in files_to_move:
        shutil.move(f"output_files/{file_to_move}", f'archive/{os.getenv("WOJEWODZTWO")}/')
