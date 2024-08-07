import os
import csv
import random
import tkinter as tk
from tkinter import filedialog


def bulk_rename_images(images_folder, names_folder):
    # List all files in the images folder
    image_files = [f for f in os.listdir(
        images_folder) if os.path.isfile(os.path.join(images_folder, f))]

    # Prompt user to select the CSV file containing names
    csv_file_path = filedialog.askopenfilename(
        title="Select CSV File",
        filetypes=[("CSV files", "*.csv")]
    )

    if not csv_file_path:
        print("No CSV file selected. Exiting.")
        return

    # Read names from the CSV file
    with open(csv_file_path, 'r', newline='', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        names_list = [row[0] for row in csv_reader]

    # Check if the number of images and names match
    num_images = len(image_files)
    num_names = len(names_list)

    if num_images == 0 or num_names == 0:
        print("No images or names found. Exiting.")
        return

    print(f"Number of images: {num_images}")
    print(f"Number of names: {num_names}")

    # Rename images using random names
    for i, image_file in enumerate(image_files):
        new_name = random.choice(names_list)
        # You can adjust the file extension if needed
        new_path = os.path.join(images_folder, f"{new_name}.jpg")
        old_path = os.path.join(images_folder, image_file)

        os.rename(old_path, new_path)
        print(f"Renamed: {old_path} -> {new_path}")

        # Remove the used name from the list
        names_list.remove(new_name)

        # If the number of names runs out, start over
        if not names_list:
            print("Out of names. Restarting from the beginning.")
            names_list = [row[0] for row in csv.reader(
                open(csv_file_path, 'r', newline='', encoding='utf-8'))]


if __name__ == "__main__":
    # Create a Tkinter root window (hidden)
    root = tk.Tk()
    root.withdraw()

    # Prompt user to select the images folder
    images_folder = filedialog.askdirectory(title="Select Images Folder")

    if not images_folder:
        print("No images folder selected. Exiting.")
        exit()

    # Prompt user to select the names folder
    names_folder = filedialog.askdirectory(title="Select Names Folder")

    if not names_folder:
        print("No names folder selected. Exiting.")
        exit()

    # Call the function to perform bulk renaming
    bulk_rename_images(images_folder, names_folder)
