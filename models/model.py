from pydantic import BaseModel



class UserField(BaseModel):
    firstname:str
    lastname:str
    email:str
    password:str
    
