import os
#define the folder to organize

folder_path = "C:/Users/OWNER/OneDrive/Desktop/Python Folder/practice_folder"

all_files = os.listdir(folder_path)
total_number_of_files = (f"Found {len(all_files)} Files")
print(all_files)
print(total_number_of_files)
for files in all_files:
    print(f" - {files}")