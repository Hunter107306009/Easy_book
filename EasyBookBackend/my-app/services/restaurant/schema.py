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


class RestaurantLoginRequest(BaseModel):
    RAccount: str
    Rpwd: str


###############
class RestaurantRequest(BaseModel):
    RID: int
    Rname: str
    Rphone: int
    RAddress: str
    RAccount: str
    RPwd: str
    image_url: str


class UpdateRestaurantRequest(BaseModel):
    RPwd: str
    RID: int
    RName: str
    RPhone: str
    RAddress: str
    URL: str


class AddToBlacklistRequest(BaseModel):
    Phone: str


class AddConsumptionRecordRequest(BaseModel):
    Phone: str
    RID: int
    Consumptions: int
