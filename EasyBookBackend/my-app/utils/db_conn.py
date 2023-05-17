import os

from . import config

database = config.DatabaseBasic(
    os.environ["ACCOUNT"],
    os.environ["PASSWORD"],
    os.environ["ADDRESS"],
    os.environ["DATABASE"],
)


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()
