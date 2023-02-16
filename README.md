# To-do-list

Python Version: 3.8.10

Steps to Run the Application:
$ python3 -m venv todo_app_env
$ source todo_app_env/bin/activate
$ pip install flask
$ pip install flask-restful
$ pip install flask_sqlalchemy


Clone the repository:
  $ git clone https://github.com/<username>/<repository>.git
  
Change into the project directory:
  $ cd <repository>
  
Run the application:
  $ python app.py
  

Open your web browser and go to http://localhost:5000/tasks to view the list of tasks.

API Endpoints:

GET /tasks - Get a list of all tasks
POST /tasks - Create a new task
GET /tasks/int:task_id - Get a task by ID
PUT /tasks/int:task_id - Update a task by ID
DELETE /tasks/int:task_id - Delete a task by ID
PUT /tasks/int:task_id/complete - Mark a task as completed
PUT /tasks/int:task_id/incomplete - Mark a task as incomplete
Data Model:

The application uses SQLite as the database. The data model has the following attributes:

id (integer) - Unique identifier for the task
task (string) - Description of the task
completed (boolean) - Whether the task is completed or not
External Libraries:

Flask - A micro web framework for Python
Flask-RESTful - An extension for Flask that adds support for building RESTful APIs
Flask-SQLAlchemy - An extension for Flask that provides easy integration with SQLAlchemy
Requirements:

The application has the following requirements:

Python 3.8.10 or higher
Flask 2.0.1 or higher
Flask-RESTful 0.3.9 or higher
Flask-SQLAlchemy 2.5.1 or higher






