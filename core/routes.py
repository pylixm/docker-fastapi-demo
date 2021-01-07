from fastapi import APIRouter
from service import views
from api import views as api_views

# 页面路由
page_routes = APIRouter()
page_routes.include_router(views.router, prefix="")

# api 相关路由
api_routes = APIRouter()
api_routes.include_router(api_views.router, prefix='/v1')
