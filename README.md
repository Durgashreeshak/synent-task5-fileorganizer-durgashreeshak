# 📂 File Organizer

A Python-based File Organizer that automatically organizes files into category folders based on their file extensions.

This project was developed as **Task 5 – File Organizer** for the **Synent Technologies Python Development Internship Program**.

---

## 📌 Project Overview

The application allows the user to select any folder using a graphical folder picker. It automatically detects each file's type, creates the required category folders (if they do not already exist), and moves every file into its appropriate folder.

The project is built using Python's built-in **os**, **shutil**, and **tkinter** modules.

---

## ✨ Features

- Graphical folder selection using Tkinter
- Automatic file scanning
- File categorization based on extension
- Automatic creation of category folders
- Automatic file movement
- Supports multiple file categories
- Handles unsupported file types by placing them in an **Others** folder
- Displays processing status in the terminal
- Simple and easy-to-understand code structure

---

## 📂 Supported Categories

| Category | Extensions |
|----------|------------|
| Documents | .pdf, .doc, .docx, .txt, .ppt, .pptx, .xls, .xlsx |
| Images | .jpg, .jpeg, .png, .gif, .bmp, .webp |
| Videos | .mp4, .mkv, .avi, .mov, .wmv |
| Audio | .mp3, .wav, .aac, .flac |
| Archives | .zip, .rar, .7z, .tar, .gz |
| Programs | .exe, .msi, .bat |
| Code | .py, .java, .c, .cpp, .html, .css, .js, .json, .xml |
| Others | Unsupported file types |

---

## 🛠 Technologies Used

- Python 3
- os
- shutil
- tkinter

---

## 📁 Project Structure

```text
synent-task5-fileorganizer-durgashreeshak/
│
├── organizer.py
├── README.md
├── requirements.txt
├── sample_files/
├── screenshots/
└── .gitignore
```

---

## ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/Durgashreeshak/synent-task5-fileorganizer-durgashreeshak.git
```

Move into the project directory:

```bash
cd synent-task5-fileorganizer-durgashreeshak
```

---

## ▶️ How to Run

Run the application:

```bash
python organizer.py
```

1. A folder selection dialog will appear.
2. Select the folder you want to organize.
3. The application scans the files.
4. Category folders are created automatically.
5. Files are moved into their respective folders.
6. The terminal displays the processing summary.

> **Note:** For testing, it is recommended to use a copy of the sample files instead of modifying the original `sample_files` folder.

---

## 📷 Sample Output

```text
Moving Files:
------------------------------
✔ report.docx --> Documents
✔ photo.jpg --> Images
✔ movie.mp4 --> Videos
✔ song.mp3 --> Audio

Total Files Processed: 16
```

---

## 📸 Screenshots

Project screenshots are available in the **screenshots/** folder.

Example screenshots:

- Folder Selection
- Before Organizing Files
- After Organizing Files
- Terminal Output

---

## 🎥 Demo Video

Demo video link:

```
Add your YouTube or LinkedIn video link here after recording.
```

---

## 🚀 Future Improvements

- Duplicate file handling
- Recursive folder organization
- Custom user-defined categories
- Drag-and-drop support
- Progress bar for large folders
- User-defined file categories

---

## 👨‍💻 Author

**Durgashreesha K**

B.E. Artificial Intelligence & Machine Learning

Vivekananda College of Engineering and Technology, Puttur

GitHub:
https://github.com/Durgashreeshak

---

## 📄 License

This project was created for educational purposes as part of the **Synent Technologies Python Development Internship Program**.