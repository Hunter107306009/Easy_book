from services.book import crud, schema
from sqlalchemy.orm.session import Session
from utils.response import Response
from datetime import date


async def book(bookRequest: schema.BookRequest, db: Session):
    if await crud.check_reservation_exists(
        bookRequest.ID, bookRequest.RID, bookRequest.ReTime, db
    ):
        return Response.Error(msg="不可重複訂位！")
    elif await crud.check_blacklist(bookRequest.ID, db):
        return Response.Error(msg="您為黑名單不可訂位！")
    else:
        reservation_data = await crud.book_reservation(bookRequest, db)
        return Response.Success(data=reservation_data)


async def cancel_book(ReNumber: int, db: Session):
    cancel_data = await crud.cancel_reservation(ReNumber, db)
    return Response.Success(data=cancel_data)


async def update_book(updateBookRequest: schema.UpdateBookRequest, db: Session):
    reservation_info = await crud.get_reservation_info_by_ReNumber(
        updateBookRequest, db
    )

    if not reservation_info:
        return Response.Error(msg="查無此訂位記錄，請與店家聯繫～謝謝")
    else:
        if (
            reservation_info["ReNumber"] == updateBookRequest.ReNumber
            and reservation_info["MemberID"] == updateBookRequest.ID
            and reservation_info["RID"] == updateBookRequest.RID
        ):
            if (
                updateBookRequest.BookTime != reservation_info["BookTime"]
                or updateBookRequest.Person != reservation_info["RePerson"]
            ):
                # 先查詢該時段有無座位
                Is_seats = await crud.search_seats(updateBookRequest, db)
                # 新時段有位子，開始update
                if Is_seats:
                    ###update SeatsRecord table - 原本變為F，新的訂位變為Y
                    await crud.update_seatsrecord(
                        Is_seats["TNo"], updateBookRequest, reservation_info, db
                    )
                    ###更新reservation table
                    await crud.update_reservation(
                        Is_seats["TNo"], updateBookRequest, db
                    )
                    return Response.Success(data=None)
                else:
                    return Response.Error(msg="該時段該人數訂位已滿")
            # 只更改用餐原因
            else:
                await crud.update_reservation(None, updateBookRequest, db)
        else:
            return Response.Error(msg="有該筆訂位記錄，但是記錄有誤，請前端確認代的值是否正確。")

        return Response.Success(data=None)


async def query_book_member(MemberID: int, db: Session):
    Is_member = await crud.get_account_info_by_ID(MemberID, db)

    if Is_member:
        reservation_info = await crud.get_reservation_info_by_MemberID(MemberID, db)

        if reservation_info:
            return Response.Success(data=reservation_info)
        else:
            return Response.Success(data=[])
    else:
        return Response.Error(msg="查無此會員資訊")


async def query_book_restaurant(RID: int, db: Session):
    Is_restaurant = await crud.get_restaurant_info_by_ID(RID, db)

    if Is_restaurant:
        reservation_info = await crud.get_reservation_info_by_RID(RID, db)

        if reservation_info:
            return Response.Success(data=reservation_info)
        else:
            return Response.Success(data=[])
    else:
        return Response.Error(msg="查無此餐廳資訊")
 
async def check_seats(request: schema.CheckSeatsRequest, db: Session):
    check_seats_info = crud.check_seats_availability(request.RID, request.BookTime, request.Person,db)
    return Response.Success(data=check_seats_info)
