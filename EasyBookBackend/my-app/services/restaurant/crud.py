from utils.db_model import (
    Member,
    Seats,
    Restaurant,
    Reservation,
    SeatsRecord,
    Consumptions,
    BlackList,
)
from sqlalchemy.orm.session import Session
from services.restaurant import schema
import datetime
import calendar
from dateutil.relativedelta import relativedelta

DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"


async def get_account_info_by_account(account: str, db: Session):
    account_info = [
        {
            "RID": data[0],
            "RAccount": data[1],
            "RPwd": data[2],
            "RName": data[3],
            "RPhone": data[4],
            "RAddress": data[5],
            "URL": data[6],
        }
        for data in db.query(
            Restaurant.RID,
            Restaurant.RAccount,
            Restaurant.RPwd,
            Restaurant.RName,
            Restaurant.RPhone,
            Restaurant.RAddress,
            Restaurant.URL,
        )
        .filter(Restaurant.RAccount == account)
        .all()
    ]

    if len(account_info) > 0:
        return account_info[0]
    else:
        return None


async def get_account_info_by_RID(RID: str, db: Session):
    account_info = [
        {
            "RID": data[0],
            "RName": data[1],
            "RPhone": data[2],
            "RAddress": data[3],
            "URL": data[4],
        }
        for data in db.query(
            Restaurant.RID,
            Restaurant.RName,
            Restaurant.RPhone,
            Restaurant.RAddress,
            Restaurant.URL,
        )
        .filter(Restaurant.RID == RID)
        .all()
    ]

    if len(account_info) > 0:
        return account_info[0]
    else:
        return None


async def create_restaurant(
    hash_pwd: str, createRestaurantRequest: schema.CreateRestaurantRequest, db: Session
):
    db.add(
        Restaurant(
            RAccount=createRestaurantRequest.RAccount,
            RPwd=hash_pwd,
            RName=createRestaurantRequest.RName,
            RPhone=createRestaurantRequest.RPhone,
            RAddress=createRestaurantRequest.RAddress,
            URL=createRestaurantRequest.Url,
        )
    )
    db.commit()


async def create_restaurant_seats(RID: int, db: Session):
    seats_list = [
        {"TNo": "A1", "Seats": 2},
        {"TNo": "A2", "Seats": 2},
        {"TNo": "B1", "Seats": 4},
        {"TNo": "B2", "Seats": 4},
        {"TNo": "C1", "Seats": 6},
        {"TNo": "C2", "Seats": 6},
    ]

    for each in seats_list:
        db.add(
            Seats(
                RID=RID,
                Seats=each["Seats"],
                TNo=each["TNo"],
            )
        )

        db.commit()


async def create_restaurant_seats_record(RID: int, db: Session):
    ###Create Datetime - 建立這個月剩餘的日期＆下個月整個月的日期
    time_list = [
        "11:00:00",
        "12:00:00",
        "13:00:00",
        "17:00:00",
        "18:00:00",
        "19:00:00",
        "20:00:00",
    ]

    next_month_first_date = (datetime.date.today() + relativedelta(months=1)).replace(
        day=1
    )

    next_day_count = calendar.monthrange(
        next_month_first_date.year, next_month_first_date.month
    )[1]

    this_month_first_date = (
        # datetime.date.today() + relativedelta(months=1)
        datetime.date.today()
    ).replace(day=datetime.date.today().day)

    this_day_count = calendar.monthrange(
        this_month_first_date.year,
        this_month_first_date.month,
    )[1]

    total_day = this_day_count - datetime.date.today().day + next_day_count

    date_list = [
        (this_month_first_date + relativedelta(days=i)).strftime("%Y-%m-%d")
        for i in range(total_day)
    ]

    date_time_list = []
    for date in date_list:
        for time in time_list:
            date_time_list.append(f"{date} {time}")

    ###Get Seats Data
    seats_info = [
        {"RID": data[0], "TNo": data[1], "Seats": data[2]}
        for data in db.query(Seats.RID, Seats.TNo, Seats.Seats)
        .filter(Seats.RID == RID)
        .all()
    ]

    ###Join Seats & Time
    final_table = []

    for seats in seats_info:
        for times in date_time_list:
            new_dict = {
                "RID": seats["RID"],
                "TNo": seats["TNo"],
                "Seats": seats["Seats"],
                "BookTime": times,
            }
            final_table.append(new_dict)

    ### Insert Data to DB
    for each in final_table:
        db.add(
            SeatsRecord(
                RID=each["RID"],
                Seats=each["Seats"],
                TNo=each["TNo"],
                BookTime=each["BookTime"],
                Is_Reserved="F",
            )
        )

        db.commit()


##################
async def get_restaurant_info(restaurant_id: int, db: Session):
    restaurant_info = [
        {
            "RID": data[0],
            "RName": data[1],
            "RPhone": data[2],
            "RAddress": data[3],
            "URL": data[4],
        }
        for data in db.query(
            Restaurant.RID,
            Restaurant.RName,
            Restaurant.RPhone,
            Restaurant.RAddress,
            Restaurant.URL,
        )
        .filter(restaurant_id == Restaurant.RID)
        .all()
    ]

    return restaurant_info


async def get_search_restaurant(restaurant_name: str, db: Session):
    restaurant_name = [
        {
            "RID": data[0],
            "RName": data[1],
            "RPhone": data[2],
            "RAddress": data[3],
            "URL": data[4],
        }
        for data in db.query(
            Restaurant.RID,
            Restaurant.RName,
            Restaurant.RPhone,
            Restaurant.RAddress,
            Restaurant.URL,
        )
        .filter(restaurant_name == Restaurant.RName)
        .all()
    ]

    return restaurant_name


async def get_restaurant_list(db: Session):
    restaurant_list = [
        {"RID": data[0], "RName": data[1], "RAddress": data[2], "URL": data[3]}
        for data in db.query(
            Restaurant.RID, Restaurant.RName, Restaurant.RAddress, Restaurant.URL
        ).all()
    ]

    return restaurant_list


async def update_restaurant_info(
    hash_pwd, UpdateRestaurantRequest: schema.UpdateRestaurantRequest, db: Session
):
    db.query(Restaurant).filter(
        Restaurant.RID == UpdateRestaurantRequest.RID,
    ).update(
        {
            "RPwd": hash_pwd,
            "RName": UpdateRestaurantRequest.RName,
            "RPhone": UpdateRestaurantRequest.RPhone,
            "RAddress": UpdateRestaurantRequest.RAddress,
            "URL": UpdateRestaurantRequest.URL,
        }
    )
    db.commit()


async def get_blacklist_list(db: Session):
    blacklist = [
        {"BID": data[0], "Name": data[1], "Phone": data[2], "NonArrive": data[3]}
        for data in db.query(
            BlackList.BID, Member.Name, Member.Phone, BlackList.NonArrive
        )
        .filter(BlackList.BID == Member.ID)
        .all()
    ]
    if blacklist:
        return blacklist
    else:
        return []


async def is_in_blacklist(id: int, db: Session):
    blacklist = [
        {"BID": data[0], "NonArrive": data[1]}
        for data in db.query(BlackList.BID, BlackList.NonArrive)
        .filter(BlackList.BID == id)
        .all()
    ]
    if blacklist:
        return blacklist
    else:
        return None


async def add_to_blacklist(id: int, db: Session):
    db.add(BlackList(BID=id, NonArrive=1))
    db.commit()


async def update_to_blacklist(blacklist: list, db: Session):
    db.query(BlackList).filter(
        BlackList.BID == blacklist[0]["BID"],
    ).update({"NonArrive": blacklist[0]["NonArrive"] + 1})
    db.commit()


async def add_consumption_record(
    memberID: int,
    AddConsumptionRecordRequest: schema.AddConsumptionRecordRequest,
    db: Session,
):
    db.add(
        Consumptions(
            CMID=memberID,
            CRID=AddConsumptionRecordRequest.RID,
            Consumptions=AddConsumptionRecordRequest.Consumptions,
            CTime=datetime.datetime.now(),
            PointsChange=AddConsumptionRecordRequest.Consumptions // 100,
        )
    )
    db.commit()

    points_info = {
        "ID": memberID,
        "Consumptions": AddConsumptionRecordRequest.Consumptions,
        "PointsChange": AddConsumptionRecordRequest.Consumptions // 100,
    }
    return points_info


async def get_member_info_by_id(id: int, db: Session):
    member_info = [
        {"ID": data[0], "MLevel": data[1], "MPoints": data[2], "MAccumSpend": data[3]}
        for data in db.query(
            Member.ID, Member.MLevel, Member.MPoints, Member.MAccumSpend
        )
        .filter(Member.ID == id)
        .all()
    ]

    return member_info[0]


async def update_member_points(member_level_info: dict, points_info: dict, db: Session):
    db.query(Member).filter(
        Member.ID == points_info["ID"],
    ).update(
        {
            "MAccumSpend": member_level_info["MAccumSpend"]
            + points_info["Consumptions"],
            "MPoints": member_level_info["MPoints"] + points_info["PointsChange"],
        }
    )
    db.commit()


async def get_member_info_by_phone(phone: str, db: Session):
    member_info = [
        {
            "ID": data[0],
        }
        for data in db.query(Member.ID).filter(Member.Phone == phone).all()
    ]

    if len(member_info) > 0:
        return member_info[0]
    else:
        return None
