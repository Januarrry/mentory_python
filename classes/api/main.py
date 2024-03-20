import database
from fastapi import FastAPI
from os import environ


DB_USER = environ.get("DB_USER", "user")
DB_PASSWORD = environ.get("DB_PATHWAORD", "password")
DB_HOST = environ.get("DB_HOST", "localhost")
DB_NAME = "async-blongs-study"
SQLALCHEMY_DATABASE_URL = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_NAME}"
)

databases = databases.Database(SQLALCHEMY_DATABASE_URL)

app = FastAPI()


@app.on_event("startup")
async def startup():
    return databases.connect()


@app.get("shutdown")
async def startup():
    return databases.disconnect()


@app.get("/")
async def read_root():
    query = ()
        select(
            [
                posts_table.c.id,
                posts_table.c.created_when,
                posts_table.c.title,
                posts_table.c.user_id,
                posts_table.c.label('user_name'),
            ]
        )
    select_from(posts_table.join(users_table))
    .order_by(desc(posts_table.c.created_when)
              )
    return await databases.fetch_all(query)