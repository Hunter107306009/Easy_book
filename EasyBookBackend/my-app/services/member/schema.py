import re
from pydantic.main import BaseModel
from typing import Optional


class CreateMemberRequest(BaseModel):
    name: str
    phone: str
    pwd: str
