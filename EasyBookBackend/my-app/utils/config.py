from decimal import Decimal

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# 新增類別方法.
class BASE(object):
    def json(self, skip=[]):
        result = {}
        cols = [
            name
            for name in dir(self)
            if not name.startswith("__")
            and not name.startswith("_")
            and not name.startswith("json")
            and not name.startswith("metadata")
            and not name.startswith("registry")
        ]
        for i in cols:
            if i in skip:
                continue
            # Decimal 無法轉換Json, 將Decimal轉為float後轉為string
            val = getattr(self, i) if type(getattr(self, i)
                                           ) != Decimal else str(float(getattr(self, i)))
            result[i] = val
        return result


BASE = declarative_base(cls=BASE)


class DatabaseBasic:
    def __init__(self, account, password, address, database):
        self.account = account
        self.password = password
        self.address = address
        self.database = database
        self.session = None
        self.connection = None

        self.engine = create_engine(
            f"mysql+pymysql://{self.account}:{self.password}@{self.address}/{self.database}?charset=utf8mb4",
            convert_unicode=True,
            pool_pre_ping=True,
            pool_recycle=900,
        )

        self.SessionLocal = sessionmaker(
            bind=self.engine, autocommit=False, autoflush=True)
