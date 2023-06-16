import re
import datetime
from pydantic.main import BaseModel
from typing import Optional


class CreateMemberRequest(BaseModel):
    name: str
    phone: str
    pwd: str
    gender: Optional[str] = None
    birthday: Optional[datetime.datetime] = None


class UpdateMemberRequest(BaseModel):
    ID: int
    name: str
    pwd: str
    gender: Optional[str] = None
    birthday: Optional[datetime.datetime] = None


class LoginRequest(BaseModel):
    phone: str
    pwd: str
