from fastapi import FastAPI

app = FastAPI()

from auth_routes import auth_router
from order_routes import orders_router

# Rotas
app.include_router(auth_router) # http://127.0.0.1:8000/auth
app.include_router(orders_router) # http://127.0.0.1:8000/orders