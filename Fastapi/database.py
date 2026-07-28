from sqlalchemy import  create_engine , Column , Integer , String , DateTime
from sqlalchemy.orm import declarative_base , sessionmaker
from datetime import datetime

URL = "postgresql://postgres:ayush123@localhost:5432/taskmanager"

engine = create_engine(URL)

SessionLocal = sessionmaker(bind = engine)

Base= declarative_base()

class user(Base):
    __tablename__ = "users"
    id = Column(Integer , primary_key= True , index = True)
    username = Column(String , unique= True , nullable = False)
    email = Column(String , unique= True , nullable= False)
    hash_password = Column(String , nullable= False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

Base.metadata.create_all(bind= engine)



