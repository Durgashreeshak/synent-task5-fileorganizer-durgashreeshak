# 📂 File Organizer

A Python-based File Organizer that automatically sorts files into categorized folders such as Documents, Images, Videos, Audio, Archives, Programs, Code, and Others.

This project was developed as **Task 5 – File Organizer** for the **Synent Technologies Python Development Internship**.

---

## 🚀 Features

- Select any folder using a graphical folder picker.
- Automatically detect file types.
- Create category folders if they do not already exist.
- Move files into the appropriate folders.
- Organize files into:
  - Documents
  - Images
  - Videos
  - Audio
  - Archives
  - Programs
  - Code
  - Others
- Display the number of processed files.

---

## 🛠 Technologies Used

- Python 3
- os module
- shutil module
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
├── sample_files_original/
├── screenshots/
└── .gitignore
```

---

## ▶️ How to Run

1. Clone the repository.

2. Open the project in Visual Studio Code.

3. Run:

```bash
python organizer.py
```

4. Select the folder you want to organize.

5. The files will automatically be sorted into category folders.

---

## 📸 Sample Output

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

## 💡 Future Improvements

- Duplicate file handling
- Recursive folder organization
- Custom user-defined categories
- Drag-and-drop interface

---

## 👨‍💻 Author

**Durgashreesha K**

Artificial Intelligence & Machine Learning Engineering Student

Vivekananda College of Engineering and Technology, Puttur