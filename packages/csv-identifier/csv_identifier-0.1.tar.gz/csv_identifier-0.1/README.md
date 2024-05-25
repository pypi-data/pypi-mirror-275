# csv_identifier

`csv_identifier` is a Python package that reads a CSV file, converts it to a DataFrame, and assigns a unique identifier to a specified column.

## Installation

You can install the package using pip:

```sh
pip install csv_identifier
```

## Usage

Here is an example of how to use the package:

```python
from csv_identifier import assign_unique_ids

# Path to your CSV file
csv_file_path = 'path/to/your/file.csv'

# Column to which you want to assign unique IDs
column_name = 'column_name'

# Assign unique IDs and get the DataFrame
df = assign_unique_ids(csv_file_path, column_name)

# Display the DataFrame
print(df)
```

## Function

### assign_unique_ids

```python
assign_unique_ids(csv_file_path, column_name)
```

- **csv_file_path**: Path to the CSV file.
- **column_name**: The column to which you want to assign unique IDs.

This function reads the CSV file, assigns unique IDs to the specified column, and returns the modified DataFrame.