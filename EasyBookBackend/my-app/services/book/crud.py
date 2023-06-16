from services.book import schema
from sqlalchemy.orm.session import Session
from utils.db_model import Reservation,Seats,SeatsRecord,BlackList
import datetime
from fastapi import FastAPI, HTTPException
from datetime import datetime


async def check_blacklist(BID: int, db: Session):
    blacklist = db.query(BlackList).get(BID)
    if blacklist:
        return True
    else:
        return False


async def check_reservation_exists(ID:int,RID: int, ReTime: datetime.time, db: Session):

    existing_reservation = db.query(Reservation).filter(
        Reservation.ReMID == ID,
        Reservation.ReRID == RID,
        Reservation.ReTime == ReTime
    ).first()

    if existing_reservation:
        return True
    else:
        return False


async def book_reservation(postRequest: schema.BookRequest, db = Session):
    seats = None 
  
    if postRequest.Person <= 2:
        seats = "2"
    elif 3<= postRequest.Person <= 4:
        seats = "4"
    elif 5<= postRequest.Person <= 6:
        seats = "6"
    else:
        raise HTTPException(status_code=400, detail="訂位人數超過可預訂範圍")

    
    available_tables = db.query(SeatsRecord.TNo).filter(
        SeatsRecord.RID == postRequest.RID,
        SeatsRecord.Seats == seats,
        SeatsRecord.BookTime == postRequest.ReTime,
        SeatsRecord.Is_Reserved == "F"
    ).all()
    

    if not available_tables:
        raise HTTPException(status_code=200, detail={
             "code": 200,
             "message": "error",
            "data": {
                "data": "暫無座位可預訂" }})


    tno = available_tables[0].TNo
    
    # 建立訂位紀錄
    reservation = Reservation(
        ReRID=postRequest.RID,
        ReMID=postRequest.ID, 
        Reason=postRequest.Reason,
        CreateTime=datetime.now(),
        ReTime=postRequest.ReTime,
        ReTNo=tno,
        RePerson=postRequest.Person
    )

   
    db.add(reservation)

    
    # 更新座位紀錄為已預訂
    seats_record = db.query(SeatsRecord).filter_by(
    RID=postRequest.RID,
    Seats=str(postRequest.Person),
    TNo=tno,
    BookTime=postRequest.ReTime,
    Is_Reserved="F"
    ).first()

    if seats_record:
        seats_record.Is_Reserved = "Y"
    else:
        raise HTTPException(status_code=500, detail="Failed to update SeatsRecord")

    db.commit()
    return {
        "code": 200,
        "message": "Success",
        "data": {
            "data": "訂位成功",
            "numbers":  tno
        }
    }
