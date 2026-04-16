from fastapi import FastAPI, HTTPException
from motor.motor_asyncio import AsyncIOMotorClient
import mysql.connector
import os

app = FastAPI()

MONGO_URL = os.getenv("MONGO_URL", "mongodb://admin:password@db_mongo:27017")
MYSQL_CONFIG = {
    'user': 'root',
    'password': os.getenv('MYSQL_ROOT_PASSWORD'),
    'host': 'db_mysql',
    'database': os.getenv('MYSQL_DATABASE')
}

@app.get("/posts")
async def get_posts():
    client = AsyncIOMotorClient(MONGO_URL)
    db = client.blog_db
    cursor = db.posts.find({}, {"_id": 0})
    posts = await cursor.to_list(length=100)
    return posts

@app.get("/users")
def get_users():
    try:
        conn = mysql.connector.connect(**MYSQL_CONFIG)
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM utilisateurs")
        users = cursor.fetchall()
        cursor.close()
        conn.close()
        return users
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))