from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from enum import Enum

class Create(BaseModel):

    username : str
    email : str 
    hash_password : str

class Response(BaseModel):
    id : int 
    username : str 
    email : str

    class Config:
        from_attributes = True

class Login(BaseModel):
    email: str
    password: str

class PriorityEnum( str , Enum):
    low = "low"
    medium = "medium"
    high = "high"

class StatusEnum( str , Enum):
    todo = "todo"
    in_progress = "in_progress"
    done = "done"

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    priority: PriorityEnum = PriorityEnum.medium
    status: StatusEnum = StatusEnum.todo
    due_date: Optional[datetime] = None

class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    priority: PriorityEnum
    status: StatusEnum
    due_date: Optional[datetime]
    created_at: datetime
    user_id: int

    class Config:
        from_attributes = True