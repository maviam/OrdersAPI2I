from fastapi import APIRouter

orders_router = APIRouter(prefix="/orders",tags=["orders"])

@orders_router.get("/") # http://127.0.0.1:8000/orders/
async def index():
    return { "message": "Orders router begins here"}