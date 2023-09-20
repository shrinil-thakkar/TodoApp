# Building a TODO app.
# Here you can create, update, delete and get your tasks.
# There is a functionality to mark them as completed when done.

# This file consists of the API endpoints that are built leveraging
# python's FastAPI framework.

from fastapi import FastAPI
from pydantic import BaseModel
from todoService import TODO_SERVICE

app = FastAPI()
todo_service = TODO_SERVICE()

class Task(BaseModel):
    task_name: str

# API endpoint to create a task
# Here you need to pass a Task type object which just contains the task name
@app.post("/todo")
def create_task(task: Task):
    return todo_service.create_task(task.task_name)

# API endpoint to get a task by task id
# It returns you an dictionary containing the task info
@app.get("/todo/{task_id}")
def get_task(task_id: int):
    return todo_service.get_task(task_id)

# API endpoint to get a update the Task by task id
# It returns you an updated dictionary containing the task info
@app.put("/todo/{task_id}")
def update_task(task_id: int, task: Task):
    try:
        return todo_service.update_task(task_id, task.task_name)
    except Exception as e:
        print(f"Failed to update the task + {str(e)}")

# API endpoint to delete a task by task id
# It does not return anything, but logs for success as well as failure
@app.delete("/todo/{task_id}")
def delete_task(task_id: int):
    todo_service.delete_task(task_id)

# API endpoint to mark the task as completed by passing task id
# It returns you the updated dictionary containing the task info
@app.put("/todo/mark_completed/{task_id}")
def mark_completed(task_id: int):
    return todo_service.mark_completed(task_id)
