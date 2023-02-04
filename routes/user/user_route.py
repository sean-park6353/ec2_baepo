from fastapi import APIRouter, Depends

from database import SessionLocal, get_db
from sqlalchemy.orm import Session
from sqlalchemy import select
from models import User


user_router = APIRouter(prefix="/user")

@user_router.get("")
async def get_all_user(
    session: Session = Depends(get_db)
):
    data = session.query(User).all()
    session.close()
    return data
    