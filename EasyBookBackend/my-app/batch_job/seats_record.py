import datetime
import time
import pandas
import pytz
from batchjob_config import Base, engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func
import datetime
import calendar
from dateutil.relativedelta import relativedelta
from sqlalchemy import (
    INTEGER,
    Column,
    DateTime,
    ForeignKey,
    String,
    FLOAT,
    Text,
    Index,
)


class Restaurant(Base):
    """"""

    __tablename__ = "RESTAURANT"

    RID = Column(INTEGER, primary_key=True, nullable=False, autoincrement=True)
    RName = Column(String(255), nullable=False)
    RPhone = Column(String(20), nullable=False)
    RAddress = Column(String(255))
    RAccount = Column(String(100), nullable=False)
    RPwd = Column(String(255), nullable=False)
    URL = Column(Text)


class Seats(Base):
    """"""

    __tablename__ = "SEATS"

    RID = Column(
        INTEGER, ForeignKey("RESTAURANT.RID"), primary_key=True, nullable=False
    )
    TNo = Column(String(10), primary_key=True, nullable=False)
    Seats = Column(INTEGER)

    Index("idx_tno", TNo)


class SeatsRecord(Base):
    """"""

    __tablename__ = "SEATSRECORD"

    SRID = Column(INTEGER, primary_key=True, nullable=False, autoincrement=True)
    RID = Column(INTEGER, ForeignKey("RESTAURANT.RID"), nullable=False)
    Seats = Column(String(10), nullable=False)
    TNo = Column(String(10), ForeignKey("SEATS.TNo"), nullable=False)
    BookTime = Column(DateTime, nullable=False)
    Is_Reserved = Column(String(1), nullable=False)


class SeatsRecordCreate:
    def __init__(self):
        self.session = self.loadSession()

    def loadSession(self):
        """"""
        Session = sessionmaker(bind=engine)
        session = Session()
        return session

    def StartCreateTable(self):
        ###Create Datetime
        time_list = [
            "11:00:00",
            "12:00:00",
            "13:00:00",
            "17:00:00",
            "18:00:00",
            "19:00:00",
            "20:00:00",
        ]

        next_month_first_date = (
            datetime.date.today() + relativedelta(months=1)
        ).replace(day=1)

        day_count = calendar.monthrange(
            next_month_first_date.year, next_month_first_date.month
        )[1]

        date_list = [
            (next_month_first_date + relativedelta(days=i)).strftime("%Y-%m-%d")
            for i in range(day_count)
        ]

        date_time_list = []
        for date in date_list:
            for time in time_list:
                date_time_list.append(f"{date} {time}")

        ###Get Seats Data
        seats_info = [
            {"RID": data[0], "TNo": data[1], "Seats": data[2]}
            for data in self.session.query(Seats.RID, Seats.TNo, Seats.Seats).all()
        ]

        ###Join Seats & Time
        final_table = []

        for seats in seats_info:
            for times in date_time_list:
                new_dict = {
                    "RID": seats["RID"],
                    "TNo": seats["TNo"],
                    "Seats": seats["Seats"],
                    "BookTime": times,
                }
                final_table.append(new_dict)

        ### Insert Data to DB
        for each in final_table:
            self.session.add(
                SeatsRecord(
                    RID=each["RID"],
                    Seats=each["Seats"],
                    TNo=each["TNo"],
                    BookTime=each["BookTime"],
                    Is_Reserved="F",
                )
            )

            self.session.commit()

    def close(self):
        self.session.close()


def main():
    print("main start")
    task = SeatsRecordCreate()
    task.StartCreateTable()
    task.close()
    print("main end")


if __name__ == "__main__":
    main()
