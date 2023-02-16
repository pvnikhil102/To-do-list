from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
db = SQLAlchemy(app)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    completed = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"Task(id={self.id}, name='{self.name}', completed={self.completed})"

python
>>> from app import db
>>> db.create_all()

from flask_restful import Resource, reqparse

parser = reqparse.RequestParser()
parser.add_argument('name', type=str, help='Name of the task')
parser.add_argument('completed', type=bool, help='Completion status of the task')

class TaskList(Resource):
    def get(self):
        tasks = Task.query.all()
        return [task.__dict__ for task in tasks]

    def post(self):
        args = parser.parse_args()
        task = Task(name=args['name'], completed=args['completed'])
        db.session.add(task)
        db.session.commit()
        return task.__dict__

class TaskDetail(Resource):
    def get(self, task_id):
        task = Task.query.get(task_id)
        return task.__dict__

    def put(self, task_id):
        args = parser.parse_args()
        task = Task.query.get(task_id)
        if args['name']:
                            task.name = args['name']
            if args['completed'] is not None:
                task.completed = args['completed']
            db.session.commit()
            return task.__dict__

        def delete(self, task_id):
            task = Task.query.get(task_id)
            db.session.delete(task)
            db.session.commit()
            return '', 204

    class TaskStatus(Resource):
        def put(self, task_id):
            task = Task.query.get(task_id)
            task.completed = not task.completed
            db.session.commit()
            return task.__dict__

    api.add_resource(TaskList, '/tasks')
    api.add_resource(TaskDetail, '/tasks/<int:task_id>')
    api.add_resource(TaskStatus, '/tasks/<int:task_id>/status')
    

    