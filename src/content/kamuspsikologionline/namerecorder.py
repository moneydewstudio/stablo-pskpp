import os
import csv
import tkinter as tk
from tkinter import filedialog


def collect_file_names(folder_path):
    # List all files in the specified folder
    files = os.listdir(folder_path)

    # Extract file names without extensions
    file_names = [os.path.splitext(file)[0] for file in files]

    return file_names


def record_file_names():
    # Create a Tkinter root window (hidden)
    root = tk.Tk()
    root.withdraw()

    # Prompt user to select a folder
    folder_path = filedialog.askdirectory(title="Select Folder")

    if not folder_path:
        print("No folder selected. Exiting.")
        return

    # Collect file names
    file_names = collect_file_names(folder_path)

    # Create a CSV file and write the file names
    csv_file_path = os.path.join(folder_path, 'file_names.csv')
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['File Names'])
        csv_writer.writerows([[file_name] for file_name in file_names])

    print(f"File names recorded in: {csv_file_path}")


# Call the function to record file names
record_file_names()
