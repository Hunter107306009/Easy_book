from utils.config import BASE
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


class Member(BASE):
    __tablename__ = "MEMBER"

    ID = Column(INTEGER, primary_key=True, nullable=False, autoincrement=True)
    Name = Column(String(255), nullable=False)
    Phone = Column(String(20), nullable=False)
    Pwd = Column(String(255), nullable=False)
    Gender = Column(String(20))
    Birthday = Column(DateTime)
    MLevel = Column(INTEGER, nullable=False)
    MPoints = Column(INTEGER)
    MAccumSpend = Column(FLOAT(10, 2))


class Restaurant(BASE):
    __tablename__ = "RESTAURANT"

    RID = Column(INTEGER, primary_key=True, nullable=False, autoincrement=True)
    RName = Column(String(255), nullable=False)
    RPhone = Column(String(20), nullable=False)
    RAddress = Column(String(255))
    RAccount = Column(String(100), nullable=False)
    RPwd = Column(String(255), nullable=False)
    URL = Column(Text)


class Seats(BASE):
    __tablename__ = "SEATS"

    RID = Column(
        INTEGER, ForeignKey("RESTAURANT.RID"), primary_key=True, nullable=False
    )
    TNo = Column(String(10), primary_key=True, nullable=False)
    Seats = Column(INTEGER)

    Index("idx_tno", TNo)


class SeatsRecord(BASE):
    __tablename__ = "SEATSRECORD"

    SRID = Column(INTEGER, primary_key=True, nullable=False, autoincrement=True)
    RID = Column(INTEGER, ForeignKey("RESTAURANT.RID"), nullable=False)
    Seats = Column(String(10), nullable=False)
    TNo = Column(String(10), ForeignKey("SEATS.TNo"), nullable=False)
    BookTime = Column(DateTime, nullable=False)
    Is_Reserved = Column(String(1), nullable=False)


class Reservation(BASE):
    __tablename__ = "RESERVATION"

    ReNumber = Column(INTEGER, primary_key=True, nullable=False, autoincrement=True)
    ReRID = Column(INTEGER, ForeignKey("RESTAURANT.RID"), nullable=False)
    ReMID = Column(INTEGER, ForeignKey("MEMBER.ID"), nullable=False)
    Reason = Column(String(255))
    CreateTime = Column(DateTime, nullable=False)
    ReTime = Column(DateTime, nullable=False)
    ReTNo = Column(String(10), nullable=False)
    RePerson = Column(INTEGER, nullable=False)


class BlackList(BASE):
    __tablename__ = "BLACKLIST"

    BID = Column(INTEGER, ForeignKey("MEMBER.ID"), primary_key=True, nullable=False)
    NonArrive = Column(INTEGER)


class Consumptions(BASE):
    __tablename__ = "CONSUMPTIONS"

    ID = Column(INTEGER, primary_key=True, nullable=False, autoincrement=True)
    CMID = Column(INTEGER, ForeignKey(Member.ID), nullable=False)
    CRID = Column(INTEGER, ForeignKey(Restaurant.RID), nullable=False)
    CTime = Column(DateTime, nullable=False)
    Consumptions = Column(INTEGER, nullable=False)
    PointsChange = Column(INTEGER, nullable=False)
