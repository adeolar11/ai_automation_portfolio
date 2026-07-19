Filename = [("Project.pdf", 25 ), 
            ("Tecnology.docx", 15),
            ("holiday.jpg", 70),
            ("resume.pdf",10),
            ("NADF.docx", 20),
            ("resume1.txt", 5),
            ("statue.png", 30),
            ("list.xlsx", 15),
            ("budget.xlsx", 25),
            ("resume2.docx", 15),
            ("statement.txt", 5)]
file_category = {".pdf":"Documents",
                 ".docx":"Documents",
                 ".jpg":"Images",
                 ".png":"Images",
                 ".txt":"Documents",
                 ".xlsx":"Spreadsheet"
                 }
category_count = {}

for file,size in Filename:
    extension = "." + file.split(".")[-1]
    #get the category of the file based on its extension
    category = file_category.get(extension, "Others")
    print(f"{file} with size {size} MB is categorized as {category} Folder")
    #print a summary of total files in each category
    if category in category_count:
        category_count[category] += 1
    else:
        category_count[category] = 1

print("\nWe have the following number of files in each category: ")
for category, count in category_count.items():
    print(f"{count} {category} files")
    #print if size larger 20MB (Very Large)
for file, size in Filename:
    if size > 20:
        print(f"\nCompress before storing {file}, File too Large")