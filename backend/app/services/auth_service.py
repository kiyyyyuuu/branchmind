from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.repositories.user_repository import UserRepository
from app.core.security import (
    hash_password,
    verify_password,
    create_access_token,
)

def register_user(db: Session, name: str, email: str, password: str):
    existing_user = UserRepository.get_by_email(db, email)
    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    UserRepository.create(
        db=db,
        name=name,
        email=email,
        password=hash_password(password),
)

    return {
        "message": "User registered successfully"
    }


def login_user(db: Session, email: str, password: str):
    db_user = UserRepository.get_by_email(db, email)

    if not db_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    if not verify_password(password, db_user.password):
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    token = create_access_token(
        {"sub": db_user.email}
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }