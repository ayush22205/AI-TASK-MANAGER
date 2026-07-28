from fastapi import FastAPI , Depends , HTTPException
from sqlalchemy.orm import Session
from database import engine , SessionLocal
import model , schemas
from passlib.context import CryptContext

app = FastAPI()
pwd_context = CryptContext(schemes=["bcrypt"])

model.Base.metadata.create_all(bind = engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/user_data" , response_model= schemas.Response)
def create_user_data( data : schemas.Create , db : Session = Depends(get_db)):
    new_user = model.User(

        username = data.username,
        email = data.email,
        hash_password = pwd_context.hash(data.hash_password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
    