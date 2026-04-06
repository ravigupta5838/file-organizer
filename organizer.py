import os
import shutil

# Folder path (Downloads folder)
path = "C:/Users/DELL/Downloads"

files = os.listdir(path)

for file in files:
    filename, extension = os.path.splitext(file)

    extension = extension.lower()

    if extension in ['.jpg', '.png', '.jpeg']:
        folder = "Images"
    elif extension in ['.mp4', '.mkv']:
        folder = "Videos"
    elif extension in ['.pdf']:
        folder = "PDF"
    else:
        folder = "Others"

    folder_path = os.path.join(path, folder)

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    shutil.move(os.path.join(path, file), os.path.join(folder_path, file))

print("Files Organized Successfully!")