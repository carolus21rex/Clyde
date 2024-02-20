import os
import pandas as pd

# Get a list of all CSV files in the current directory
csv_files = [file for file in os.listdir() if file.endswith('.csv')]

# Iterate over each CSV file
if __name__ == '__main__':

    for file in csv_files:
        # Load the CSV file into a DataFrame
        df = pd.read_csv(file, header=None, names=['Close/Open', 'Open', 'High', 'Low', 'Close', 'Volume'])

        # Iterate over each column (except the first one which is assumed to be a label)
        for column in df.columns[1:]:
            # Calculate the exponential moving average with a window of 5
            df[column] = df[column].ewm(span=5, adjust=False).mean()

        # Drop the first 5 rows
        df = df.iloc[5:]

        # Save the modified DataFrame back to the original CSV file (overwrite)
        df.to_csv(file, index=False)
        # print(df)

        print(f"file {file} is completed.")
