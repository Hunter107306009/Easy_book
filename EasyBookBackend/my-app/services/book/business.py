from services.book import crud, schema
from sqlalchemy.orm.session import Session
from utils.response import Response


async def book(bookRequest: schema.BookRequest, db: Session):
    if await crud.check_reservation_exists(bookRequest.ID,bookRequest.RID,bookRequest.ReTime, db):
       return Response.Error(msg="不可重複訂位！")
    elif await crud.check_blacklist(bookRequest.ID,db):
        return Response.Error(msg="您為黑名單不可訂位！")
    else:
        reservation_data = await crud.book_reservation(bookRequest, db)
        return Response.Success(data=reservation_data)
    
