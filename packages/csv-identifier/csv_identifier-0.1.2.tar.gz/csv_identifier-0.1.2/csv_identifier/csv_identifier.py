import pandas as pd

def assign_unique_ids(data, column_name):
    if isinstance(data, str):
        if data.endswith('.csv'):
            df = pd.read_csv(data)
        elif data.endswith('.xlsx') or data.endswith('.xls'):
            df = pd.read_excel(data)
        else:
            raise ValueError("Unsupported file type. Please provide a CSV or Excel file.")
    elif isinstance(data, pd.DataFrame):
        df = data.copy()
    else:
        raise ValueError("Unsupported data type. Please provide a file path or a DataFrame.")

    df[column_name + '_id'] = pd.factorize(df[column_name])[0] + 1    
    return df