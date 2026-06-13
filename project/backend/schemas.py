from pydantic import BaseModel
from typing import Optional


# TASK CREATE
class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    status: Optional[str] = "pending"


# TASK UPDATE (MISSING BEFORE → NOW FIXED)
class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None


# OPTIONAL: TASK RESPONSE
class Task(BaseModel):
    id: int
    title: str
    description: Optional[str]
    status: str