from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm  # ADD THIS
from sqlalchemy.orm import Session
from database import engine, SessionLocal
import model, schemas
from passlib.context import CryptContext
from auth import create_token, verify_token

app = FastAPI()
pwd_context = CryptContext(schemes=["bcrypt"])
model.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/register", response_model=schemas.Response)
def register(data: schemas.Create, db: Session = Depends(get_db)):
    existing = db.query(model.User).filter(model.User.email == data.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    new_user = model.User(
        username=data.username,
        email=data.email,
        hash_password=pwd_context.hash(data.hash_password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@app.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
  
    user = db.query(model.User).filter(model.User.email == form_data.username).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if not pwd_context.verify(form_data.password, user.hash_password):
        raise HTTPException(status_code=401, detail="Wrong password")

    token = create_token(data={"sub": user.email})
    return {"access_token": token, "token_type": "bearer"}



@app.get("/me", response_model=schemas.Response)
def get_me(current_user_email: str = Depends(verify_token), db: Session = Depends(get_db)):
    user = db.query(model.User).filter(model.User.email == current_user_email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@app.get("/get_user/{username}", response_model=schemas.Response)
def get_user(username: str, db: Session = Depends(get_db), current_user_email: str = Depends(verify_token)):
    user = db.query(model.User).filter(model.User.username == username).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@app.get("/get_all", response_model=list[schemas.Response])
def get_all(db: Session = Depends(get_db), current_user_email: str = Depends(verify_token)):
    return db.query(model.User).all()


@app.put("/change_in_user/{username}", response_model=schemas.Response)
def change_in_user(
    username: str,
    new_data: schemas.Create,
    db: Session = Depends(get_db),
    current_user_email: str = Depends(verify_token)
):
    existing_user = db.query(model.User).filter(model.User.username == username).first()
    if not existing_user:
        raise HTTPException(status_code=404, detail="User not found")
    existing_user.username = new_data.username
    existing_user.email = new_data.email
    existing_user.hash_password = pwd_context.hash(new_data.hash_password)
    db.commit()
    db.refresh(existing_user)
    return existing_user
    

@app.delete("/delete_user/{username}")
def delete_user(username: str, db: Session = Depends(get_db), current_user_email: str = Depends(verify_token)):
    user_to_delete = db.query(model.User).filter(model.User.username == username).first()
    if not user_to_delete:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user_to_delete)
    db.commit()
    return {"message": "User deleted successfully"}