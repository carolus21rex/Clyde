import os
import pandas as pd

# Get the current directory
current_directory = os.getcwd()

# List all files in the directory
files = os.listdir(current_directory)

# Filter only CSV files
csv_files = [file for file in files if file.endswith('.csv')]

# Iterate through each CSV file
for file in csv_files:
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file, header=None)

    # Modify the 0th index column
    df.iloc[:, 0] = df.iloc[:, 4] / df.iloc[:, 1]

    # Save the modified DataFrame back to the CSV file
    df.to_csv(file, index=False)
    print(f"file: {file} is complete.")
