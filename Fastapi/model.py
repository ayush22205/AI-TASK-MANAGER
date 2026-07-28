from sqlalchemy import  Column , Integer , String , DateTime , Text
from datetime import datetime
from database import Base

class user(Base):
    __tablename__ = "users"
    id = Column(Integer , primary_key= True , index = True)
    username = Column(String , unique= True , nullable = False)
    email = Column(String , unique= True , nullable= False)
    hash_password = Column(String , nullable= False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)




