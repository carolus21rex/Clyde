import csv
import os
import shutil

# Directory where CSV files are located (assuming they're in the same directory as the script)
directory = os.path.dirname(os.path.abspath(__file__))

# Loop through each file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv"):
        with open(os.path.join(directory, filename), 'r', newline='') as csvfile:
            # Read the CSV file
            reader = csv.reader(csvfile)
            # Read the header
            header = next(reader)
            # Skip the first non-header row
            next(reader, None)
            # Create a temporary file to write the modified CSV data
            temp_file = os.path.join(directory, 'temp.csv')
            with open(temp_file, 'w', newline='') as temp_csvfile:
                writer = csv.writer(temp_csvfile)
                # Write the header
                writer.writerow(header)
                # Write the rest of the rows
                for row in reader:
                    writer.writerow(row)
        # Replace the original file with the temporary file
        shutil.move(temp_file, os.path.join(directory, filename))
