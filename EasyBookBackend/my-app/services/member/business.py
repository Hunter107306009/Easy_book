from services.member import crud, schema
from sqlalchemy.orm.session import Session
from utils.response import Response
from utils.basic import sha_256


async def create_member(createMemberRequest: schema.CreateMemberRequest, db: Session):
    member_info = await crud.get_account_info_for_login_signup(
        createMemberRequest.phone, db
    )

    if not member_info:
        hash_pwd = sha_256(createMemberRequest.pwd)
        await crud.create_member(hash_pwd, createMemberRequest, db)
        return Response.Success(data=None)
    else:
        return Response.Error(msg="此手機號碼已註冊過，請直接登入，謝謝")


async def login(loginRequest: schema.LoginRequest, db: Session):
    # 查詢是否有此phone的會員資料
    account_info = await crud.get_account_info_for_login_signup(loginRequest.phone, db)
    hash_pwd = sha_256(loginRequest.pwd)

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


async def get_member_info(id: int, db: Session):
    member_info = await crud.get_account_info_by_ID(id, db)

    if member_info:
        return Response.Success(data=member_info)
    else:
        return Response.Error(msg="查無此帳號資訊，請與相關人員聯絡～謝謝")


async def update_member(updateMemberRequest: schema.UpdateMemberRequest, db: Session):
    member_info = await crud.get_account_info_by_ID(updateMemberRequest.ID, db)
    hash_pwd = sha_256(updateMemberRequest.pwd)

    if member_info:
        await crud.update_member(hash_pwd, updateMemberRequest, db)
        return Response.Success(data=None)
    else:
        return Response.Error(msg="更新失敗，查無此帳號資訊，請與相關人員聯絡～謝謝")


async def get_member_paypoints_info(id: int, db: Session):
    member_info = await crud.get_account_info_by_ID(id, db)

    if not member_info:
        return Response.Error(msg="尚未註冊或查無此帳號資訊，請與相關人員聯絡～謝謝")

    consumption_info = await crud.get_consumption_info_by_ID(id, db)
    member_list = {
        "MLevel": member_info["MLevel"],
        "MPoints": member_info["MPoints"],
        "MAccumSpend": member_info["MAccumSpend"],
        "Points_list": consumption_info,
    }

    return Response.Success(data=member_list)
