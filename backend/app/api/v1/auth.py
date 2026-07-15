from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies.database import get_db
from app.schemas.user import UserCreate, UserLogin
from app.services.auth_service import register_user, login_user

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    return register_user(
        db=db,
        name=user.name,
        email=user.email,
        password=user.password,
    )


@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    return login_user(
        db=db,
        email=user.email,
        password=user.password,
    )