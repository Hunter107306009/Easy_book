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
