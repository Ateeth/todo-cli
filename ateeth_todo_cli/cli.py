import typer
from ateeth_todo_cli.model.Task import Task
import json
import os

app = typer.Typer()

# todos = []  # In-memory todo list
file_path = "ateeth_todo_cli/data/tasks.json"
key = "tasks"

def file_exist_check():
    if not os.path.exists(file_path):
        print("Creating file")
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w') as file:
            json.dump({key: []}, file)
        
@app.command()
def add(task: str):
    """
    Add a new task to the todo list.
    """
    tasks = []
    file_exist_check()
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            tasks = data.get(key, [])
    except (json.JSONDecodeError, IOError) as e:
        print(f"Error reading or parsing {file_path}: {e}. Returning an empty list.")
    
    newTask = Task(task, len(tasks) + 1)
    newTask_dict = newTask.to_dict()
    tasks.append(newTask_dict)
    
    with open(file_path, 'w') as file:
        json.dump({key: tasks}, file, indent=4)
        # print(newTask_dict)
        print(f"Task added successfully (ID: {newTask_dict['id']})")


@app.command()
def list_tasks():
    """
    List all tasks in the todo list.
    """

if __name__ == "__main__":
    app()
