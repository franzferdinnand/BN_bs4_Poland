import datetime
import pandas as pd


def refactor_and_save_to_excel(data, num) -> None:
    df = pd.DataFrame(data=data,
                      columns=['name', 'nip', 'street', 'zip', 'city', 'woj',  'web',  'telephone', 'email'])

    df['email'] = [str(x).replace(",",
                                  ";").replace("[",
                                               "").replace("]",
                                                           "").replace("'",
                                                                       "") for x in
                   df['email'].values]

    df['telephone'] = [str(x).replace("[",
                                      "").replace("]",
                                                  "").replace("'",
                                                              "") for x in df['telephone'].values]

    df['web'] = [str(x).replace("[",
                                      "").replace("]",
                                                  "").replace("'",
                                                              "") for x in df['web'].values]

    df.to_excel(f'output_files/database_{datetime.date.today()}_{num}.xlsx',
                sheet_name=f'poland{num}', index=False)