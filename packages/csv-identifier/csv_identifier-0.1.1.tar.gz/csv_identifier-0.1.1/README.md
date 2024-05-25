# csv_identifier

`csv_identifier` is a Python package that reads a CSV file, Excel file, or DataFrame, converts it to a DataFrame if necessary, and assigns a unique identifier to a specified column.

`csv_identifier` は、CSV ファイル、Excel ファイル、または DataFrame を読み込み、必要に応じて DataFrame に変換し、指定したカラムに一意な識別子を割り当てる Python パッケージです。

## Installation

You can install the package using pip:

パッケージはpipを使用してインストールできます：
```sh
pip install csv_identifier
```

## Usage

Here is an example of how to use the package:

パッケージの使用例は以下の通りです：

```python
from csv_identifier import assign_unique_ids
import pandas as pd

# Path to your CSV file
csv_file_path = 'path/to/your/file.csv'

# Path to your Excel file
excel_file_path = 'path/to/your/file.xlsx'

# Example DataFrame
data = {'column_name': ['A', 'B', 'A', 'C']}
df = pd.DataFrame(data)

# Column to which you want to assign unique IDs
column_name = 'column_name'

# Assign unique IDs from CSV file
df_from_csv = assign_unique_ids(csv_file_path, column_name)
print(df_from_csv)

# Assign unique IDs from Excel file
df_from_excel = assign_unique_ids(excel_file_path, column_name)
print(df_from_excel)

# Assign unique IDs from DataFrame
df_from_df = assign_unique_ids(df, column_name)
print(df_from_df)
```

## Function

### assign_unique_ids

```python
assign_unique_ids(data, column_name)
```

- **data**
  - Path to the CSV/Excel file or a DataFrame.
  - CSV/ExcelファイルのパスまたはDataFrame
- **column_name**
  - The column to which you want to assign unique IDs.
  -  一意のIDを割り当てたいカラム


This function reads the data, assigns unique IDs to the specified column, and returns the modified DataFrame.

この関数はデータを読み込み、指定されたカラムに一意のIDを割り当て、変更されたDataFrameを返します。