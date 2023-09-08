import os
import certifi
import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from database.config import DB_CONFIG
from Graphql.query import Query
from Graphql.mutation import Mutation
from mongoengine import connect, disconnect_all




app = FastAPI()




# Connect to MongoDB on startup
@app.on_event("startup")
def startup_event():

    # Verify application certificate with MongoDB
    CERTIFICATE = os.path.join(os.path.dirname(certifi.__file__), "cacert.pem")

    connect(host=DB_CONFIG, tls=True, tlsCAFile=CERTIFICATE)




# Disconnect from MongoDB on shutdown
@app.on_event("shutdown")
def shutdown_event():
    disconnect_all()




# Initialize GraphQL Router
schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_router = GraphQLRouter(schema)

app.include_router(graphql_router, prefix="/graphql")





@app.get("/")
def home():
    return "Welcome Man"

