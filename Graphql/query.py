import strawberry
from typing import List
from repository.user import UserRepository




@strawberry.type
class Query:

    @strawberry.field
    def TestField(self) ->str:
        return "Test"


    

        