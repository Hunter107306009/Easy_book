from fastapi import APIRouter
from sqlalchemy.orm.session import Session
from fastapi.params import Depends
from utils.db_conn import get_db
from services.book import business
from services.book import business, schema
from datetime import datetime


router = APIRouter(prefix="/book", tags=["book"])


@router.post("/book", summary="訂位")
async def book(bookRequest: schema.BookRequest, db: Session = Depends(get_db)):
    return await business.book(bookRequest, db)


@router.delete("/cancel_book", summary="取消訂位")
async def cancel_book(ReNumber: int, db: Session = Depends(get_db)):
    return await business.cancel_book(ReNumber, db)


@router.patch("/update_book", summary="修改訂位")
async def update_book(
    updateBookRequest: schema.UpdateBookRequest, db: Session = Depends(get_db)
):
    return await business.update_book(updateBookRequest, db)


@router.get("/query_book_member", summary="會員查詢訂位")
async def query_book_member(MemberID: int, db: Session = Depends(get_db)):
    return await business.query_book_member(MemberID, db)


@router.get("/query_book_restaurant", summary="店家查詢訂位")
async def query_book_restaurant(RID: int, db: Session = Depends(get_db)):
    return await business.query_book_restaurant(RID, db)
    

@router.post("/check_seats", summary="店家查詢座位資訊")
async def check_seats(checkBookRequest:schema.CheckSeatsRequest, db: Session = Depends(get_db)):
    return await business.check_seats(checkBookRequest, db)
