from database.schema import User
from utils.validate_bson import get_object_id
from authentication.hashing import hashPassword
from mongoengine.errors import MongoEngineException
from models.model import UserField
from exceptions.custom_exception import BadRequestException, ServerErrorException




class UserRepository:

    @staticmethod
    async def create_user(user_model:UserField):

        try:

            user = User(
                firstname=user_model.firstname,
                lastname = user_model.lastname, 
                email = user_model.email,
                password = hashPassword(user_model.password))
            
            user.save()

            return user
        
        except MongoEngineException as e:

            raise BadRequestException(str(e))
        
        except Exception as e:

            raise ServerErrorException(str(e))

    @staticmethod
    async def get_by_id(user_id:str):

        try:

            user_id = get_object_id(user_id)

            user:User = User.objects.get(id=user_id)

            return user


        except MongoEngineException as e:

            raise BadRequestException(str(e))
        
        except Exception as e:

            raise ServerErrorException(str(e))
        

    @staticmethod
    async def get_by_email(email:str):

        try:

            user:User = User.objects.get(email=email)

            return user
        
        except User.DoesNotExist:
            return None
        

    @staticmethod
    async def get_all():

        try:

            all_users = [user.to_dict() for user in User.objects.all()]

            return all_users


        except MongoEngineException as e:

            raise BadRequestException(str(e))
        
        except Exception as e:

            raise ServerErrorException(str(e))


    