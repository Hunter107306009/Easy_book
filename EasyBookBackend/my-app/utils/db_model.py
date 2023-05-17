from utils.config import BASE
from sqlalchemy import INTEGER, Column, DateTime, ForeignKey, String, FLOAT


class Member(BASE):
    __tablename__ = "MEMBER"

    ID = Column(String(200), primary_key=True, nullable=False)
    Name = Column(String(255), nullable=False)
    Phone = Column(String(20), nullable=False)
    MLevel = Column(INTEGER, nullable=False)
    MPoints = Column(INTEGER)
    AccumSpend = Column(FLOAT(10, 2))


class Alternate(BASE):
    __tablename__ = "ALTERNATE"

    ALNO = Column(INTEGER, primary_key=True, nullable=False)
    ALRID = Column(INTEGER, primary_key=True, nullable=False)
    ALOrder = Column(INTEGER)


class BlackList(BASE):
    __tablename__ = "BLACKLIST"

    BID = Column(INTEGER, primary_key=True, nullable=False)
    BPhone = Column(String(20), primary_key=True, nullable=False)
    NonArriv = Column(INTEGER)


class Consumptions(BASE):
    __tablename__ = "CONSUMPTIONS"

    CID = Column(INTEGER, primary_key=True, nullable=False)
    CRID = Column(INTEGER, primary_key=True, nullable=False)
    CTime = Column(DateTime, primary_key=True, nullable=False)
    CTNo = Column(INTEGER, nullable=False)
    Consumptions = Column(FLOAT(10, 2))


class Reservation(BASE):
    __tablename__ = "RESERVATION"

    ReNumber = Column(INTEGER, primary_key=True, nullable=False)
    ReRID = Column(INTEGER, primary_key=True, nullable=False)
    RePhone = Column(String(20), nullable=False)
    ResName = Column(String(255), nullable=False)
    Reason = Column(String(255))
    ReTime = Column(DateTime, nullable=False)
    ReTNo = Column(INTEGER, nullable=False)
    ReDate = Column(DateTime)


class Restaurant(BASE):
    __tablename__ = "RESTAURANT"

    RID = Column(INTEGER, primary_key=True, nullable=False)
    RName = Column(String(255))
    RPhone = Column(String(20), nullable=False)
    RAddress = Column(String(255))


class Seats(BASE):
    __tablename__ = "SEATS"

    SRID = Column(INTEGER, primary_key=True, nullable=False)
    TNo = Column(INTEGER, primary_key=True, nullable=False)
    AttendToday = Column(INTEGER)
    Idle = Column(String(5))
    Seats = Column(INTEGER)
