import strawberry
from .schema import UserInput, Token, UserReturnType, LoginInput
from authentication.auth import authenticate_user
from exceptions.custom_exception import BadRequestException
from models.model import UserField
from repository.user import UserRepository




@strawberry.type
class Mutation:


    @strawberry.mutation
    async def signup(self, user_input: UserInput) -> UserReturnType:

        # Validate user input with pydantic
        user_field = UserField(
            firstname=user_input.firstname, 
            lastname=user_input.lastname, 
            email=user_input.email, 
            password=user_input.password)
        

        # Check if user exist
        if await UserRepository.get_by_email(user_input.email):

            raise BadRequestException("Email already exist")


        # Save user to database
        user  = await UserRepository.create_user(user_field)

        return UserReturnType(**user.to_dict())
    

    @strawberry.mutation
    async def login_user(self, login_input: LoginInput) -> Token:

        token = await authenticate_user(login_input.email, login_input.password)


        return Token(access_token=token)
    





