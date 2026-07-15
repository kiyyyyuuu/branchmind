from fastapi import FastAPI

from app.core.database import Base, engine
import app.models

from app.api.v1.auth import router as auth_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="BranchMind API"
)

app.include_router(auth_router)


@app.get("/")
def root():
    return {
        "message": "BranchMind Backend Running 🚀"
    }