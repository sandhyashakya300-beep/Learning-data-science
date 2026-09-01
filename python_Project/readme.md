# 📺 YouTube Video Manager CLI

A simple **Python command-line application** for managing a personal collection of YouTube videos.

The application allows users to **view, add, update, and delete video records** through an interactive terminal menu. Video information is stored using **JSON**, allowing the data to persist between program executions.

---

## 📌 Project Overview

The **YouTube Video Manager CLI** is a beginner-friendly Python project designed to practice:

* Functions
* Lists
* Dictionaries
* User input
* File handling
* JSON data persistence
* CRUD operations
* Loops
* Conditional logic
* Python `match/case`
* Modular program structure

Each video is stored as a dictionary containing:

```python
{
    "name": "Python Tutorial",
    "time": "30 minutes"
}
```

---

## ✨ Features

The application provides five menu options:

| Option | Feature          | Description                        |
| ------ | ---------------- | ---------------------------------- |
| 1      | 📋 List Videos   | Display all saved videos           |
| 2      | ➕ Add Video      | Add a new YouTube video            |
| 3      | ✏️ Update Video  | Update an existing video's details |
| 4      | 🗑️ Delete Video | Remove a video from the list       |
| 5      | 🚪 Exit          | Close the application              |

These options are implemented in the `main()` function using Python's `match/case` statement.

---

# 🛠️ Technologies Used

* 🐍 Python
* 📄 JSON
* 💻 Command Line / Terminal
* 📁 File Handling

The project only imports Python's built-in `json` module, so there are no external Python packages required by the code.

---

# 📂 Project Structure

A recommended repository structure is:

```text
YouTube-Video-Manager/
│
├── youtube.py
├── youtube.txt
└── README.md
```

The Python script is responsible for the application logic, while `youtube.txt` is used as the JSON data file.

---

# 🧠 How the Application Works

The application follows this basic workflow:

```text
             Start Application
                    │
                    ▼
             Load Video Data
                    │
                    ▼
              Display Menu
                    │
       ┌────────────┼────────────┐
       ▼            ▼            ▼
     List          Add         Update
       │            │            │
       └────────────┼────────────┘
                    │
                    ▼
                  Delete
                    │
                    ▼
              Save JSON Data
                    │
                    ▼
                 Continue
                    │
                    ▼
                  Exit
```

---

# 1️⃣ Loading Video Data

The `load_data()` function loads existing video information from a JSON file:

```python
def load_data():
    try:
        with open('python_Project/youtube.txt', 'r') as file:
            test = json.load(file)
            return test
    except FileNotFoundError:
        return []
```

The function:

1. Opens the data file.
2. Reads the JSON content.
3. Converts the JSON data into Python objects using `json.load()`.
4. Returns the video list.
5. Returns an empty list if the file does not exist.

This allows the application to start even when there is no existing data file.

---

# 2️⃣ Saving Video Data

The `save_data()` function stores the current video list as JSON:

```python
def save_data(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)
```

The Python list is converted into JSON using:

```python
json.dump()
```

and written to the file.

---

# 3️⃣ Listing All Videos

The `List_all_videos()` function displays all stored videos:

```python
def List_all_videos(videos):
    print("\n")
    print('*' * 79)

    for index, video in enumerate(videos, start=1):
        print(f"{index}.{video['name']},Duration:{video['time']}")

    print("\n")
    print('*' * 79)
```

The use of:

```python
enumerate(videos, start=1)
```

provides user-friendly numbering beginning from `1`.

For each video, the application displays:

```text
1. Python Tutorial, Duration:30 minutes
2. Machine Learning, Duration:45 minutes
```

The listing functionality is implemented in the uploaded script.

---

# 4️⃣ Adding a Video

The `add_video()` function collects information from the user:

```python
def add_video(videos):
    name = input("Enter the video name :")
    time = input("Enter the video time :")

    videos.append({
        'name': name,
        'time': time
    })

    save_data(videos)
```

The user enters:

* Video name
* Video duration

The information is stored as a dictionary:

```python
{
    'name': name,
    'time': time
}
```

The dictionary is then added to the `videos` list.

Finally, `save_data()` persists the updated list to the JSON file.

---

# 5️⃣ Updating a Video

The `update_video()` function first displays the available videos:

```python
List_all_videos(videos)
```

The user then selects a video number:

```python
index = int(input("Enter the video number to update"))
```

The program checks whether the selected index is valid:

```python
if 1 <= index <= len(videos):
```

If valid, the user enters the new name and duration:

```python
name = input("Enter the new video name :")
time = input("Enter the new video time :")
```

The selected video is then replaced:

```python
videos[index - 1] = {
    'name': name,
    'time': time
}
```

Finally, the updated list is saved.

---

# 6️⃣ Deleting a Video

The `delete_video()` function allows users to remove a video.

First, the application displays all videos:

```python
List_all_videos(videos)
```

Then it asks for the video number:

```python
index = int(input("Enter the video number to be deleted"))
```

If the index is valid:

```python
del videos[index - 1]
```

The video is removed from the list and the updated data is saved.

---

# 7️⃣ Main Menu

The `main()` function controls the application.

It first loads the existing videos:

```python
videos = load_data()
```

Then it continuously displays the menu:

```text
Youtube Manager | choose an option

1. List all youtube videos
2. Add a youtube videos
3. Update a youtube videos details
4. Delete a youtube videos
5. Exit the app
```

The application uses a `while True` loop to keep running until the user selects option `5`.

---

# 🔀 Menu Selection Using `match/case`

The user's choice is handled using:

```python
match choice:
    case "1":
        List_all_videos(videos)

    case "2":
        add_video(videos)

    case "3":
        update_video(videos)

    case "4":
        delete_video(videos)

    case "5":
        break

    case _:
        print("Invalid Choice")
```

This provides a clean way to map menu choices to application functions.

---

# 💾 Data Persistence

The project uses JSON for storing data.

A video is represented as:

```json
{
    "name": "Python Tutorial",
    "time": "30 minutes"
}
```

Multiple videos can be stored as a JSON array:

```json
[
    {
        "name": "Python Tutorial",
        "time": "30 minutes"
    },
    {
        "name": "Machine Learning",
        "time": "45 minutes"
    }
]
```

This makes the project a simple example of **persistent CRUD data management**.

---

# 🔄 CRUD Operations

The project demonstrates the four fundamental CRUD operations:

```text
C → Create → Add a video
R → Read   → List videos
U → Update → Update video details
D → Delete → Delete a video
```

| CRUD   | Project Function    |
| ------ | ------------------- |
| Create | `add_video()`       |
| Read   | `List_all_videos()` |
| Update | `update_video()`    |
| Delete | `delete_video()`    |

These operations are implemented through separate functions, making the code easier to understand and maintain.

---

# ⚠️ Important Code Observation

There is currently an inconsistency in the data-file paths.

### `load_data()` reads from:

```python
python_Project/youtube.txt
```

### `save_data()` writes to:

```python
youtube.txt
```

These are different paths.

Because of this, the application may save data to one location but attempt to load it from another.

### Recommended Improvement

Use the same path in both functions.

For example:

```python
DATA_FILE = "youtube.txt"
```

Then:

```python
def load_data():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
```

and:

```python
def save_data(videos):
    with open(DATA_FILE, "w") as file:
        json.dump(videos, file, indent=4)
```

This is a recommended improvement rather than part of the current implementation.

---

# ▶️ How to Run

## 1. Clone the Repository

```bash
git clone <your-repository-url>
```

## 2. Navigate to the Project

```bash
cd YouTube-Video-Manager
```

## 3. Run the Application

```bash
python youtube.py
```

The application will display the interactive menu in the terminal.

---

# 💻 Example Usage

When the application starts:

```text
Youtube Manager | choose an option

1. List all youtube videos
2. Add a youtube videos
3. Update a youtube videos details
4. Delete a youtube videos
5. Exit the app

Enter your choice:
```

### Add a Video

```text
Enter your choice: 2

Enter the video name: Python Tutorial
Enter the video time: 30 minutes
```

### List Videos

```text
Enter your choice: 1

*******************************************************************************
1.Python Tutorial,Duration:30 minutes
*******************************************************************************
```

The exact display depends on the data entered by the user.

---

# 🎯 Learning Objectives

This project helps practice:

* Python functions
* Lists
* Dictionaries
* Loops
* Conditional statements
* User input
* File handling
* JSON serialization
* JSON deserialization
* CRUD operations
* Exception handling
* `match/case`
* Modular programming

---

# 🚀 Possible Improvements

This project can be extended into a more complete YouTube/video management application.

### 1. Add YouTube URLs

Instead of storing only:

```text
name
time
```

store:

```text
name
time
url
```

Example:

```python
{
    "name": "Python Tutorial",
    "time": "30 minutes",
    "url": "https://youtube.com/..."
}
```

---

### 2. Improve JSON Formatting

Use:

```python
json.dump(videos, file, indent=4)
```

to make the stored JSON easier to read.

---

### 3. Add Input Validation

Currently, invalid numeric input could cause a `ValueError`.

For example:

```text
Enter the video number to update: abc
```

could cause an error.

A `try/except` block could handle this more safely.

---

### 4. Improve Function Naming

The current function is named:

```python
List_all_videos()
```

Python naming conventions generally favor:

```python
list_all_videos()
```

Using lowercase `snake_case` consistently would make the project more Pythonic.

---

### 5. Add Search Functionality

Add an option such as:

```text
6. Search for a video
```

Users could search by video name.

---

### 6. Add Categories

Videos could be organized by:

```text
Python
Machine Learning
Data Science
AI
Web Development
```

---

### 7. Add Confirmation Before Delete

Before deleting:

```text
Are you sure you want to delete this video? (y/n)
```

This helps prevent accidental deletion.

---

# 📊 Project Architecture

The project follows a simple functional architecture:

```text
youtube.py
    │
    ├── load_data()
    │       └── Read JSON data
    │
    ├── save_data()
    │       └── Write JSON data
    │
    ├── List_all_videos()
    │       └── Display videos
    │
    ├── add_video()
    │       └── Create video
    │
    ├── update_video()
    │       └── Modify video
    │
    ├── delete_video()
    │       └── Remove video
    │
    └── main()
            └── Control application
```

This separation of responsibilities makes the project suitable for learning fundamental programming concepts.

---

# 🔐 Data Storage

The project does **not** use a database.

Instead, video information is stored locally in a JSON-formatted text file.

```text
Python Application
       │
       ▼
   Python List
       │
       ▼
    json.dump()
       │
       ▼
  youtube.txt
```

When the application starts:

```text
youtube.txt
       │
       ▼
    json.load()
       │
       ▼
   Python List
```

The persistence logic is implemented using Python's built-in `json` module.

---

# 📦 Dependencies

No third-party packages are required.

The project uses:

```python
import json
```

which is included in Python's standard library.

---

# 🧪 Project Type

**Python CLI Application | CRUD Application | JSON Data Persistence | Beginner Project**

---

# 🎓 What I Learned

Through this project, I practiced:

* Building a command-line application
* Structuring a Python program using functions
* Working with lists and dictionaries
* Reading and writing files
* Working with JSON
* Implementing CRUD functionality
* Handling missing files with `try/except`
* Using Python `match/case`
* Creating a simple persistent data-management system

---

# 🔮 Future Scope

The project can eventually be upgraded into:

```text
CLI Application
      ↓
Improved CLI + Validation
      ↓
SQLite Database
      ↓
REST API
      ↓
Web Application
      ↓
YouTube Video Management Dashboard
```

Potential future technologies could include:

* SQLite
* Flask or FastAPI
* Streamlit
* HTML/CSS/JavaScript
* REST APIs

---

# ⭐ Conclusion

The **YouTube Video Manager CLI** is a simple but practical Python project that demonstrates how to build an interactive command-line application with persistent data storage.

It combines fundamental Python concepts such as **functions, lists, dictionaries, loops, file handling, JSON, exception handling, and CRUD operations** into one practical project.

The project is a good foundation for learning how small Python applications are structured before moving toward databases, APIs, and full-stack applications.

---

## 👩‍💻 Author

**Sandhya Shakya**

Built with ❤️ using **Python 🐍**

---

## ⭐ If You Like This Project

If this project helped you understand Python CLI applications, JSON persistence, or CRUD operations, consider giving the repository a ⭐ on GitHub.

**Happy Coding! 🚀🐍**
