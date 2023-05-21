from services.member import crud, schema
from sqlalchemy.orm.session import Session
from utils.response import Response
from utils.basic import sha_256


async def create_member(createMemberRequest: schema.CreateMemberRequest, db: Session):
    member_info = await crud.get_account_info_by_phone(createMemberRequest.phone, db)

    if not member_info:
        # hash_pwd = sha_256(createMemberRequest.pwd)
        # await crud.create_member(uuid_code, hash_pwd, createMemberRequest, db)
        await crud.create_member(createMemberRequest, db)
        return Response.Success(data=None)
    else:
        return Response.Error(msg="此信箱已註冊過，請直接登入，謝謝")
