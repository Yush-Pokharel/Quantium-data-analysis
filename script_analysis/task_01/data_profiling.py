import pandas as pd
import os


raw_data_files = ['QVI_purchase_behaviour.csv', 'QVI_transaction_data.xlsx']


def get_df():
    dfs = {}

    profiling_script_path = os.path.dirname(os.path.abspath(__file__))
    raw_data_dir = os.path.join(profiling_script_path, '..', 'raw_data')

    for file in raw_data_files:
        raw_data_file_path = os.path.join(raw_data_dir, file)
        if file.endswith('.csv'):
            dfs[file] = pd.read_csv(raw_data_file_path)
        elif file.endswith('.xlsx'):
            dfs[file] = pd.read_excel(raw_data_file_path)
    return dfs


if __name__ == "__main__":
    dataframes = get_df()

    print("Data Profiling \n")
    print(f"-"*50)

    for file_name, df in dataframes.items():

        print(f"\nDataframe of {file_name}")
        print(df.head())
        df.info()
        print(df.describe(include='all'))


