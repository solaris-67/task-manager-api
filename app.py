import sqlite3
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from todo_models import Task
from pydantic import BaseModel


database_name = 'task.sqlite'
table_name = 'Task'

conn = sqlite3.connect(database_name)
cursor = conn.cursor()

cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name}(id INTEGER PRIMARY KEY, title TEXT, description TEXT, status TEXT)")
conn.commit()
conn.close()

class Task:
    def __init__(self, title, description, status, id = None):
        self.id = id
        self.title = title
        self.description = description
        self.status = status

    def create(self):
        conn = sqlite3.connect(database_name)
        cursor = conn.cursor()

        cursor.execute(f'INSERT INTO {table_name} VALUES(NULL, "{self.title}", "{self.description}", "{self.status}")')
        conn.commit()
        conn.close()

    def update(self):
        conn = sqlite3.connect(database_name)
        cursor = conn.cursor()

        cursor.execute(f"UPDATE {table_name} SET title = '{self.title}', description = '{self.description}', status = '{self.status}' WHERE id = {self.id}")
        conn.commit()
        conn.close()

    @classmethod
    def get_task(cls, id):
        conn = sqlite3.connect(database_name)
        cursor = conn.cursor()

        cursor.execute(f"SELECT * FROM {table_name} WHERE id = {id}")
        found_task = cursor.fetchone()

        if found_task is not None:
            return Task(found_task[1], found_task[2], found_task[3], found_task[0])

    @classmethod
    def get_all(cls):
        conn = sqlite3.connect(database_name)
        cursor = conn.cursor()

        cursor.execute(f"SELECT * FROM {table_name}")

        found_tasks = cursor.fetchall()
        tasks = []

        for task in found_tasks:
            tasks.append(Task(task[1], task[2], task[3], task[0]))

        return tasks

    @classmethod
    def delete(cls, id):
        conn = sqlite3.connect(database_name)
        cursor = conn.cursor()

        cursor.execute(f"DELETE FROM {table_name} WHERE id = {id}")
        conn.commit()
        conn.close()


app = FastAPI()

app.add_middleware(
    CORSMiddleware,  # type: ignore
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

class TaskAPI(BaseModel):
    title: str
    description: str
    status: str

@app.get("/tasks")
async def get_all_tasks():
    return Task.get_all()

@app.get("/tasks/{id}")
async def get_task(id):
    return Task.get_task(id)

@app.delete("/tasks/{id}")
async def delete_task(id):
    Task.delete(id)
    return {"message": "Task deleted"}

@app.post("/tasks")
async def create_task(task: TaskAPI):
    task = Task(task.title, task.description, task.status)

    task.create()
    return {"message": "Task created"}

@app.put("/tasks/{id}")
async def update_task(id, task: TaskAPI):
    found_task = Task.get_task(id)
    if found_task is None:
        task = Task(task.title, task.description, task.status)

        task.create()
        return {"message": "Task created"}
    else:
        found_task.title = task.title
        found_task.description = task.description
        found_task.status = task.status

        found_task.update()

        return {"message": "Task updated"}



