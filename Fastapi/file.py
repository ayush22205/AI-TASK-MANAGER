from fastapi import FastAPI
from database import engine
import model

app = FastAPI()

model.Base.metadata.create_all(bind = engine)

@app.get("/")
def home():
    return{
        "message":"successfull"
    }