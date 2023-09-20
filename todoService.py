# This file contains combination of model layer, service layer and DAO layer.


# This class contains the attributes for a TODO task

class TODO:

    def __init__(self, task_id, task_name):
        self.task_id = task_id
        self.task_name = task_name
        self.is_completed = False


# This class maintains the created tasks in memory
# It also handles the logic for all the supported API endpoints.

class TODO_SERVICE:

    def __init__(self):
        self.task_map = {}
        self.id = 0

    def create_task(self, task_name):
        try:
            self.id += 1
            todo_task = TODO(self.id, task_name)
            self.task_map[self.id] = todo_task
            print(f"Task created successfully with Id: {self.id}: {todo_task}")
            return {
                "task_id": todo_task.task_id,
                "task_name": todo_task.task_name,
                "is_completed": todo_task.is_completed
            }
        except Exception as e:
            print(f"Failed to create task + {str(e)}")

    def get_task(self, task_id):
        try:
            if task_id in self.task_map:
                todo_task = self.task_map.get(task_id)
                return {
                    "task_id": todo_task.task_id,
                    "task_name": todo_task.task_name,
                    "is_completed": todo_task.is_completed
                }
            print(f"Task with id: {task_id} does not exist")
            return None
        except Exception as e:
            print(f"Failed to get the task + {str(e)}")

    def update_task(self, task_id, task_name):
        try:
            if task_id in self.task_map:
                todo_task = self.task_map[task_id]
                todo_task.task_name = task_name
                self.task_map[task_name] = todo_task
                print(f"Task updated successfully: {todo_task}")
                return {
                    "task_id": todo_task.task_id,
                    "task_name": todo_task.task_name,
                    "is_completed": todo_task.is_completed
                }
            print(f"Task with id: {task_id} does not exist")
            return None
        except Exception as e:
            print(f"Failed to update the task + {str(e)}")

    def delete_task(self, task_id):
        try:
            self.task_map.pop(task_id)
            print(f"Task with Id: {task_id} deleted successfully")
        except Exception as e:
            print(f"Failed to delete the task + {str(e)}")

    def mark_completed(self, task_id):
        try:
            todo_task = self.task_map.get(task_id)
            if todo_task:
                todo_task.is_completed = True
                self.task_map[task_id] = todo_task
                print(f"Task updated successfully: {todo_task}")
                return {
                    "task_id": todo_task.task_id,
                    "task_name": todo_task.task_name,
                    "is_completed": todo_task.is_completed
                }
            print(f"Task with id: {task_id} does not exist")
            return None
        except Exception as e:
            print(f"Failed to mark task completed + {str(e)}")