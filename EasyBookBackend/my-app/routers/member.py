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
    return await business.create_member(createMemberRequest, db)


@router.post("/login", summary="登入")
async def login(loginRequest: schema.LoginRequest, db: Session = Depends(get_db)):
    return await business.login(loginRequest, db)


@router.get("/get_member_info", summary="查詢會員基本資料")
async def get_member_info(id: int, db: Session = Depends(get_db)):
    return await business.get_member_info(id, db)


@router.patch("/update_member", summary="修改會員資料")
async def update_member(
    updateMemberRequest: schema.UpdateMemberRequest, db: Session = Depends(get_db)
):
    return await business.update_member(updateMemberRequest, db)


@router.get("/get_member_paypoints_info", summary="會員點數/消費紀錄查詢")
async def get_member_paypoints_info(id: int, db: Session = Depends(get_db)):
    return await business.get_member_paypoints_info(id, db)
