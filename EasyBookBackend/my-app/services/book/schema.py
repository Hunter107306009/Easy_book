import re
import datetime
from pydantic.main import BaseModel
from typing import Optional


class BookRequest(BaseModel):
    ID: int
    RID: int
    Name: str
    Phone: str
    Reason: str
    ReTime: datetime.datetime
    Person: int


class CancelRequest(BaseModel):
    ReNumber: int
    ID: int
    RID: int
    BookTime: datetime.datetime
    CTNo: str


class UpdateBookRequest(BaseModel):
    ReNumber: int
    ID: int
    RID: int
    BookTime: datetime.datetime
    Person: int
    Reason: str
