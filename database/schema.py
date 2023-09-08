from mongoengine import Document, StringField, EmailField, DateTimeField
from datetime import datetime




class User(Document):

    firstname = StringField(required=True, max_length=200)

    lastname = StringField(required=True, max_length=200)

    email = EmailField(required=True, unique=True,  max_length=250)

    password =  StringField(required=True)

    created_at = DateTimeField(default=datetime.now())

    updated_at = DateTimeField(default=datetime.now())



    def to_dict(self):

        return {
            "id": str(self.id),
            "firstname": self.firstname,
            "lastname": self.lastname,
            "email": self.email,
            "created_at":self.created_at,
            "updated_at":self.updated_at
        }
