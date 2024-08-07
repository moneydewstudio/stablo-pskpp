import os
import csv
import re
import chardet
import tkinter as tk
from tkinter import filedialog


def get_folder_path(title):
    root = tk.Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory(title=title)
    return folder_path


def get_file_path(title, filetypes):
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title=title, filetypes=filetypes)
    return file_path


def detect_encoding(file_path):
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
    return result['encoding']


def read_csv(csv_file, encoding):
    data = []
    with open(csv_file, newline='', encoding=encoding) as csvfile:
        csvreader = csv.reader(csvfile)
        headers = next(csvreader)  # Assuming the first row contains headers
        for row in csvreader:
            data.append(dict(zip(headers, row)))
    return data


def remove_front_matter(content):
    # Remove existing front matter
    front_matter_pattern = r'^---(.*?)---'
    return re.sub(front_matter_pattern, '', content, count=1, flags=re.DOTALL)


def bulk_edit_front_matter(markdown_folder, csv_file):
    markdown_files = [f for f in os.listdir(
        markdown_folder) if f.endswith('.md')]
    encoding = detect_encoding(csv_file)
    csv_data = read_csv(csv_file, encoding)

    for file_name in markdown_files:
        file_path = os.path.join(markdown_folder, file_name)

        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # Remove existing front matter
        content_without_front_matter = remove_front_matter(content)

        # Find the corresponding row in CSV data based on the filename
        csv_row = next((row for row in csv_data if row.get(
            'filename') == file_name), None)

        if csv_row:
            # Create new front matter
            new_front_matter = '---\n'
            for field, value in csv_row.items():
                if field != 'filename':  # Exclude filename from the front matter
                    new_front_matter += f'{field}: {value}\n'
            new_front_matter += '---\n'

            # Append new front matter to the content
            updated_content = new_front_matter + content_without_front_matter

            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(updated_content)
                print(f"Front matter updated in {file_name}")
        else:
            print(f"No CSV data found for {file_name}")


if __name__ == "__main__":
    markdown_folder = get_folder_path(
        "Select the folder containing Markdown files")
    csv_file = get_file_path("Select the CSV file", [("CSV files", "*.csv")])

    if markdown_folder and csv_file:
        bulk_edit_front_matter(markdown_folder, csv_file)
