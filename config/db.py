import pymongo
import os
from dotenv import load_dotenv

# os.makedirs("databases/tmp", exist_ok=True)
global db_conn

def init_db():
    global db_conn
    load_dotenv()
    DATABASE_NAME = os.getenv("DATABASE_NAME", "app")

    mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")
    db_conn = mongo_client[DATABASE_NAME]
    user_collection =db_conn["users"]

    if not user_collection.find_one({"username":"Admin"}):
        user_collection.insert_one({"username":"Admin", "password":"12345678", "admin": "True"})

    print("Connected and created tables")
    

def get_db_conn():
    return db_conn
    