import re
import datetime
from pydantic.main import BaseModel
from typing import Optional


class BookRequest(BaseModel):
    ID: int
    RID: int
    Reason: str
    ReTime: datetime.datetime
    Person: int


class UpdateBookRequest(BaseModel):
    ReNumber: int
    ID: int
    RID: int
    BookTime: datetime.datetime
    Person: int
    Reason: str


class QueryMemberRequest(BaseModel):
    MemberID: int


class QueryRestaurantRequest(BaseModel):
    RID: int
