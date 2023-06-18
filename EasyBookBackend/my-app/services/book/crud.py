from services.book import schema
from sqlalchemy.orm.session import Session
from utils.db_model import Reservation, Member, SeatsRecord, BlackList, Restaurant
import datetime
from fastapi import FastAPI, HTTPException
from datetime import datetime, timedelta, date
from typing import List, Dict
from collections import defaultdict


DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"


async def check_blacklist(BID: int, db: Session):
    blacklist = (
        db.query(BlackList)
        .filter(BlackList.BID == BID, BlackList.NonArrive >= 10)
        .all()
    )
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

    # 顯示訂位人姓名、電話
    member_info = [
        {"ID": data[0], "Name": data[1], "Phone": data[2]}
        for data in db.query(Member.ID, Member.Name, Member.Phone)
        .filter(Member.ID == postRequest.ID)
        .all()
    ]

    db.commit()
    return {
        "code": 200,
        "data": {
            "message": "訂位成功",
            "Name": member_info[0]["Name"],
            "Phone": member_info[0]["Phone"],
            "桌號": tno,
        },
    }


async def cancel_reservation(ReNumber: int, db: Session):
    reservation = [
        {"ReNumber": data[0], "ReRID": data[1], "ReTime": data[2], "ReTNo": data[3]}
        for data in db.query(
            Reservation.ReNumber,
            Reservation.ReRID,
            Reservation.ReTime,
            Reservation.ReTNo,
        )
        .filter(Reservation.ReNumber == ReNumber)
        .all()
    ]

    if not reservation:
        raise HTTPException(status_code=400, detail="尚無此訂位！")

    if reservation[0]["ReTime"] < datetime.now():
        raise HTTPException(status_code=400, detail="不能取消訂位")

    db.query(Reservation).filter(
        Reservation.ReNumber == ReNumber,
    ).delete()
    db.commit()

    # 更新座位動態表
    db.query(SeatsRecord).filter(
        SeatsRecord.RID == reservation[0]["ReRID"],
        SeatsRecord.BookTime == reservation[0]["ReTime"],
        SeatsRecord.TNo == reservation[0]["ReTNo"],
    ).update({"Is_Reserved": "F"})
    db.commit()

    return {"code": 200, "data": "取消成功"}


async def get_reservation_info_by_ReNumber(
    updateBookRequest: schema.UpdateBookRequest, db: Session
):
    reservation_info = [
        {
            "ReNumber": data[0],
            "MemberID": data[1],
            "RID": data[2],
            "BookTime": data[3],
            "Reason": data[4],
            "ReTNo": data[5],
            "RePerson": data[6],
        }
        for data in db.query(
            Reservation.ReNumber,
            Reservation.ReMID,
            Reservation.ReRID,
            Reservation.ReTime,
            Reservation.Reason,
            Reservation.ReTNo,
            Reservation.RePerson,
        )
        .filter(Reservation.ReNumber == updateBookRequest.ReNumber)
        .all()
    ]

    if len(reservation_info) > 0:
        return reservation_info[0]
    else:
        return None


async def search_seats(updateBookRequest: schema.UpdateBookRequest, db: Session):
    seats = None

    if updateBookRequest.Person <= 2:
        seats = "2"
    elif 3 <= updateBookRequest.Person <= 4:
        seats = "4"
    elif 5 <= updateBookRequest.Person <= 6:
        seats = "6"
    else:
        raise HTTPException(status_code=400, detail="訂位人數超過可預訂範圍")

    Is_seats = [
        {
            "TNo": data[0],
        }
        for data in db.query(
            SeatsRecord.TNo,
        )
        .filter(
            SeatsRecord.RID == updateBookRequest.RID,
            SeatsRecord.BookTime == updateBookRequest.BookTime,
            SeatsRecord.Seats == seats,
            SeatsRecord.Is_Reserved == "F",
        )
        .all()
    ]

    if Is_seats:
        return Is_seats[0]
    else:
        return None


###更新SeatsRecord Table
async def update_seatsrecord(
    seats_no: str,
    updateBookRequest: schema.UpdateBookRequest,
    reservation_info: list,
    db: Session,
):
    # 更新座位紀錄為已預訂
    db.query(SeatsRecord).filter(
        SeatsRecord.RID == updateBookRequest.RID,
        SeatsRecord.TNo == seats_no,
        SeatsRecord.BookTime == updateBookRequest.BookTime,
        SeatsRecord.Is_Reserved == "F",
    ).update({"Is_Reserved": "Y"})
    db.commit()

    # 更新舊的座位紀錄為改回F
    db.query(SeatsRecord).filter(
        SeatsRecord.RID == reservation_info["RID"],
        SeatsRecord.TNo == reservation_info["ReTNo"],
        SeatsRecord.BookTime == reservation_info["BookTime"],
        SeatsRecord.Is_Reserved == "Y",
    ).update({"Is_Reserved": "F"})
    db.commit()


###更新Reservation Table
async def update_reservation(
    seats_no: str, updateBookRequest: schema.UpdateBookRequest, db: Session
):
    if seats_no:
        db.query(Reservation).filter(
            Reservation.ReNumber == updateBookRequest.ReNumber,
            Reservation.ReMID == updateBookRequest.ID,
            Reservation.ReRID == updateBookRequest.RID,
        ).update(
            {
                "CreateTime": datetime.now(),
                "ReTime": updateBookRequest.BookTime,
                "ReTNo": seats_no,
                "RePerson": updateBookRequest.Person,
                "Reason": updateBookRequest.Reason,
            }
        )
        db.commit()

    else:
        db.query(Reservation).filter(
            Reservation.ReNumber == updateBookRequest.ReNumber,
            Reservation.ReMID == updateBookRequest.ID,
            Reservation.ReRID == updateBookRequest.RID,
        ).update(
            {
                "Reason": updateBookRequest.Reason,
            }
        )
        db.commit()


async def get_reservation_info_by_MemberID(memberid: int, db: Session):
    reservation_list = [
        {
            "ReNumber": data[0],
            "MemberID": data[1],
            "MName": data[2],
            "MPhone": data[3],
            "RID": data[4],
            "RName": data[5],
            "RURL": data[6],
            "ReTime": datetime.strftime(data[7], DATETIME_FORMAT)
            if data[7] is not None
            else data[7],
            "ReTNo": data[8],
            "RePerson": data[9],
            "Reason": data[10],
        }
        for data in db.query(
            Reservation.ReNumber,
            Reservation.ReMID,
            Member.Name,
            Member.Phone,
            Reservation.ReRID,
            Restaurant.RName,
            Restaurant.URL,
            Reservation.ReTime,
            Reservation.ReTNo,
            Reservation.RePerson,
            Reservation.Reason,
        )
        .join(Restaurant, Reservation.ReRID == Restaurant.RID)
        .join(Member, Reservation.ReMID == Member.ID)
        .filter(Reservation.ReMID == memberid)
        .all()
    ]

    if reservation_list:
        return reservation_list
    else:
        return None


async def get_reservation_info_by_RID(RID: int, db: Session):
    reservation_list = [
        {
            "ReNumber": data[0],
            "MemberID": data[1],
            "MName": data[2],
            "MPhone": data[3],
            "RID": data[4],
            "RName": data[5],
            "RURL": data[6],
            "ReTime": datetime.strftime(data[7], DATETIME_FORMAT)
            if data[7] is not None
            else data[7],
            "ReTNo": data[8],
            "RePerson": data[9],
            "Reason": data[10],
        }
        for data in db.query(
            Reservation.ReNumber,
            Reservation.ReMID,
            Member.Name,
            Member.Phone,
            Reservation.ReRID,
            Restaurant.RName,
            Restaurant.URL,
            Reservation.ReTime,
            Reservation.ReTNo,
            Reservation.RePerson,
            Reservation.Reason,
        )
        .join(Restaurant, Reservation.ReRID == Restaurant.RID)
        .join(Member, Reservation.ReMID == Member.ID)
        .filter(Reservation.ReRID == RID)
        .all()
    ]

    if reservation_list:
        return reservation_list
    else:
        return None


async def get_account_info_by_ID(id: int, db: Session):
    member_info = [
        {"ID": data[0]}
        for data in db.query(
            Member.ID,
        )
        .filter(Member.ID == id)
        .all()
    ]

    if len(member_info) > 0:
        return member_info[0]
    else:
        return None


async def get_restaurant_info_by_ID(RID: int, db: Session):
    restaurant_info = [
        {"RID": data[0]}
        for data in db.query(
            Restaurant.RID,
        )
        .filter(Restaurant.RID == RID)
        .all()
    ]

    if len(restaurant_info) > 0:
        return restaurant_info[0]
    else:
        return None


def check_seats_availability(RID: int, Date: date, Person: int, db: Session):
    start_time = datetime.combine(Date, datetime.min.time())
    end_time = start_time + timedelta(days=1)

    seats = None

    if Person <= 2:
        seats = "2"
    elif 3 <= Person <= 4:
        seats = "4"
    elif 5 <= Person <= 6:
        seats = "6"

    seats_records = (
        db.query(SeatsRecord.BookTime, SeatsRecord.Is_Reserved)
        .filter(
            SeatsRecord.RID == RID,
            SeatsRecord.BookTime >= start_time,
            SeatsRecord.BookTime < end_time,
            SeatsRecord.Seats == seats,
        )
        .all()
    )

    availability = []
    time_slots = defaultdict(lambda: {"time_slot": None, "available": False})

    for record in seats_records:
        time_slot = record.BookTime.strftime("%H:%M")

        if record.Is_Reserved == "F":
            time_slots[time_slot]["available"] = True

        time_slots[time_slot]["time_slot"] = time_slot

    availability = list(time_slots.values())

    return availability
