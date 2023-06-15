import datetime
import time
import pandas
import pytz
from batchjob_config import Base, engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func


class Seats(Base):
    """"""

    __tablename__ = "SEATS"
    __table_args__ = {"autoload": True}


class SeatsRecord(Base):
    """"""

    __tablename__ = "SEATSRECORD"
    __table_args__ = {"autoload": True}


class SeatsRecordCreate:
    def __init__(self):
        self.session = self.loadSession()

    def loadSession(self):
        """"""
        Session = sessionmaker(bind=engine)
        session = Session()
        return session

    def close(self):
        self.session.close()


def main():
    print("main start")
    task = SeatsRecordCreate()

    task.close()
    print("main end")


if __name__ == "__main__":
    main()
