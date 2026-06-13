from fastapi import FastAPI

from database import init_db
from routers import tasks, users
import auth

app = FastAPI()

# create tables
init_db()

# routers
app.include_router(tasks.router)
app.include_router(users.router)
app.include_router(auth.router)


@app.get("/")
def home():
    return {"message": "Task Manager API running"}