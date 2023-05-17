import uvicorn
from fastapi import FastAPI
from utils.config import BASE
from utils.db_conn import database
from routers import member, book, restaurant
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(member.router)
app.include_router(book.router)
app.include_router(restaurant.router)


# @app.on_event("startup")
# async def startup():
#     BASE.metadata.drop_all(database.engine)
#     BASE.metadata.create_all(database.engine)
#     with database.engine.connect() as con:
#         with open("./init.sql", "r", encoding="utf-8") as f:
#             sqlCommands = f.read().split(";")
#             for command in sqlCommands:
#                 if command.strip():
#                     con.execute(command)


@app.get("/")
async def root():
    return {"msg": 0}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8001, reload=True)
