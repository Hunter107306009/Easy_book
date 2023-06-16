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
