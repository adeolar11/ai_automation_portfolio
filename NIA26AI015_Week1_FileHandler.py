import os

import shutil
import time

# check file in a folder
folder_path = r'C:\Users\OWNER\OneDrive\Desktop\Python Folder\practice_organizer'
os.listdir(folder_path)

result = os.listdir(folder_path)

for item in result:
    item_path = os.path.join(folder_path, item)
    if os.path.isfile(item_path):
        size = os.path.getsize(item_path) / (1024 * 1024)
        print(f"File: {item} with size {size: .2f} MB")
    elif os.path.isdir(item_path):
        print(f"\nFolder: {item}")

categories = {"PDF": ".pdf",
              "Document": ".docx",
              "Image": [".jpg",".png", ".jpeg", ".gif"],
              "spreadsheet": [".xlsx", ".csv", ".xls"],
              "code": [".py", ".js", ".html"],
              "video": [".mp4", ".mov", ".avi"],
              "audio": [".mp3", ".wav", ".aac"]}

def get_category(file_name):
    ext = os.path.splitext(file_name)[1].lower()
    for category, extension in categories.items():
        if ext in extension:
            return category
    return "Others"

for category in categories:
    os.makedirs(os.path.join(folder_path, category), exist_ok=True)

os.makedirs(os.path.join(folder_path, "Others"), exist_ok=True)

moved = 0
skipped = 0
duplicates = 0

# Current time
current_time = time.time()

# Scan files
for filename in result:

    filename_path = os.path.join(folder_path, filename)

    # Skip folders
    if os.path.isdir(filename_path):
        skipped += 1
        continue

    # Check if modified within last 7 days
    modified_time = os.path.getmtime(filename_path)

    if current_time - modified_time <= 7 * 24 * 60 * 60:
        destination_folder = os.path.join(folder_path, "Recently Modified")
    else:
        category = get_category(filename)
        destination_folder = os.path.join(folder_path, category)

    destination_path = os.path.join(destination_folder, filename)

    # Handle duplicate names
    if os.path.exists(destination_path):

        name, ext = os.path.splitext(filename)

        counter = 1

        while os.path.exists(destination_path):
            new_name = f"{name}_{counter}{ext}"
            destination_path = os.path.join(destination_folder, new_name)
            counter += 1

        duplicates += 1

    shutil.move(filename_path, destination_path)
    moved += 1

# Summary
print("\n========== SUMMARY ==========")
print(f"Files moved: {moved}")
print(f"Folders skipped: {skipped}")
print(f"Duplicate files renamed: {duplicates}")