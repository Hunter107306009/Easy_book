from utils.db_model import Member
from sqlalchemy.orm.session import Session
from services.member import schema
import datetime


async def get_account_info_by_phone(phone: str, db: Session):
    member_info = [
        {
            "ID": data[0],
            "Name": data[1],
            "Phone": data[2],
            "Pwd": data[3],
            "Gender": data[4],
            "Birthday": data[5],
            "MLevel": data[6],
            "MPoints": data[7],
            "AccumSpend": data[8],
        }
        for data in db.query(
            Member.ID,
            Member.Name,
            Member.Phone,
            Member.Pwd,
            Member.Gender,
            Member.Birthday,
            Member.MLevel,
            Member.MPoints,
            Member.AccumSpend,
        )
        .filter(Member.Phone == phone)
        .all()
    ]

    if len(member_info) > 0:
        return member_info[0]
    else:
        return None


async def create_member(hash_pwd, postRequest: schema.CreateMemberRequest, db: Session):
    db.add(
        Member(
            Name=postRequest.name,
            Phone=postRequest.phone,
            Pwd=hash_pwd,
            Gender=postRequest.gender,
            Birthday=postRequest.birthday,
            MLevel=1,
            MPoints=0,
            AccumSpend=0,
        )
    )
    db.commit()
