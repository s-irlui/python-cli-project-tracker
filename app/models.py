from app.base import BaseModel

class User(BaseModel):
    def __init__(self, user_id, name, email):
        super().__init__(user_id)
        self.name = name
        self.email = email

    def to_dict(self):
        return {
            "user_id": self.id,
            "name": self.name,
            "email": self.email
        }


class Project(BaseModel):
    def __init__(self, project_id, title, description, user_id):
        self.project_id = project_id
        self.title = title
        self.description = description
        self.user_id = user_id

    def to_dict(self):
        return {
            "project_id": self.project_id,
            "title": self.title,
            "description": self.description,
            "user_id": self.user_id
        }


class Task:
    def __init__(self, task_id, title, project_id, contributors=None, completed=False):
        self.task_id = task_id
        self.title = title
        self.project_id = project_id
        self.contributors = contributors if contributors else []
        self.completed = completed

    def mark_complete(self):
        self.completed = True

    def to_dict(self):
        return {
            "task_id": self.task_id,
            "title": self.title,
            "project_id": self.project_id,
            "contributors": self.contributors,
            "completed": self.completed
        }