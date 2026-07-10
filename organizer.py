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


def main():
    folder = select_folder()

    if folder:
        print(f"\nSelected Folder:\n{folder}")
    else:
        print("\nNo folder selected.")


if __name__ == "__main__":
    main()