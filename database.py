import sqlite3


def create_database():
    connection = sqlite3.connect("tasks.db")

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            due_date TEXT,
            status TEXT DEFAULT 'Pending'
        )
    """)

    connection.commit()
    connection.close()
def add_task(title, description, due_date):
    connection = sqlite3.connect("tasks.db")

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO tasks (title, description, due_date)
        VALUES (?, ?, ?)
    """, (title, description, due_date))

    connection.commit()
    connection.close()
def get_tasks():
    connection = sqlite3.connect("tasks.db")

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM tasks")

    tasks = cursor.fetchall()

    connection.close()

    return tasks
def complete_task(task_id):
    connection = sqlite3.connect("tasks.db")

    cursor = connection.cursor()

    cursor.execute("""
        UPDATE tasks
        SET status = 'Completed'
        WHERE id = ?
    """, (task_id,))

    connection.commit()
    connection.close()
def delete_task(task_id):
    connection = sqlite3.connect("tasks.db")

    cursor = connection.cursor()

    cursor.execute("""
        DELETE FROM tasks
        WHERE id = ?
    """, (task_id,))

    connection.commit()
    connection.close()