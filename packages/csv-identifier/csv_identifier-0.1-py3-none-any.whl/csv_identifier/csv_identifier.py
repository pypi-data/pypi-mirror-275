import pandas as pd

def assign_unique_ids(csv_file_path, column_name):
    df = pd.read_csv(csv_file_path)

    df[column_name + '_id'] = pd.factorize(df[column_name])[0] + 1    
    return df