import pandas as pd
import os

# Get the current directory
folder_path = os.getcwd()

# Get a list of all CSV files in the current directory
csv_files = [file for file in os.listdir(folder_path) if file.endswith('.csv')]


# Define the function to calculate the covariance for each CSV file
def calculate_covariance(file_path):
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(file_path)

    # Calculate the covariance between the specified columns
    columns = df.columns
    covariances = {}
    for i in range(1, 4):
        for col in columns:
            if col != 'Close/Open':
                # Adjusted column name construction
                target_col = f"{col}"
                covariance = df['Close/Open'].cov(df[target_col]) * len(df)
                covariances[target_col] = covariance

    # Calculate the total count of rows
    total_rows = len(df)

    return covariances, total_rows



if __name__ == "__main__":
    column_names = ['Close/Open', 'Open(-1)', 'High(-1)', 'Low(-1)', 'Close(-1)', 'Volume(-1)',
                    'Open(-2)', 'High(-2)', 'Low(-2)', 'Close(-2)', 'Volume(-2)',
                    'Open(-3)', 'High(-3)', 'Low(-3)', 'Close(-3)', 'Volume(-3)']
    total_covariances = {col: 0 for col in column_names}
    total_rows = 0

    # Calculate and print the covariance for each CSV file
    for file in csv_files:
        print(f"File: {file} is complete.")
        covariances, tr = calculate_covariance(os.path.join(folder_path, file))
        total_rows += tr
        for col, covariance in covariances.items():
            total_covariances[col] += covariance

    # Calculate the overall average covariance for each column
    print(f"total_covariances: {total_covariances}, total_rows: {total_rows}")
    overall_average_covariance = {col: total_covariances[col] / total_rows for col in total_covariances}

    print("Overall Average Covariance:")
    print(overall_average_covariance)
