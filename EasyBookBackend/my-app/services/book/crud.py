from services.book import schema
from sqlalchemy.orm.session import Session
from utils.db_model import Reservation, Seats, SeatsRecord, BlackList
import datetime
from fastapi import FastAPI, HTTPException
from datetime import datetime


async def check_blacklist(BID: int, db: Session):
    blacklist = db.query(BlackList).get(BID)
    if blacklist:
        return True
    else:
        return False


async def check_reservation_exists(
    ID: int, RID: int, ReTime: datetime.time, db: Session
):
    existing_reservation = (
        db.query(Reservation)
        .filter(
            Reservation.ReMID == ID,
            Reservation.ReRID == RID,
            Reservation.ReTime == ReTime,
        )
        .first()
    )

    if existing_reservation:
        return True
    else:
        return False


async def book_reservation(postRequest: schema.BookRequest, db=Session):
    seats = None

    if postRequest.Person <= 2:
        seats = "2"
    elif 3 <= postRequest.Person <= 4:
        seats = "4"
    elif 5 <= postRequest.Person <= 6:
        seats = "6"
    else:
        raise HTTPException(status_code=400, detail="訂位人數超過可預訂範圍")

    available_tables = (
        db.query(SeatsRecord.TNo)
        .filter(
            SeatsRecord.RID == postRequest.RID,
            SeatsRecord.Seats == seats,
            SeatsRecord.BookTime == postRequest.ReTime,
            SeatsRecord.Is_Reserved == "F",
        )
        .all()
    )

    if not available_tables:
        raise HTTPException(
            status_code=200,
            detail={"code": 200, "message": "error", "data": {"data": "暫無座位可預訂"}},
        )

    tno = available_tables[0].TNo

    # 建立訂位紀錄
    reservation = Reservation(
        ReRID=postRequest.RID,
        ReMID=postRequest.ID,
        Reason=postRequest.Reason,
        CreateTime=datetime.now(),
        ReTime=postRequest.ReTime,
        ReTNo=tno,
        RePerson=postRequest.Person,
    )

    db.add(reservation)

    # 更新座位紀錄為已預訂
    db.query(SeatsRecord).filter(
        SeatsRecord.RID == postRequest.RID,
        SeatsRecord.Seats == seats,
        SeatsRecord.TNo == tno,
        SeatsRecord.BookTime == postRequest.ReTime,
        SeatsRecord.Is_Reserved == "F",
    ).update({"Is_Reserved": "Y"})

    db.commit()
    return {"code": 200, "data": {"data": "訂位成功", "桌號": tno}}


async def cancel_reservation(cancel_request: schema.CancelRequest, db: Session):
    reservation = (
        db.query(Reservation)
        .filter(
            Reservation.ReRID == cancel_request.RID,
            Reservation.ReMID == cancel_request.ID,
            Reservation.ReNumber == cancel_request.ReNumber,
        )
        .first()
    )

    if not reservation:
        raise HTTPException(status_code=400, detail="尚無此訂位！")

    current_date = datetime.now().date()

    if reservation.ReTime.date() < current_date:
        raise HTTPException(status_code=200, detail="不能取消訂位")

    db.delete(reservation)
    db.commit()

    # 更新座位動態表
    db.query(SeatsRecord).filter(
        SeatsRecord.RID == cancel_request.RID,
        SeatsRecord.BookTime == cancel_request.BookTime,
        SeatsRecord.TNo == cancel_request.CTNo,
    ).update({"Is_Reserved": "F"})
    db.commit()

    return {"code": 200, "data": "取消成功"}
