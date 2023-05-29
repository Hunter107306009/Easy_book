from services.member import crud, schema
from sqlalchemy.orm.session import Session
from utils.response import Response
from utils.basic import sha_256


async def create_member(createMemberRequest: schema.CreateMemberRequest, db: Session):
    member_info = await crud.get_account_info_by_phone(createMemberRequest.phone, db)

    if not member_info:
        hash_pwd = sha_256(createMemberRequest.pwd)
        await crud.create_member(hash_pwd, createMemberRequest, db)
        return Response.Success(data=None)
    else:
        return Response.Error(msg="此信箱已註冊過，請直接登入，謝謝")


async def login(phone: str, pwd: str, db: Session):
    # 查詢是否有此phone的會員資料
    account_info = await crud.get_account_info_by_phone(phone, db)
    hash_pwd = sha_256(pwd)

    if account_info:
        if hash_pwd != account_info["Pwd"]:
            return Response.Error(msg="密碼錯誤，請重新輸入")

        else:
            account_info_return = {
                "ID": account_info["ID"],
                "Name": account_info["Name"],
                "Phone": account_info["Phone"],
            }
            return Response.Success(data=account_info_return)
    else:
        return Response.Error(msg="手機號碼尚未註冊，請先註冊唷！")
