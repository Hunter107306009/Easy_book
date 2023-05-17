from fastapi import APIRouter
from sqlalchemy.orm.session import Session
from fastapi.params import Depends
from utils.db_conn import get_db
from services.member import business

router = APIRouter(prefix="/member", tags=["member"])


@router.get("/")
async def root():
    return {"msg": 0}
