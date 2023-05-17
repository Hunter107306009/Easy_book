from fastapi import APIRouter
from sqlalchemy.orm.session import Session
from fastapi.params import Depends
from utils.db_conn import get_db
from services.restaurant import business

router = APIRouter(prefix="/restaurant", tags=["restaurant"])


@router.get("/")
async def root():
    return {"msg": 0}
