from sqlalchemy import  Column , Integer , String , DateTime , Text , Enum , ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime , timezone
from database import Base
import enum


class User(Base):
    __tablename__ = "users"
    id = Column(Integer , primary_key= True , index = True)
    username = Column(String , unique= True , nullable = False)
    email = Column(String , unique= True , nullable= False)
    hash_password = Column(String , nullable= False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    tasks = relationship("Task", back_populates="owner")



class PriorityEnum( str , enum.Enum):
    low = "low"
    medium  = "medium"
    high = "high"

class StatusEnum( str , enum.Enum):
    todo = "todo"
    in_progress = "in_progress"
    done = "done"

class Task(Base):
    __tablename__ = "tasks"

    id = Column( Integer , primary_key= True , index = True)
    title = Column( String ,  nullable = False)
    description = Column( String , nullable= True)
    priority = Column( Enum(PriorityEnum) , default= PriorityEnum.medium)
    status = Column( Enum(StatusEnum) , default= StatusEnum.todo)
    due_date = Column( DateTime ,nullable = True )
    created_at = Column( DateTime  , default= lambda: datetime.now(timezone.utc))

    user_id = Column( Integer, ForeignKey("users.id") , nullable = False)
    owner = relationship("User" ,back_populates = "tasks")

