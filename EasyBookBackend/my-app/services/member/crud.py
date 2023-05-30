from utils.db_model import Member
from sqlalchemy.orm.session import Session
from services.member import schema
import datetime


async def get_account_info_for_login_signup(phone: str, db: Session):
    member_info = [
        {
            "ID": data[0],
            "Name": data[1],
            "Phone": data[2],
            "Pwd": data[3],
        }
        for data in db.query(
            Member.ID,
            Member.Name,
            Member.Phone,
            Member.Pwd,
        )
        .filter(Member.Phone == phone)
        .all()
    ]

    if len(member_info) > 0:
        return member_info[0]
    else:
        return None


async def get_account_info_by_ID(id: int, db: Session):
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
        .filter(Member.ID == id)
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


async def update_member(
    hash_pwd, updateMemberRequest: schema.UpdateMemberRequest, db: Session
):
    db.query(Member).filter(Member.ID == updateMemberRequest.ID).update(
        {
            "Name": updateMemberRequest.name,
            "Pwd": hash_pwd,
            "Gender": updateMemberRequest.gender,
            "Birthday": updateMemberRequest.birthday,
        }
    )
    db.commit()
