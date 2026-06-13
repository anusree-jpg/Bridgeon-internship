from fastapi import APIRouter, HTTPException
from database import get_connection
from schemas import TaskCreate, TaskUpdate

router = APIRouter(prefix="/tasks", tags=["Tasks"])


# CREATE TASK
@router.post("/")
def create_task(task: TaskCreate):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO tasks (title, description, status) VALUES (?, ?, ?)",
        (task.title, task.description, task.status)
    )

    conn.commit()
    conn.close()

    return {"message": "Task created successfully"}


# GET ALL TASKS
@router.get("/")
def get_tasks():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tasks")
    rows = cursor.fetchall()

    conn.close()

    return [dict(row) for row in rows]


# GET TASK BY ID
@router.get("/{task_id}")
def get_task(task_id: int):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tasks WHERE id=?", (task_id,))
    row = cursor.fetchone()

    conn.close()

    if not row:
        raise HTTPException(status_code=404, detail="Task not found")

    return dict(row)


# UPDATE TASK
@router.put("/{task_id}")
def update_task(task_id: int, task: TaskUpdate):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE tasks
        SET title=?, description=?, status=?
        WHERE id=?
    """, (task.title, task.description, task.status, task_id))

    conn.commit()
    conn.close()

    return {"message": "Task updated successfully"}


# DELETE TASK
@router.delete("/{task_id}")
def delete_task(task_id: int):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM tasks WHERE id=?", (task_id,))

    conn.commit()
    conn.close()

    return {"message": "Task deleted successfully"}