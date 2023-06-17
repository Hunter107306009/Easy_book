from fastapi import APIRouter
from sqlalchemy.orm.session import Session
from fastapi.params import Depends
from utils.db_conn import get_db
from services.book import business
from services.book import business, schema


router = APIRouter(prefix="/book", tags=["book"])


@router.post("/book", summary="訂位")
async def book(bookRequest: schema.BookRequest, db: Session = Depends(get_db)):
    return await business.book(bookRequest, db)


@router.delete("/cancel_book", summary="取消訂位")
async def cancel_book(
    cancelRequest: schema.CancelRequest, db: Session = Depends(get_db)
):
    return await business.cancel_book(cancelRequest, db)


@router.patch("/update_book", summary="修改訂位")
async def update_book(
    updateBookRequest: schema.UpdateBookRequest, db: Session = Depends(get_db)
):
    return await business.update_book(updateBookRequest, db)
