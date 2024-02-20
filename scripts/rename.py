import os

def rename_files():
    folder_path = os.getcwd()  # Get the current directory
    files = os.listdir(folder_path)  # List all files in the directory

    for filename in files:
        if filename.endswith("_full_1min_adjsplit.txt"):  # Check if the file ends with the specified suffix
            new_filename = filename.split("_")[0] + ".csv"  # Extract the desired part and add the .csv extension
            os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))  # Rename the file

if __name__ == "__main__":
    rename_files()
