from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware  # middleware helper
from fastapi_sqlalchemy import db  # an object to provide global access to a database session

from models.posts import Posts

app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url="sqlite://")

# once the middleware is applied, any route can then access the database session
# from the global ``db``

@app.get("/users")
def get_users():
    users = db.session.query(Posts).all()

    return users