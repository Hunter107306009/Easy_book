from fastapi import APIRouter
from sqlalchemy.orm.session import Session
from fastapi.params import Depends
from utils.db_conn import get_db
from services.member import business, schema
import uuid

router = APIRouter(prefix="/member", tags=["member"])


@router.post("/create_member", summary="註冊")
async def create_member(
    createMemberRequest: schema.CreateMemberRequest, db: Session = Depends(get_db)
):
    # uuid_code = str(uuid.uuid4())
    return await business.create_member(createMemberRequest, db)
