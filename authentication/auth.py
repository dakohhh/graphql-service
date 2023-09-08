from repository.user import UserRepository
from .hashing import checkPassword
from .tokens import create_access_token
from exceptions.custom_exception import BadRequestException


async def authenticate_user(email:str, password:str):

    user = await UserRepository.get_by_email(email)

    if user is None or not checkPassword(password, user.password):
        raise BadRequestException("Incorrect email or password")
 
    access_token = create_access_token(str(user.id))

    return access_token