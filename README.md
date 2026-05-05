# task-manager-api

This project is part of my learning journey in backend development and API design.

A RESTful TODO API built with FastAPI and SQLite.
This project is an improved version of my earlier CLI-based TODO application, expanding it into a backend service with HTTP endpoints.

Features
Create tasks
Retrieve all tasks
Retrieve a task by ID
Update task details
Delete tasks
Persistent storage using SQLite
REST API design

Technologies Used
Python
FastAPI
SQLite (sqlite3)
Pydantic

How to Run
Install dependencies:
pip install fastapi uvicorn

Run the server:
uvicorn main:app --reload

Open in browser:
http://127.0.0.1:8000/docs

FastAPI provides an interactive Swagger UI where you can test all endpoints.

API Endpoints
Method	Endpoint	Description
GET	/tasks	Get all tasks
GET	/tasks/{id}	Get task by ID
POST	/tasks	Create a new task
PUT	/tasks/{id}	Update a task
DELETE	/tasks/{id}	Delete a task

Database
SQLite database: task.sqlite
Table structure:
Column	Type
id	INTEGER (Primary Key)
title	TEXT
description	TEXT
status	TEXT

Project Background
This project builds on a previous CLI-based TODO application and represents my transition from basic Python scripting to backend development using FastAPI and REST APIs.

Possible Improvements
Add input validation for status values
Prevent SQL injection (use parameterized queries)
Add authentication (JWT)
Connect to a frontend (React / web app)
Use an ORM like SQLAlchemy
