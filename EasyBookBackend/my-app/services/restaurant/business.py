from services.restaurant import crud, schema
from sqlalchemy.orm.session import Session
from utils.response import Response
from utils.basic import sha_256


async def create_restaurant(
    createRestaurantRequest: schema.CreateRestaurantRequest, db: Session
):
    account_info = await crud.get_account_info_by_account(
        createRestaurantRequest.RAccount, db
    )

    if account_info:
        return Response.Error(msg="該帳號已被註冊過，請換一個帳號！")
    else:
        await crud.create_restaurant(createRestaurantRequest, db)

        account_info = await crud.get_account_info_by_account(
            createRestaurantRequest.RAccount, db
        )
        await crud.create_restaurant_seats(account_info["RID"], db)
        await crud.create_restaurant_seats_record(account_info["RID"], db)

        return Response.Success(data=None)
