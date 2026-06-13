class User:
    def __init__(self, id, username, email, hashed_password):
        self.id = id
        self.username = username
        self.email = email
        self.hashed_password = hashed_password


class Task:
    def __init__(self, id, task_name, description, priority, due_date, completed):
        self.id = id
        self.task_name = task_name
        self.description = description
        self.priority = priority
        self.due_date = due_date
        self.completed = completed