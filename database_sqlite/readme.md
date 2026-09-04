YouTube Manager App with SQLite

A simple command-line YouTube Manager App built with Python and
SQLite. It allows users to store and manage YouTube video details
through a menu-driven interface.

Project Overview

This project demonstrates a basic CRUD (Create, Read, Update,
Delete) application using Python's built-in sqlite3 module.

The application creates and uses a SQLite database containing a videos
table with:

Column   Type      Description

id     INTEGER   Unique video ID and primary key
name   TEXT      YouTube video name
time   TEXT      Video duration/time

The database is connected using sqlite3.connect() and the table is
created automatically if it does not already exist.

Features

📋 List all stored YouTube videos

➕ Add a new YouTube video

✏️ Update an existing video's details

🗑️ Delete a video by ID

💾 Store data persistently in SQLite

🖥️ Interactive command-line menu

🔐 Uses parameterized SQL queries for database operations

Technologies Used

Python 3

SQLite

sqlite3 --- Python's built-in SQLite database interface

Project Structure

youtube-manager-app/
│
├── youtube_manager_app.py
├── database_sqlite/
│   └── youtube_videos.db
└── README.md

The application uses the database path
database_sqlite/youtube_videos.db.

How the Application Works

When the program starts, it connects to the SQLite database and ensures
that the videos table exists.

The application then displays a menu with five options:

Youtube Manager App with DB
1. List all youtube videos
2. Add a youtube videos
3. Update a youtube videos details
4. Delete a youtube videos
5. Exit the app

fileciteturn14file0L44-L54

CRUD Operations

1. List Videos

Retrieves all records from the videos table and prints them to the
terminal.

2. Add a Video

The user enters the video name and time. The record is inserted and
committed to the database.

INSERT INTO videos(name, time) VALUES(?, ?);

3. Update a Video

The user provides the video ID, new name, and new time. The selected
record is updated.

UPDATE videos
SET name = ?, time = ?
WHERE id = ?;

4. Delete a Video

The user provides a video ID and the corresponding record is deleted.

DELETE FROM videos
WHERE id = ?;

Installation

1. Clone the Repository

git clone <your-github-repository-url>
cd youtube-manager-app

2. Check Python Installation

python --version

No external Python packages are required because sqlite3 is included
with Python.

Running the Application

Run:

python youtube_manager_app.py

The interactive menu will appear in the terminal. The program continues
running until the user selects option 5, after which the database
connection is closed.

Example Usage

Add a Video

Enter your choice : 2
Enter the video name : Python SQLite Tutorial
Enter the video time : 15:30

List Videos

Enter your choice : 1

(1, 'Python SQLite Tutorial', '15:30')

Update a Video

Enter your choice : 3
Enter the video id to update : 1
Enter the video name : Python SQLite CRUD Tutorial
Enter the video time : 18:20

Delete a Video

Enter your choice : 4
Enter the video id to deleted : 1

Code Structure

The application is organized around four CRUD functions:

list_videos() --- retrieves and displays all videos.

add_video(name, time) --- inserts a new video.

update_video(video_id, new_name, new_time) --- updates an existing
video.

delete_video(video_id) --- deletes a video.

The main() function controls the menu-driven application flow.

Database Design

videos
├── id       INTEGER PRIMARY KEY
├── name     TEXT NOT NULL
└── time     TEXT NOT NULL

The schema is created with CREATE TABLE IF NOT EXISTS, so an existing
table is preserved.

Learning Objectives

This project provides practice with:

Python functions

Loops and conditional statements

User input handling

SQLite database connections

SQL CRUD operations

Database transactions using commit()

Parameterized SQL queries

Menu-driven command-line applications

Current Limitations

The current implementation does not include:

Input validation

Exception handling

Search/filter functionality

Delete confirmation

Video URLs or channel information

Automated tests

Logging

GUI or web interface

Future Improvements

Possible enhancements include:

Add input validation and exception handling.

Add search functionality.

Improve terminal output formatting.

Add delete confirmation.

Store video URLs and channel names.

Add categories or tags.

Build a GUI with Tkinter.

Create a web version with Flask or FastAPI.

Add automated tests with pytest.

Author

Sandhya Shakya

Conclusion

The YouTube Manager App is a beginner-friendly Python project that
combines a command-line interface with SQLite persistence. It
demonstrates the complete CRUD lifecycle for managing YouTube video
records and provides a practical foundation for learning Python database
programming.