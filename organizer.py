import os
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

    # Open folder selection dialog
    folder_path = filedialog.askdirectory(
        title="Select a Folder to Organize"
    )

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


def main():
    folder = select_folder()

    if folder:
        print(f"\nSelected Folder:\n{folder}")

        files = scan_files(folder)

        print("\nFiles Found:")
        print("-" * 30)

        for file in files:
            category = categorize_file(file)
            print(f"{file}  -->  {category}")

        print(f"\nTotal Files: {len(files)}")

    else:
        print("\nNo folder selected.")


if __name__ == "__main__":
    main()