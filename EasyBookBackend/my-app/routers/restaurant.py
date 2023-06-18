from fastapi import APIRouter
from sqlalchemy.orm.session import Session
from fastapi.params import Depends
from utils.db_conn import get_db
from services.restaurant import business, schema

router = APIRouter(prefix="/restaurant", tags=["restaurant"])


@router.post("/create_restaurant", summary="餐廳註冊")
async def create_restaurant(
    createRestaurantRequest: schema.CreateRestaurantRequest,
    db: Session = Depends(get_db),
):
    return await business.create_restaurant(createRestaurantRequest, db)


@router.post("/restaurant_login", summary="餐廳登入")
async def restaurant_login(
    restaurantLoginRequest: schema.RestaurantLoginRequest, db: Session = Depends(get_db)
):
    return await business.restaurant_login(restaurantLoginRequest, db)


#################
@router.get("/restaurant_list", summary="餐廳列表")
async def get_restaurant_list(db: Session = Depends(get_db)):
    return await business.get_restaurant_list(db)


@router.get("/restaurant_info", summary="餐廳資訊")
async def get_restaurant_info(restaurant_id: int, db: Session = Depends(get_db)):
    return await business.get_restaurant_info(restaurant_id, db)

@router.get("/search_restaurant", summary="搜尋特定餐廳")
async def get_search_restaurant(restaurant_name: str, db: Session = Depends(get_db)):
    return await business.get_search_restaurant(restaurant_name, db)


@router.patch("/update_restaurant_info", summary="餐廳資訊修改")
async def update_restaurant_info(
    UpdateRestaurantRequest: schema.UpdateRestaurantRequest,
    db: Session = Depends(get_db),
):
    return await business.update_restaurant_info(UpdateRestaurantRequest, db)


@router.get("/blacklist_list", summary="黑名單列表")
async def get_blacklist_list(db: Session = Depends(get_db)):
    return await business.get_blacklist_list(db)


@router.post("/add_to_blacklist", summary="新增黑名單")
async def add_to_blacklist(
    AddToBlacklistRequest: schema.AddToBlacklistRequest, db: Session = Depends(get_db)
):
    return await business.add_to_blacklist(AddToBlacklistRequest, db)


@router.post("/add_consumption_record", summary="新增會員消費紀錄")
async def add_consumption_record(
    AddConsumptionRecordRequest: schema.AddConsumptionRecordRequest,
    db: Session = Depends(get_db),
):
    return await business.add_consumption_record(AddConsumptionRecordRequest, db)
