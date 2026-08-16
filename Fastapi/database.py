from sqlalchemy import  create_engine 
from sqlalchemy.orm import declarative_base , sessionmaker 
from datetime import datetime

URL = "postgresql://postgres:ayush123@db:5432/taskmanager"

engine = create_engine(URL)

SessionLocal = sessionmaker(bind = engine)

Base= declarative_base()



def get_db():
    db =SessionLocal()
    try:
        yield db
    finally:
        db.close()



