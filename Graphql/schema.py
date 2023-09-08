import strawberry



@strawberry.type
class Token:
    access_token:str



@strawberry.type
class UserReturnType:
    id:str
    firstname:str
    lastname:str
    email:str
    created_at:str
    updated_at:str




@strawberry.input
class UserInput:
    firstname:str
    lastname:str
    email:str
    password:str

@strawberry.input
class LoginInput:
    email:str
    password:str
