from pydantic import BaseModel

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