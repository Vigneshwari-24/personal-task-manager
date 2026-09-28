import streamlit as st
from database import (
    create_database,
    add_task,
    get_tasks,
    complete_task,
    delete_task
)


# Create database
create_database()


# Page title
st.title("Personal Task Manager")

st.write("Manage your daily tasks easily using Python, Streamlit and SQLite.")


# -----------------------------
# ADD NEW TASK
# -----------------------------

st.header("Add New Task")

title = st.text_input("Task Title")

description = st.text_area("Description")

due_date = st.date_input("Due Date")


if st.button("Add Task"):

    if title:

        add_task(
            title,
            description,
            str(due_date)
        )

        st.success("Task added successfully!")

        st.rerun()

    else:

        st.warning("Please enter a task title.")


# -----------------------------
# SEARCH AND FILTER
# -----------------------------

st.header("My Tasks")

search = st.text_input("Search Tasks")

status_filter = st.selectbox(
    "Filter by Status",
    ["All", "Pending", "Completed"]
)


# Get all tasks
tasks = get_tasks()


# Search tasks
if search:

    tasks = [
        task
        for task in tasks
        if search.lower() in task[1].lower()
    ]


# Filter by status
if status_filter != "All":

    tasks = [
        task
        for task in tasks
        if task[4] == status_filter
    ]


# -----------------------------
# TASK STATISTICS
# -----------------------------

total_tasks = len(tasks)

completed_tasks = len([
    task
    for task in tasks
    if task[4] == "Completed"
])

pending_tasks = total_tasks - completed_tasks


col1, col2, col3 = st.columns(3)

col1.metric("Total Tasks", total_tasks)

col2.metric("Completed", completed_tasks)

col3.metric("Pending", pending_tasks)


# -----------------------------
# DISPLAY TASKS
# -----------------------------

st.subheader("Task List")


if len(tasks) == 0:

    st.info("No tasks found.")


else:

    for task in tasks:

        task_id, title, description, due_date, status = task

        st.write("###", title)

        st.write("Description:", description)

        st.write("Due Date:", due_date)

        st.write("Status:", status)


        # Mark as completed
        if status == "Pending":

            if st.button(
                "Mark as Completed",
                key=f"complete_{task_id}"
            ):

                complete_task(task_id)

                st.success("Task completed!")

                st.rerun()


        # Delete task
        if st.button(
            "Delete",
            key=f"delete_{task_id}"
        ):

            delete_task(task_id)

            st.success("Task deleted!")

            st.rerun()


        st.divider()