import pymongo
import os
from dotenv import load_dotenv
from werkzeug.security import generate_password_hash

global db_conn

def init_db():
    global db_conn
    load_dotenv()
    DATABASE_NAME = os.getenv("DATABASE_NAME", "app")
    DATABASE_SERVER = os.getenv("DATABASE_SERVER")

    mongo_client = pymongo.MongoClient(DATABASE_SERVER)
    db_conn = mongo_client[DATABASE_NAME]
    user_collection =db_conn["users"]

    if not user_collection.find_one({"username":"Admin"}):
        password = generate_password_hash("Tt345678!")
        user_collection.insert_one({"username":"Admin", "password": password, "telegram":"andy_tchu", "admin": "True"})
        user_collection.create_index([("username", pymongo.ASCENDING)], unique=True)

    print("Connected and created tables")
    

def get_db_conn():
    return db_conn
    