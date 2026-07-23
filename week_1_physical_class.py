import os
import shutil
#define the folder to organize

folder_path = r"C:/Users/OWNER/OneDrive/Desktop/Python Folder/practice_folder"

all_files = os.listdir(folder_path)
total_number_of_files = (f"Found {len(all_files)} Files")
print(all_files)
print(total_number_of_files)
for files in all_files:
    print(f" - {files}")

CATEGORIES = {
    "PDFs":          [".pdf"],
    "Images":        [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Spreadsheets":  [".xlsx", ".xls", ".csv"],
    "Documents":     [".docx", ".doc", ".txt", ".rtf"],
    "Presentations": [".pptx", ".ppt"],
    "Code":          [".py", ".js", ".html", ".css", ".json"],
    "Archives":      [".zip", ".rar", ".tar", ".gz"],
    "Videos":        [".mp4", ".mov", ".avi", ".mkv"],
    "Audio":         [".mp3", ".wav", ".aac"]
}
def get_category(filename):
    _, extension = os.path.splitext(filename)
    extension = extension.lower()
    for category, extensions in CATEGORIES.items():
        if extension in extensions:
            return category
    return "Others"   
#organize the files into their respective folders
def organize_files(folder_path):
    for category in CATEGORIES.keys():
        category_folder = os.path.join(folder_path, category)
        os.makedirs(category_folder, exist_ok=True)
    moved_files_count = 0
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isdir(file_path):
            continue
        category = get_category(filename)
        destination = os.path.join(folder_path, category, filename)
        shutil.move(file_path, destination)
        moved_files_count += 1
        print(f"Moved {filename} to {category}/")
    return moved_files_count

result = organize_files(folder_path)
print(f"Organized {result} files into their respective folders.")

#error handling
def organize_folder_safe(folder_path):
    error =[]
    moved_files_count = 0
    try:
        for category in CATEGORIES.keys():
            category_folder = os.path.join(folder_path, category)
            os.makedirs(category_folder, exist_ok=True)
            for filename in os.listdir(folder_path):
                file_path = os.path.join(folder_path, filename)
                if os.path.isdir(file_path):
                    continue
                try:
                    category = get_category(filename)
                    destination = os.path.join(folder_path, category, filename)
                    #handle the case where the file already exists in the destination
                    if os.path.exists(destination):
                        base, extension = os.path.splitext(filename)
                        destination = os.path.join (folder_path, category, f"{base}_DUPLICATE{extension}")
                        shutil.move(file_path, destination)
                        moved_files_count += 1
                except Exception as e:
                    error.append(f"Error moving {filename}: {str(e)}")
    except Exception as e:
        return 0, [str(e)]
    return moved_files_count, error
from datetime import datetime

def generate_report(folder_path, moved_count, errors):
    report = f"""
FILE ORGANIZATION REPORT
Date:             {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Folder:           {folder_path}
Files Organized:  {moved_count}
"""
    for category in CATEGORIES.keys():
        cat_path = os.path.join(folder_path, category)
        if os.path.exists(cat_path):
            count = len(os.listdir(cat_path))
            report += f"   {category}: {count} files\n"

    if errors:
        report += f"\nErrors ({len(errors)}):\n"
        for error in errors:
            report += f"   - {error}\n"
    else:
        report += "\nNo errors encountered!\n"

    report_path = os.path.join(folder_path, "organization_report.txt")
    with open(report_path, "w") as f:
        f.write(report)

    print(report)
    return report_path