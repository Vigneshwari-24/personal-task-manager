# Personal Task Manager

A simple web-based task management application built using Python, Streamlit, and SQLite.

## Features

* Add new tasks
* Add task descriptions
* Set due dates
* View all tasks
* Mark tasks as completed
* Delete tasks
* Search tasks
* Filter tasks by status
* View task statistics
* Store tasks using SQLite

## Technologies Used

* Python
* Streamlit
* SQLite
* Git
* GitHub

## Project Structure

```text
personal-task-manager/
│
├── app.py
├── database.py
├── requirements.txt
├── README.md
└── .gitignore
```

## How to Run the Project

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the project folder

```bash
cd personal-task-manager
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

For Windows:

```bash
venv\Scripts\activate
```

### 5. Install required packages

```bash
pip install -r requirements.txt
```

### 6. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

## Database

The project uses SQLite to store task information.

Each task contains:

* Task ID
* Task title
* Description
* Due date
* Status

## CRUD Operations

The application implements basic CRUD operations:

* **Create** — Add a new task
* **Read** — View saved tasks
* **Update** — Mark a task as completed
* **Delete** — Delete a task

## Future Improvements

* Task priority
* Task categories
* User login
* Notifications
* Task editing
* Cloud database
* Application deployment

## Author

Ganiga Vigneshwari
