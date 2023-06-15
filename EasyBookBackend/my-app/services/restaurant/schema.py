import re
import datetime
from pydantic.main import BaseModel
from typing import Optional


class CreateRestaurantRequest(BaseModel):
    RAccount: str
    Rpwd: str
    RName: str
    RPhone: str
    RAddress: Optional[str] = None
    Url: str
