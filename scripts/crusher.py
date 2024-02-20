import pandas as pd
import os

# Get the current directory
folder_path = os.getcwd()

# Get a list of all CSV files in the current directory
csv_files = [file for file in os.listdir(folder_path) if file.endswith('.csv')]

# Define the function to transform each CSV file
def transform_csv(file_path):
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(file_path, header=None, names=['Close/Open', 'Open', 'High', 'Low', 'Close', 'Volume'])

    # Calculate the required columns
    for i in range(1, 4):
        for col in ['Open', 'High', 'Low', 'Close', 'Volume']:
            df[f"{col}(-{i})"] = df[col].shift(i)

    # Reorder the columns as per the desired layout
    new_columns = ['Close/Open'] + [f'{col}(-{i})' for i in range(1, 4) for col in
                                    ['Open', 'High', 'Low', 'Close', 'Volume']]
    transformed_df = df[new_columns]

    # Remove rows with any NaN values in new_columns
    transformed_df = transformed_df.dropna(subset=new_columns)

    # Write the transformed DataFrame back to CSV
    transformed_df.to_csv(file_path, index=False)

    print(f"Successfully wrote transformation for file: {file_path}")

# Apply the transformation to each CSV file
for file in csv_files:
    transform_csv(os.path.join(folder_path, file))
