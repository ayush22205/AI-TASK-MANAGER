from fastapi import FastAPI 
import database
from dotenv import load_dotenv
import os

app = FastAPI()

load_dotenv()
URL = os.getenv("DATABASE_URL")

@app.get("/")
def home():
    return{

        "message":"successfull"
    }
