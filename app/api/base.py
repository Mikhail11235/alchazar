from fastapi import APIRouter
from api import route_potion, route_user, route_login


api_router = APIRouter()
api_router.include_router(route_potion.router, prefix="", tags=["potion"])
api_router.include_router(route_user.router, prefix="", tags=["user"])
api_router.include_router(route_login.router, prefix="", tags=["auth"])
