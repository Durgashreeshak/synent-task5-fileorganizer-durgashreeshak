import os
from tkinter import Tk
from tkinter import filedialog


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


def main():
    folder = select_folder()

    if folder:
        print(f"\nSelected Folder:\n{folder}")

        files = scan_files(folder)

        print("\nFiles Found:")
        print("-" * 30)

        for file in files:
            print(file)

        print(f"\nTotal Files: {len(files)}")

    else:
        print("\nNo folder selected.")


if __name__ == "__main__":
    main()