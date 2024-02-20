import os
import pandas as pd

# Function to check if any column dtype is not float64 and delete the file
def check_and_delete_file(file_path):
    df = pd.read_csv(file_path, header=None)
    # Check if any column dtype is not float64 or int64
    for col in df.columns:
        col_dtype = df[col].dtype
        if col_dtype != 'float64' and col_dtype != 'int64':
            print(f"File '{file_path}' contains non-float nor non-int {col_dtype} values. Deleting the file...")
            os.remove(file_path)
            break  # Exit the loop after printing the message for the first non-float or non-int column

# Get list of all CSV files in the current directory
csv_files = [file for file in os.listdir() if file.endswith('.csv')]

# Iterate over each CSV file
for file_name in csv_files:
    file_path = os.path.join(os.getcwd(), file_name)  # Full path to the CSV file
    check_and_delete_file(file_path)
