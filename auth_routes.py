from fastapi import APIRouter
from models import User, db
from sqlalchemy.orm import sessionmaker

auth_router = APIRouter(prefix="/auth",tags=["auth"])

@auth_router.get("/") # http://127.0.0.1:8000/auth/
async def index():
    return { "message": "Auth router begins here"}

@auth_router.post("/register")
async def register(name: str, email: str, password: str):
    # Abrir uma sessão
    Session = sessionmaker(bind=db)
    session = Session()

    # Saber se já tenho na tabela de utilizadores um utilizador
    # com este email
    user = session.query(User).filter(User.email==email).first()

    if user: # Se já existe o utilizador
        return { "message": "An user with this email address already exists"}
    else:
        new_user  = User(name,email,password)
        session.add(new_user)
        session.commit()
        return { "message": "User registered with success" }