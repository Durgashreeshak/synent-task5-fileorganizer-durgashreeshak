import os
import shutil
from tkinter import Tk
from tkinter import filedialog

FILE_CATEGORIES = {
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv"],
    "Audio": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Programs": [".exe", ".msi", ".bat"],
    "Code": [".py", ".java", ".c", ".cpp", ".html", ".css", ".js", ".json", ".xml"]
}

def select_folder():
    """
    Opens a folder selection dialog and returns the selected folder path.
    """

    # Hide the default Tkinter window
    root = Tk()
    root.withdraw()

    # Keep the folder dialog in front of other windows
    root.attributes("-topmost", True)

    # Open folder selection dialog
    folder_path = filedialog.askdirectory(
        title="Select a Folder to Organize"
    )

    # Close the hidden Tkinter window
    root.destroy()

    return folder_path

def scan_files(folder_path):
    """
    Returns a list of files present in the selected folder.
    Subfolders are ignored.
    """

    files = []

    for item in os.listdir(folder_path):
        full_path = os.path.join(folder_path, item)

        if os.path.isfile(full_path):
            files.append(item)

    return files

def categorize_file(filename):
    """
    Returns the category of a file based on its extension.
    """

    extension = os.path.splitext(filename)[1].lower()

    for category, extensions in FILE_CATEGORIES.items():
        if extension in extensions:
            return category

    return "Others"

def create_category_folders(folder_path):
    """
    Creates all required category folders.
    If a folder already exists, it won't raise an error.
    """

    categories = list(FILE_CATEGORIES.keys())
    categories.append("Others")

    for category in categories:
        folder = os.path.join(folder_path, category)
        os.makedirs(folder, exist_ok=True)

def move_files(folder_path, files):
    """
    Moves files into their respective category folders.
    """

    print("\nMoving Files:")
    print("-" * 30)

    for file in files:

        category = categorize_file(file)

        source_path = os.path.join(folder_path, file)

        destination_path = os.path.join(folder_path, category, file)

        shutil.move(source_path, destination_path)

        print(f"✔ {file}  -->  {category}")

def main():
    folder = select_folder()

    if folder:
        print(f"\nSelected Folder:\n{folder}")

        files = scan_files(folder)

        create_category_folders(folder)

        move_files(folder, files)

        print(f"\nTotal Files Processed: {len(files)}")

    else:
        print("\nNo folder selected.")


if __name__ == "__main__":
    main()