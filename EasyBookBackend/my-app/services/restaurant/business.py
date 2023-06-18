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
        hash_pwd = sha_256(createRestaurantRequest.Rpwd)
        await crud.create_restaurant(hash_pwd, createRestaurantRequest, db)

        account_info = await crud.get_account_info_by_account(
            createRestaurantRequest.RAccount, db
        )
        await crud.create_restaurant_seats(account_info["RID"], db)
        await crud.create_restaurant_seats_record(account_info["RID"], db)

        return Response.Success(data=None)


async def restaurant_login(
    restaurantLoginRequest: schema.RestaurantLoginRequest, db: Session
):
    restaurant_info = await crud.get_account_info_by_account(
        restaurantLoginRequest.RAccount, db
    )

    reutrn_restaurant_info = {
        "RID": restaurant_info["RID"],
        "Account": restaurant_info["RAccount"],
        "Name": restaurant_info["RName"],
        "Phone": restaurant_info["RPhone"],
        "Address": restaurant_info["RAddress"],
        "URL": restaurant_info["URL"],
    }

    if restaurant_info:
        if restaurant_info["RPwd"] == sha_256(restaurantLoginRequest.Rpwd):
            return Response.Success(data=reutrn_restaurant_info)
        else:
            return Response.Error(msg="密碼錯誤，請重新輸入。")
    else:
        return Response.Error(msg="此帳號尚未註冊，請重新確認或前往註冊。")


#################
# 取得餐廳資訊
async def get_restaurant_info(restaurant_id: int, db: Session):
    restaurant_info = await crud.get_restaurant_info(restaurant_id, db)

    if not restaurant_info:
        return Response.Error(msg="查無此餐廳資訊，可能已遭刪除。")
    else:
        return Response.Success(data=restaurant_info)


# 取得特定餐廳資訊
async def get_search_restaurant(restaurant_name: str, db: Session):
    search_restaurant = await crud.get_search_restaurant(restaurant_name, db)

    if not search_restaurant:
        return Response.Error(msg="查無此餐廳資訊，可能已遭刪除。")
    else:
        return Response.Success(data=search_restaurant)


# 更改餐廳資訊
async def update_restaurant_info(
    UpdateRestaurantRequest: schema.UpdateRestaurantRequest, db: Session
):
    update_restaurant_info = await crud.get_account_info_by_RID(
        UpdateRestaurantRequest.RID, db
    )
    hash_pwd = sha_256(UpdateRestaurantRequest.RPwd)

    if update_restaurant_info:
        await crud.update_restaurant_info(hash_pwd, UpdateRestaurantRequest, db)
        return Response.Success(data=None)
    else:
        return Response.Error(msg="更新失敗，查無此帳號資訊，請與相關人員聯絡～謝謝")


# 取得餐廳列表
async def get_restaurant_list(db: Session):
    restaurant_list = await crud.get_restaurant_list(db)
    if not restaurant_list:
        return Response.Error(msg="尚無餐廳。")
    else:
        return Response.Success(data=restaurant_list)


# 取得黑名單列表
async def get_blacklist_list(db: Session):
    black_list = await crud.get_blacklist_list(db)
    if not black_list:
        return Response.Error(msg="查無此黑名單列表，可能已遭刪除。")

    return Response.Success(data=black_list)


# 新增黑名單
async def add_to_blacklist(
    AddToBlacklistRequest: schema.AddToBlacklistRequest, db: Session
):
    black_info = await crud.get_member_info_by_phone(AddToBlacklistRequest.Phone, db)

    if black_info:
        Is_blacklist = await crud.is_in_blacklist(black_info["ID"], db)

        if Is_blacklist:
            await crud.update_to_blacklist(Is_blacklist, db)
            return Response.Success(data=None)
        else:
            await crud.add_to_blacklist(black_info["ID"], db)
            return Response.Success(data=None)
    else:
        return Response.Error(msg="查無此會員資訊")


# 新增會員消費紀錄
async def add_consumption_record(
    AddConsumptionRecordRequest: schema.AddConsumptionRecordRequest, db: Session
):
    Is_member = await crud.get_member_info_by_phone(
        AddConsumptionRecordRequest.Phone, db
    )

    Is_restaurant = await crud.get_restaurant_info(AddConsumptionRecordRequest.RID, db)

    if Is_member and Is_restaurant:
        points_info = await crud.add_consumption_record(
            Is_member["ID"], AddConsumptionRecordRequest, db
        )

        member_level_info = await crud.get_member_info_by_id(Is_member["ID"], db)

        await crud.update_member_points(member_level_info, points_info, db)

        return Response.Success(data=None)
    elif not Is_member:
        return Response.Error(msg="查無此會員資訊")
    elif not Is_restaurant:
        return Response.Error(msg="查無此餐廳資訊")
