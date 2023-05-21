from utils.db_model import Member
from sqlalchemy.orm.session import Session
from services.member import schema
import datetime


async def get_account_info_by_phone(phone: str, db: Session):
    member_info = [
        {
            "ID": data[0],
            "Phone": data[1],
        }
        for data in db.query(Member.ID, Member.Phone)
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
            Password=hash_pwd,
            MLevel=1,
            MPoints=0,
            AccumSpend=0,
        )
    )
    db.commit()
