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

    print(data.hash_password)
    print(type(data.hash_password))
    print(len(data.hash_password))
    new_user = model.User(

        username = data.username,
        email = data.email,
        hash_password = pwd_context.hash(data.hash_password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
    
@app.get("/get_user/{username}" , response_model= schemas.Response )
def get_user( username : str  , db : Session = Depends(get_db)):
    user = db.query(model.User).filter(model.User.username == username).first()

    if not user:
        raise HTTPException(
            status_code= 404 ,
            detail= "User not found"
        )
    return user

@app.get("/get_all" , response_model= list[schemas.Response])
def get_all(db : Session = Depends(get_db)):
    return db.query(model.User).all()

@app.put("change_in_user/{username}")
def change_in_user( username : str , new_user : schemas   .Create ,  db : Session = Depends( get_db)):
    existing_user = db.query(model.User).filter(model.User.username == username).first()
    if not existing_user:
        raise HTTPException( status_code= 404 , detail= "User not found")
    existing_user.username = new_user.username
    existing_user.email = new_user.email
    existing_user.hash_password =  pwd_context.hash(new_user.hash_password)

@app.delete("/delete_user/{username}")
def delete_user( username : str , db : Session = Depends(get_db)):

    user_to_be_deleted = db.query(model.User).filter(model.User.username == username).first()

    if not user_to_be_deleted :
         raise HTTPException( status_code= 404 , detail= " User not found")

    db.delete(user_to_be_deleted)
    db.commit()
    return{

        "message ":"user deleted"
    }
