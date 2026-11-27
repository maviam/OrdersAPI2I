from sqlalchemy import create_engine, Column, String, Integer, Float, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()
db = create_engine("sqlite:///pizzaria.db")

class User(Base):
    __tablename__ = "users"
    id = Column("id",primary_key=True,autoincrement=True)
    name = Column("name",String,nullable=False)
    email = Column("email",String,nullable=False)
    password = Column("pass",String,nullable=False)
    active = Column("active",Boolean)
    admin = Column("admin",Boolean,default=False)

    def __init__(self,name,email,password,active=True,admin=False):
        self.name = name
        self.email = email
        self.password = password
        self.active = active
        self.admin = admin

# Class Order (id,user,status,price) - Class ItemOrder (id, order, name, flavour, size, quantity)
class Order(Base):
    __tablename__ = "orders"
    id = Column("id",primary_key=True,autoincrement=True)
    user = Column("user",ForeignKey("users.id"))
    status = Column("status",String,nullable=False)
    price = Column("price",Float)
    # items = 

    def __init__(self,user,status="pending",price=0):
        self.user = user
        self.status = status
        self.price = price

class OrderItems(Base):
    __tablename__ = "orders_items"
    id = Column("id",primary_key=True,autoincrement=True)
    quantity = Column("quantity",Integer)
    flavour = Column("flavour",String)
    size = Column("size",String)
    unit_price = Column("unit_price",Float)
    order = Column("order",ForeignKey("orders.id"))

    def __init__(self,quantity,flavour,size,unit_price,order):
        self.quantity = quantity
        self.flavour = flavour
        self.size = size
        self.unit_price = unit_price
        self.order = order